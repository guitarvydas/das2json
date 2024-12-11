def Das2json (_r):                                          #line 1
    _r.push_new_string ()
    _r.begin_breadcrumb ("Das2json")
    _r.trace ("@0")                                         #line 2
    _r.call (XML)
    _r.append_returned_string ()
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.eof ()                                               #line 3
                                                            #line 4
    _r.end_breadcrumb ("Das2json")
    return Das2json__action__ (_r)

def XML (_r):                                               #line 5
    _r.push_new_string ()
    _r.begin_breadcrumb ("XML")
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.need_and_append ("<")
    _r.call (Name)
    _r.append_returned_string ()
    _r.call (Attributes)
    _r.append_returned_string ()
                                                            #line 6
    if False:
        pass
    elif _r.maybe_append (">"):
        _r.call (Content)
        _r.append_returned_string ()
        _r.need_and_append ("</")
        _r.call (Stuff)
        _r.append_returned_string ()
        _r.need_and_append (">")
                                                            #line 8
        pass
    elif _r.maybe_append ("/>"):

        pass
                                                            #line 11
    _r.end_breadcrumb ("XML")
    return _r.return_string_pop ()

def Content (_r):                                           #line 12
    _r.push_new_string ()
    _r.begin_breadcrumb ("Content")

    while True:                                             #line 13
        _r.call (Spaces)
        _r.append_returned_string ()
                                                            #line 14
        if False:
            pass
        elif _r.peek ("</"):
            break                                           #line 16

            pass
        elif _r.peek ("<mxGeometry "):
            _r.call (mxGeometry)
            _r.append_returned_string ()
                                                            #line 17
            pass
        elif _r.peek ("<"):
            _r.call (XML)
            _r.append_returned_string ()
                                                            #line 18
            pass
        elif True:
            _r.call (Stuff)
            _r.append_returned_string ()
                                                            #line 19
            pass
                                                            #line 21
                                                            #line 22
    _r.end_breadcrumb ("Content")
    return _r.return_string_pop ()

def mxGeometry (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("mxGeometry")
    _r.call (XML)
    _r.append_returned_string ()
                                                            #line 23
    _r.end_breadcrumb ("mxGeometry")
    return mxGeometry__action__ (_r)

def Attributes (_r):                                        #line 25
    _r.push_new_string ()
    _r.begin_breadcrumb ("Attributes")

    while True:                                             #line 26

        if False:
            pass
        elif _r.peek ("style="):
            _r.call (Style)
            _r.append_returned_string ()
                                                            #line 28
            pass
        elif _r.peek (">"):
            break                                           #line 29

            pass
        elif _r.peek ("/>"):
            break                                           #line 30

            pass
        elif _r.eof ():
            break                                           #line 31

            pass
        elif True:
            _r.accept_and_append ()                         #line 32

            pass
                                                            #line 34
                                                            #line 35
    _r.end_breadcrumb ("Attributes")
    return _r.return_string_pop ()

def Style (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Style")
    _r.need_and_append ("style=")
    _r.call (String)
    _r.append_returned_string ()
                                                            #line 36
    _r.end_breadcrumb ("Style")
    return Style__action__ (_r)

def Name (_r):                                              #line 38
    _r.push_new_string ()
    _r.begin_breadcrumb ("Name")

    while True:                                             #line 39

        if False:
            pass
        elif _r.peek (" "):
            break                                           #line 41

            pass
        elif _r.peek ("\t"):
            break                                           #line 42

            pass
        elif _r.peek ("\n"):
            break                                           #line 43

            pass
        elif _r.peek (">"):
            break                                           #line 44

            pass
        elif _r.peek ("<"):
            break                                           #line 45

            pass
        elif _r.peek ("/>"):
            break                                           #line 46

            pass
        elif _r.eof ():
            break                                           #line 47

            pass
        elif True:
            _r.accept_and_append ()                         #line 48

            pass
                                                            #line 50
                                                            #line 51
    _r.end_breadcrumb ("Name")
    return _r.return_string_pop ()

def Stuff (_r):                                             #line 52
    _r.push_new_string ()
    _r.begin_breadcrumb ("Stuff")

    while True:                                             #line 53

        if False:
            pass
        elif _r.peek (">"):
            break                                           #line 55

            pass
        elif _r.peek ("<"):
            break                                           #line 56

            pass
        elif _r.peek ("/>"):
            break                                           #line 57

            pass
        elif _r.eof ():
            break                                           #line 58

            pass
        elif True:
            _r.accept_and_append ()                         #line 59

            pass
                                                            #line 61
                                                            #line 62
    _r.end_breadcrumb ("Stuff")
    return _r.return_string_pop ()

def Spaces (_r):                                            #line 63
    _r.push_new_string ()
    _r.begin_breadcrumb ("Spaces")

    while True:                                             #line 64

        if False:
            pass
        elif _r.peek (" "):
            _r.accept_and_append ()                         #line 66

            pass
        elif _r.peek ("\t"):
            _r.accept_and_append ()                         #line 67

            pass
        elif _r.peek ("\n"):
            _r.accept_and_append ()                         #line 68

            pass
        elif True:
            break                                           #line 69

            pass
                                                            #line 71
                                                            #line 72
    _r.end_breadcrumb ("Spaces")
    return _r.return_string_pop ()

def String (_r):                                            #line 73
    _r.push_new_string ()
    _r.begin_breadcrumb ("String")
    _r.need_and_append ("\"")
    _r.call (NotDquotes)
    _r.append_returned_string ()
    _r.need_and_append ("\"")
                                                            #line 74
    _r.end_breadcrumb ("String")
    return _r.return_string_pop ()

def NotDquotes (_r):                                        #line 76
    _r.push_new_string ()
    _r.begin_breadcrumb ("NotDquotes")

    while True:                                             #line 77

        if False:
            pass
        elif _r.peek ("\""):
            break                                           #line 79

            pass
        elif True:
            _r.accept_and_append ()                         #line 80

            pass
                                                            #line 82
                                                            #line 83
    _r.end_breadcrumb ("NotDquotes")
    return _r.return_string_pop ()

def EndMxCell (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("EndMxCell")
    _r.need_and_append ("</mxCell>")
    _r.call (Spaces)
    _r.append_returned_string ()
                                                            #line 84
    _r.end_breadcrumb ("EndMxCell")
    return EndMxCell__action__ (_r)

def Das2json__action__ (_r):
    return _r.return_string_pop ()                          #line 86

def mxGeometry__action__ (_r):
    return _r.return_ignore_pop ()                          #line 87

def Style__action__ (_r):
    return _r.return_ignore_pop ()                          #line 88


import receptor
import sys
import kernel as zd
class Place_Holder:
    def __init__ (self):
        self.name = "place-holder-name"

# main...
_r = receptor.Receptor (sys.stdin, zd.make_leaf (zd.gensymbol ("sp"), Place_Holder (), None, "place-holder handler"))
Das2json (_r)
s = _r.pop_return_value ()
print (s)
