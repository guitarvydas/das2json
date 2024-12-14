def Das2json (_r):                                          #line 1
    _r.push_new_string ()
    _r.begin_breadcrumb ("Das2json")
    _r.call (XML)
    _r.append_returned_string ()
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.eof ()                                               #line 2
                                                            #line 3
    _r.end_breadcrumb ("Das2json")
    return _r.return_string_pop ()

def XML (_r):                                               #line 4
    _r.push_new_string ()
    _r.begin_breadcrumb ("XML")
    _r.call (Spaces)
    _r.append_returned_string ()
    _r.need_and_append ("<")
    _r.call (Name)
    _r.append_returned_string ()
    _r.call (Attributes)
    _r.append_returned_string ()
                                                            #line 5
    if False:
        pass
    elif _r.maybe_append (">"):
        _r.call (Content)
        _r.append_returned_string ()
        _r.need_and_append ("</")
        _r.call (Stuff)
        _r.append_returned_string ()
        _r.need_and_append (">")
                                                            #line 7
        pass
    elif _r.maybe_append ("/>"):

        pass
                                                            #line 10
    _r.end_breadcrumb ("XML")
    return _r.return_string_pop ()

def Content (_r):                                           #line 11
    _r.push_new_string ()
    _r.begin_breadcrumb ("Content")

    while True:                                             #line 12
        _r.call (Spaces)
        _r.append_returned_string ()
                                                            #line 13
        if False:
            pass
        elif _r.peek ("</"):
            break                                           #line 15

            pass
        elif _r.peek ("<mxGeometry "):
            _r.call (mxGeometry)
            _r.append_returned_string ()
                                                            #line 16
            pass
        elif _r.peek ("<"):
            _r.call (XML)
            _r.append_returned_string ()
                                                            #line 17
            pass
        elif True:
            _r.call (Stuff)
            _r.append_returned_string ()
                                                            #line 18
            pass
                                                            #line 20
                                                            #line 21
    _r.end_breadcrumb ("Content")
    return _r.return_string_pop ()

def mxGeometry (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("mxGeometry")
    _r.call (XML)
    _r.append_returned_string ()
                                                            #line 22
    _r.end_breadcrumb ("mxGeometry")
    return mxGeometry__action__ (_r)

def Attributes (_r):                                        #line 24
    _r.push_new_string ()
    _r.begin_breadcrumb ("Attributes")

    while True:                                             #line 25

        if False:
            pass
        elif _r.peek ("style="):
            _r.call (Style)
            _r.append_returned_string ()
                                                            #line 27
            pass
        elif _r.peek (">"):
            break                                           #line 28

            pass
        elif _r.peek ("/>"):
            break                                           #line 29

            pass
        elif _r.eof ():
            break                                           #line 30

            pass
        elif True:
            _r.accept_and_append ()                         #line 31

            pass
                                                            #line 33
                                                            #line 34
    _r.end_breadcrumb ("Attributes")
    return _r.return_string_pop ()

def Style (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Style")
    _r.need_and_append ("style=")
    _r.call (String)
    _r.append_returned_string ()
                                                            #line 35
    _r.end_breadcrumb ("Style")
    return Style__action__ (_r)

def Name (_r):                                              #line 37
    _r.push_new_string ()
    _r.begin_breadcrumb ("Name")

    while True:                                             #line 38

        if False:
            pass
        elif _r.peek (" "):
            break                                           #line 40

            pass
        elif _r.peek ("\t"):
            break                                           #line 41

            pass
        elif _r.peek ("\n"):
            break                                           #line 42

            pass
        elif _r.peek (">"):
            break                                           #line 43

            pass
        elif _r.peek ("<"):
            break                                           #line 44

            pass
        elif _r.peek ("/>"):
            break                                           #line 45

            pass
        elif _r.eof ():
            break                                           #line 46

            pass
        elif True:
            _r.accept_and_append ()                         #line 47

            pass
                                                            #line 49
                                                            #line 50
    _r.end_breadcrumb ("Name")
    return _r.return_string_pop ()

def Stuff (_r):                                             #line 51
    _r.push_new_string ()
    _r.begin_breadcrumb ("Stuff")

    while True:                                             #line 52

        if False:
            pass
        elif _r.peek (">"):
            break                                           #line 54

            pass
        elif _r.peek ("<"):
            break                                           #line 55

            pass
        elif _r.peek ("/>"):
            break                                           #line 56

            pass
        elif _r.eof ():
            break                                           #line 57

            pass
        elif True:
            _r.accept_and_append ()                         #line 58

            pass
                                                            #line 60
                                                            #line 61
    _r.end_breadcrumb ("Stuff")
    return _r.return_string_pop ()

def Spaces (_r):                                            #line 62
    _r.push_new_string ()
    _r.begin_breadcrumb ("Spaces")

    while True:                                             #line 63

        if False:
            pass
        elif _r.peek (" "):
            _r.accept_and_append ()                         #line 65

            pass
        elif _r.peek ("\t"):
            _r.accept_and_append ()                         #line 66

            pass
        elif _r.peek ("\n"):
            _r.accept_and_append ()                         #line 67

            pass
        elif True:
            break                                           #line 68

            pass
                                                            #line 70
                                                            #line 71
    _r.end_breadcrumb ("Spaces")
    return _r.return_string_pop ()

def String (_r):                                            #line 72
    _r.push_new_string ()
    _r.begin_breadcrumb ("String")
    _r.need_and_append ("\"")
    _r.call (NotDquotes)
    _r.append_returned_string ()
    _r.need_and_append ("\"")
                                                            #line 73
    _r.end_breadcrumb ("String")
    return _r.return_string_pop ()

def NotDquotes (_r):                                        #line 75
    _r.push_new_string ()
    _r.begin_breadcrumb ("NotDquotes")

    while True:                                             #line 76

        if False:
            pass
        elif _r.peek ("\""):
            break                                           #line 78

            pass
        elif True:
            _r.accept_and_append ()                         #line 79

            pass
                                                            #line 81
                                                            #line 82
    _r.end_breadcrumb ("NotDquotes")
    return _r.return_string_pop ()

def EndMxCell (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("EndMxCell")
    _r.need_and_append ("</mxCell>")
    _r.call (Spaces)
    _r.append_returned_string ()
                                                            #line 83
    _r.end_breadcrumb ("EndMxCell")
    return _r.return_string_pop ()

def mxGeometry__action__ (_r):
    return _r.return_ignore_pop ()                          #line 85

def Style__action__ (_r):
    return _r.return_ignore_pop ()                          #line 86


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
