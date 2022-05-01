#!/usr/bin/env python3
# tools.py
# cell_7
import mpos
import dispatcher

class _tools (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['go']
        self.outputs=['baton', 'quit']
    def react (self, inputMessage):
        import subprocess
        r = subprocess.run (["make", "tools"])
        if (r.returncode != 0):
            self.send ("quit", f"error {r} in make tools")
        else:
            self.send ("baton", True)
        return super ().react (inputMessage)
