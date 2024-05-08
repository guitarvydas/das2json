
def Das2json (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Das2json")
    XML (_r)
    _r.append_returned_string ()
    Spaces (_r)
    _r.append_returned_string ()
    _r.eof ()
    _r.end_breadcrumb ("Das2json")
    return _r.return_string_pop ()

def XML (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("XML")
    Spaces (_r)
    _r.append_returned_string ()
    _r.need_and_append ("<")
    Stuff (_r)
    _r.append_returned_string ()
    if False:
        pass
    elif _r.maybe_append (">"):
        Content (_r)
        _r.append_returned_string ()
        _r.need_and_append ("</")
        Stuff (_r)
        _r.append_returned_string ()
        _r.need_and_append (">")
        pass
    elif _r.maybe_append ("/>"):
        pass
    _r.end_breadcrumb ("XML")
    return _r.return_string_pop ()

def Content (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Content")
    while True:
        Spaces (_r)
        _r.append_returned_string ()
        if False:
            pass
        elif _r.peek ("</"):
            break
            pass
        elif _r.peek ("<"):
            XML (_r)
            _r.append_returned_string ()
            pass
        elif True:
            Stuff (_r)
            _r.append_returned_string ()
            pass
        
    _r.end_breadcrumb ("Content")
    return _r.return_string_pop ()

def Attributes (_r):
    _r.push_new_string ()
    _r.begin_breadcrumb ("Attributes")
    while True:
        if False:
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
            Stuff (_r)
            _r.append_returned_string ()
            pass
        
    _r.end_breadcrumb ("Attributes")
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
    NotDquotes (_r)
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


import receptor
_r = receptor.Receptor ()
Das2json (_r)
s = _r.pop_return_value ()
print (s)

