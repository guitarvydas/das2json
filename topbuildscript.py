#!/usr/bin/env python3
import dispatcher
import buildscript
disp = dispatcher.Dispatcher ()
top = buildscript._buildscript (disp, None, '')
top.kickstart ()
disp.dispatch ()
