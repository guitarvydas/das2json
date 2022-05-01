#!/usr/bin/env python3
# d2py.py
# cell_6
import mpos
import dispatcher
import abort
import tools
import build
import clean

class _d2py (mpos.Container):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['go']
        self.outputs=[]

        child0 = abort._abort (dispatcher, self, 'abort')
        child1 = tools._tools (dispatcher, self, 'tools')
        child2 = build._build (dispatcher, self, 'build')
        child3 = clean._clean (dispatcher, self, 'clean')
        conn0 = mpos.Connector ([mpos.Sender ('clean', 'baton')], [mpos.Receiver ('tools', 'go')])
        conn1 = mpos.Connector ([mpos.Sender ('clean', 'quit')], [mpos.Receiver ('abort', 'quit')])
        conn2 = mpos.Connector ([mpos.Sender ('tools', 'baton')], [mpos.Receiver ('build', 'go')])
        conn3 = mpos.Connector ([mpos.Sender ('tools', 'quit')], [mpos.Receiver ('abort', 'quit')])
        conn4 = mpos.Connector ([mpos.Sender ('build', 'quit')], [mpos.Receiver ('abort', 'quit')])
        conn5 = mpos.Connector ([mpos.Sender ('', 'go')], [mpos.Receiver ('clean', 'go')])
        self.connections = [ conn0, conn1, conn2, conn3, conn4, conn5 ]
        self.children = {'abort':child0, 'tools':child1, 'build':child2, 'clean':child3}
