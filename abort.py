#!/usr/bin/env python3
# abort.py
# cell_25
import mpos
import dispatcher

class _abort (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['quit']
        self.outputs=[]
    def react (self, inputMessage):
        self.quit (inputMessage.data)
        return super ().react (inputMessage)
