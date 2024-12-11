import asyncio
import websockets
import json
import time
import subprocess
import os

class FileWatcher:
    def __init__(self):
        self.file_timestamps = {}
        self.watch_list = []
        self.send_pairs = []
        self.connected_clients = set()
        
    def load_watch_list(self):
        """Load list of files to watch from watch.txt"""
        try:
            with open('watch.txt', 'r') as f:
                self.watch_list = [line.strip() for line in f if line.strip()]
            # Initialize timestamps for existing files only
            for file in self.watch_list:
                if os.path.exists(file):
                    self.file_timestamps[file] = os.path.getmtime(file)
        except FileNotFoundError:
            print("Error: watch.txt not found")
            return False
        return True

    def load_send_pairs(self):
        """Load key-file pairs from send.txt where each line is 'key filename'"""
        try:
            with open('send.txt', 'r') as f:
                self.send_pairs = []
                for line in f:
                    parts = line.strip().split()
                    if len(parts) >= 2:
                        key = parts[0]
                        filename = ' '.join(parts[1:])
                        self.send_pairs.append((key, filename))
        except FileNotFoundError:
            print("Error: send.txt not found")
            return False
        return True

    def check_files_changed(self):
        """Check if any existing watched files have changed"""
        changed = False
        for file in self.watch_list:
            if not os.path.exists(file):
                # Skip non-existent files
                continue
                
            try:
                current_mtime = os.path.getmtime(file)
                last_mtime = self.file_timestamps.get(file)
                
                if last_mtime is None:
                    # First time seeing this file
                    self.file_timestamps[file] = current_mtime
                elif current_mtime != last_mtime:
                    # File has changed
                    print (f'File {file} has changed')
                    changed = True
                    self.file_timestamps[file] = current_mtime
            except OSError as e:
                print(f"Error checking file {file}: {e}")
        return changed

    async def run_rebuild(self):
        """Run rebuild.bash and return result"""
        print (f'rebuild')
        try:
            process = await asyncio.create_subprocess_exec(
                './rebuild.bash',
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            print (f'run_rebuild /{process.returncode}/ /{stdout.decode ()}/ /{stderr.decode ()}/')
            return process.returncode, stderr.decode()
        except Exception as e:
            return 1, str(e)

    def collect_file_contents(self):
        """Collect contents of files specified in send.txt"""
        result = {}
        for key, filename in self.send_pairs:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                    result[key] = content
            except Exception as e:
                print(f"Error reading file {filename}: {e}")
                result[key] = f"Error reading file: {str(e)}"
        return result

    async def broadcast_message(self, message):
        """Send message to all connected clients"""
        if not self.connected_clients:
            return
        
        json_message = json.dumps(message)
        disconnected_clients = set()
        
        for client in self.connected_clients:
            try:
                await client.send(json_message)
            except websockets.exceptions.ConnectionClosed:
                disconnected_clients.add(client)
            except Exception as e:
                print(f"Error sending to client: {e}")
                disconnected_clients.add(client)
        
        # Remove disconnected clients
        self.connected_clients -= disconnected_clients

    async def clear (self):
        """Send nothing message to all connected clients to clear their displays"""
        await self.broadcast_message ({"Errors" : "begin..."})

    async def handle_client(self, websocket):
        """Handle individual WebSocket client"""
        self.connected_clients.add(websocket)
        try:
            await websocket.wait_closed()
        finally:
            self.connected_clients.remove(websocket)

    async def watch_and_rebuild(self):
        """Main loop to watch files and trigger rebuilds"""
        while True:
            if self.check_files_changed():
                # Run rebuild script only if changes detected in existing files
                print (f'watch_and_rebuild: clear')
                await self.clear ()
                return_code, stderr = await self.run_rebuild()
                
                print (f'watch_and_rebuild: {return_code} {stderr}')

                if return_code != 0:
                    error_message = {
                        "Errors": f"Build failed with code {return_code}{stderr}"
                    }
                    await self.broadcast_message(error_message)
                else:
                    contents = self.collect_file_contents()
                    await self.broadcast_message(contents)
            
            await asyncio.sleep(0.02)  # 20ms delay

async def main():
    watcher = FileWatcher()
    
    if not watcher.load_watch_list() or not watcher.load_send_pairs():
        return
    
    async with websockets.serve(watcher.handle_client, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        
        try:
            await watcher.watch_and_rebuild()
        except asyncio.CancelledError:
            print("Server shutting down...")
        except Exception as e:
            print(f"Error in main loop: {e}")

if __name__ == "__main__":
    asyncio.run(main())
