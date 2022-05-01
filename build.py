#!/usr/bin/env python3
# build.py
# cell_8
import mpos
import dispatcher

class _build (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['go']
        self.outputs=['quit']
    def react (self, inputMessage):
        import subprocess
        r = subprocess.run (["make", "helloworld.py"])
        if (r.returncode != 0):
            self.send ("quit", f"error {r} in make helloworld.py")
        
        
        return super ().react (inputMessage)
