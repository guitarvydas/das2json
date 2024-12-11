
# das2json-swib.drawio

def Das2json (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Das2json")
    _r.trace ("@0")
    _r.call (XML)
    _r.append_returned_string ()
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.eof ()
    _r.end_breadcrumb ("Das2json")
    return Das2json__action__ (_r)

def XML (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("XML")
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.need_and_append ("<")
    _r.call (Name)
    _r.append_returned_string ()
    _r.call (Attributes)
    _r.append_returned_string ()
    if False:
        pass
    elif _r.maybe_append (">"):
        _r.call (Content)
        _r.append_returned_string ()
        _r.call (ElementTail)
        _r.append_returned_string ()
        pass
    elif _r.maybe_append ("/>"):
        pass
    _r.end_breadcrumb ("XML")
    return _r.return_string_pop ()

def ElementTail (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("ElementTail")
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.need_and_append ("</")
    _r.call (Stuff)
    _r.append_returned_string ()
    _r.need_and_append (">")
    _r.end_breadcrumb ("ElementTail")
    return ElementTail__action__ (_r)

def Content (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Content")
    while True:
        _r.call (Spaces)
        _r.append_returned_string ()
        if False:
            pass
        elif _r.peek ("</"):
            break
            pass
        elif _r.peek ("<mxGeometry "):
            _r.call (mxGeometry)
            _r.append_returned_string ()
            pass
        elif _r.peek ("<"):
            _r.call (XML)
            _r.append_returned_string ()
            pass
        elif True:
            _r.call (Stuff)
            _r.append_returned_string ()
            pass
        
    _r.end_breadcrumb ("Content")
    return _r.return_string_pop ()

def mxGeometry (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("mxGeometry")
    _r.call (XML)
    _r.append_returned_string ()
    _r.end_breadcrumb ("mxGeometry")
    return mxGeometry__action__ (_r)

def Attributes (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Attributes")
    while True:
        if False:
            pass
        elif _r.peek ("style="):
            _r.call (Style)
            _r.append_returned_string ()
            pass
        elif _r.peek (">"):
            break
            pass
        elif _r.peek ("/>"):
            break
            pass
        elif _r.eof ():
            break
            pass
        elif True:
            _r.accept_and_append ()
            pass
        
    _r.end_breadcrumb ("Attributes")
    return _r.return_string_pop ()

def Style (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Style")
    _r.need_and_append ("style=")
    _r.call (String)
    _r.append_returned_string ()
    _r.end_breadcrumb ("Style")
    return Style__action__ (_r)

def Name (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Name")
    while True:
        if False:
            pass
        elif _r.peek (" "):
            break
            pass
        elif _r.peek ("\t"):
            break
            pass
        elif _r.peek ("\n"):
            break
            pass
        elif _r.peek (">"):
            break
            pass
        elif _r.peek ("<"):
            break
            pass
        elif _r.peek ("/>"):
            break
            pass
        elif _r.eof ():
            break
            pass
        elif True:
            _r.accept_and_append ()
            pass
        
    _r.end_breadcrumb ("Name")
    return _r.return_string_pop ()

def Stuff (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Stuff")
    while True:
        if False:
            pass
        elif _r.peek (">"):
            break
            pass
        elif _r.peek ("<"):
            break
            pass
        elif _r.peek ("/>"):
            break
            pass
        elif _r.eof ():
            break
            pass
        elif True:
            _r.accept_and_append ()
            pass
        
    _r.end_breadcrumb ("Stuff")
    return _r.return_string_pop ()

def Spaces (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Spaces")
    while True:
        if False:
            pass
        elif _r.peek (" "):
            _r.accept_and_append ()
            pass
        elif _r.peek ("\t"):
            _r.accept_and_append ()
            pass
        elif _r.peek ("\n"):
            _r.accept_and_append ()
            pass
        elif True:
            break
            pass
        
    _r.end_breadcrumb ("Spaces")
    return _r.return_string_pop ()

def String (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("String")
    _r.need_and_append ("\"")
    _r.call (NotDquotes)
    _r.append_returned_string ()
    _r.need_and_append ("\"")
    _r.end_breadcrumb ("String")
    return _r.return_string_pop ()

def NotDquotes (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("NotDquotes")
    while True:
        if False:
            pass
        elif _r.peek ("\""):
            break
            pass
        elif True:
            _r.accept_and_append ()
            pass
        
    _r.end_breadcrumb ("NotDquotes")
    return _r.return_string_pop ()

def EndMxCell (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("EndMxCell")
    _r.need_and_append ("</mxCell>")
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.end_breadcrumb ("EndMxCell")
    return EndMxCell__action__ (_r)

def Das2json__action__ (_r):
    return _r.return_string_pop ()

def mxGeometry__action__ (_r):
    return _r.return_ignore_pop ()

def Style__action__ (_r):
    return _r.return_ignore_pop ()

def ElementTail__action__ (_r):
    return _r.return_ignore_pop ()


import receptor
import sys
import py0d as zd
class Place_Holder:
    def __init__ (self):
        self.name = "place-holder-name"
_r = receptor.Receptor (sys.stdin, zd.make_leaf (zd.gensym ("swib"), Place_Holder (), None, "place-holder handler"))
Das2json (_r)
s = _r.pop_return_value ()
print (s)

