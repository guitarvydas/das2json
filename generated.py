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
                                                            #line 7
        if False:
            pass
        elif _r.peek ("</mxCell>"):
            _r.call (EndMxCell)
            _r.append_returned_string ()
                                                            #line 9
            pass
        elif True:
            _r.need_and_append ("</")
            _r.call (Stuff)
            _r.append_returned_string ()
            _r.need_and_append (">")
                                                            #line 10
            pass

        pass
    elif _r.maybe_append ("/>"):

        pass
                                                            #line 14
    _r.end_breadcrumb ("XML")
    return _r.return_string_pop ()

def Content (_r):                                           #line 15
    _r.push_new_string ()
    _r.begin_breadcrumb ("Content")

    while True:                                             #line 16
        _r.call (Spaces)
        _r.append_returned_string ()
                                                            #line 17
        if False:
            pass
        elif _r.peek ("</"):
            break                                           #line 19

            pass
        elif _r.peek ("<mxGeometry "):
            _r.call (mxGeometry)
            _r.append_returned_string ()
                                                            #line 20
            pass
        elif _r.peek ("<"):
            _r.call (XML)
            _r.append_returned_string ()
                                                            #line 21
            pass
        elif True:
            _r.call (Stuff)
            _r.append_returned_string ()
                                                            #line 22
            pass
                                                            #line 24
                                                            #line 25
    _r.end_breadcrumb ("Content")
    return _r.return_string_pop ()

def mxGeometry (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("mxGeometry")
    _r.call (XML)
    _r.append_returned_string ()
                                                            #line 26
    _r.end_breadcrumb ("mxGeometry")
    return mxGeometry__action__ (_r)

def Attributes (_r):                                        #line 28
    _r.push_new_string ()
    _r.begin_breadcrumb ("Attributes")

    while True:                                             #line 29

        if False:
            pass
        elif _r.peek ("style="):
            _r.call (Style)
            _r.append_returned_string ()
                                                            #line 31
            pass
        elif _r.peek (">"):
            break                                           #line 32

            pass
        elif _r.peek ("/>"):
            break                                           #line 33

            pass
        elif _r.eof ():
            break                                           #line 34

            pass
        elif True:
            _r.accept_and_append ()                         #line 35

            pass
                                                            #line 37
                                                            #line 38
    _r.end_breadcrumb ("Attributes")
    return _r.return_string_pop ()

def Style (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Style")
    _r.need_and_append ("style=")
    _r.call (String)
    _r.append_returned_string ()
                                                            #line 39
    _r.end_breadcrumb ("Style")
    return Style__action__ (_r)

def Name (_r):                                              #line 41
    _r.push_new_string ()
    _r.begin_breadcrumb ("Name")

    while True:                                             #line 42

        if False:
            pass
        elif _r.peek (" "):
            break                                           #line 44

            pass
        elif _r.peek ("\t"):
            break                                           #line 45

            pass
        elif _r.peek ("\n"):
            break                                           #line 46

            pass
        elif _r.peek (">"):
            break                                           #line 47

            pass
        elif _r.peek ("<"):
            break                                           #line 48

            pass
        elif _r.peek ("/>"):
            break                                           #line 49

            pass
        elif _r.eof ():
            break                                           #line 50

            pass
        elif True:
            _r.accept_and_append ()                         #line 51

            pass
                                                            #line 53
                                                            #line 54
    _r.end_breadcrumb ("Name")
    return _r.return_string_pop ()

def Stuff (_r):                                             #line 55
    _r.push_new_string ()
    _r.begin_breadcrumb ("Stuff")

    while True:                                             #line 56

        if False:
            pass
        elif _r.peek (">"):
            break                                           #line 58

            pass
        elif _r.peek ("<"):
            break                                           #line 59

            pass
        elif _r.peek ("/>"):
            break                                           #line 60

            pass
        elif _r.eof ():
            break                                           #line 61

            pass
        elif True:
            _r.accept_and_append ()                         #line 62

            pass
                                                            #line 64
                                                            #line 65
    _r.end_breadcrumb ("Stuff")
    return _r.return_string_pop ()

def Spaces (_r):                                            #line 66
    _r.push_new_string ()
    _r.begin_breadcrumb ("Spaces")

    while True:                                             #line 67

        if False:
            pass
        elif _r.peek (" "):
            _r.accept_and_append ()                         #line 69

            pass
        elif _r.peek ("\t"):
            _r.accept_and_append ()                         #line 70

            pass
        elif _r.peek ("\n"):
            _r.accept_and_append ()                         #line 71

            pass
        elif True:
            break                                           #line 72

            pass
                                                            #line 74
                                                            #line 75
    _r.end_breadcrumb ("Spaces")
    return _r.return_string_pop ()

def String (_r):                                            #line 76
    _r.push_new_string ()
    _r.begin_breadcrumb ("String")
    _r.need_and_append ("\"")
    _r.call (NotDquotes)
    _r.append_returned_string ()
    _r.need_and_append ("\"")
                                                            #line 77
    _r.end_breadcrumb ("String")
    return _r.return_string_pop ()

def NotDquotes (_r):                                        #line 79
    _r.push_new_string ()
    _r.begin_breadcrumb ("NotDquotes")

    while True:                                             #line 80

        if False:
            pass
        elif _r.peek ("\""):
            break                                           #line 82

            pass
        elif True:
            _r.accept_and_append ()                         #line 83

            pass
                                                            #line 85
                                                            #line 86
    _r.end_breadcrumb ("NotDquotes")
    return _r.return_string_pop ()

def EndMxCell (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("EndMxCell")
    _r.need_and_append ("</mxCell>")
    _r.call (Spaces)
    _r.append_returned_string ()
                                                            #line 87
    _r.end_breadcrumb ("EndMxCell")
    return EndMxCell__action__ (_r)

def mxGeometry__action__ (_r):
    return _r.return_ignore_pop ()                          #line 89

def Style__action__ (_r):
    return _r.return_ignore_pop ()                          #line 90

def EndMxCell__action__ (_r):
    return _r.return_ignore_pop ()                          #line 91


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
