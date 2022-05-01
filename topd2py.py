#!/usr/bin/env python3
import dispatcher
import d2py
disp = dispatcher.Dispatcher ()
top = d2py._d2py (disp, None, '')
top.kickstart ()
disp.dispatch ()
