_in = None
EOF = chr (0)


def Das2json ():
    global _in
    _in.push_new_string ()
    _in.begin_breadcrumb ("Das2json")
    Spaces ()
    _in.append_returned_string ()
    _in.need_and_append ("<")
    Attributes ()
    _in.append_returned_string (s)
    if _in.maybe_append (">"):
        Content ()
        _in.append_returned_string ()
        _in.need_and_append ("</")
        Stuff ()
        _in.append_returned_string ()
        _in.need_and_append (">")
    elif _in.maybe_append ("/>"):
        pass
    else:
        Stuff ()
        _in.append_returned_string ()
    _in.end_breadcrumb ("Das2json")
    return _in.return_string_pop ()

def Content ():
    _in.push_new_string ()
    _in.begin_breadcrumb ("Content")
    while True:
        Spaces ()
        _in.append_returned_string ()
        if _in.peek ("</"):
            break
        elif _in.peek ("<"):
            Das2json ()
            _in.append_returned_string ()
        else:
            Stuff ()
            _in.append_returned_string ()
    _in.end_breadcrumb ("Content")
    return _in.return_string_pop ()
          
            
def Attributes ():
    _in.push_new_string ()
    _in.begin_breadcrumb ("Attributes")
    while True:
        if _in.peek ("style="):
            _in.accept_and_append ()
            String ()
            _in.append_returned_string ()
        elif _in.peek (">"):
            break
        elif _in.peek ("/>"):
            break
        elif _in.eof ():
            break
        else:
            _in.accept_and_append ()
    _in.end_breadcrumb ("Attributes")
    return _in.return_string_pop ()

def Stuff ():
    _in.push_new_string ()
    _in.begin_breadcrumb ("Stuff")
    while True:
        if _in.peek (">"):
            break
        elif _in.peek ("<"):
            break
        elif _in.peek ("/>"):
            break
        elif _in.peek (EOF):
            break
        else:
            _in.accept_and_append ()
    _in.end_breadcrumb ("Stuff")
    return _in.return_string_pop ()

def Spaces ():
    global EOF
    _in.push_new_string ()
    _in.begin_breadcrumb ("Spaces")
    while True:
        if _in.peek (" "):
            _in.accept_and_append ()
        elif _in.peek ("\t"):
            _in.accept_and_append ()
        elif _in.peek ("\n"):
            _in.accept_and_append ()
        elif _in.peek (EOF):
            break
        else:
            break
    _in.end_breadcrumb ("Spaces")
    return _in.return_string_pop ()
        
def String ():
    _in.push_new_string ()
    _in.begin_breadcrumb ("String")
    _in.need_and_append ('"')
    NotDquotes ()
    _in.append_returned_string ()
    _in.need_and_append ('"')
    _in.end_breadcrumb ("String")
    return _in.return_string_pop ()

def NotDquotes ():
    _in.push_new_string ()
    _in.begin_breadcrumb ("NotDquotes")
    while True:
        if _in.peek ('"'):
            break
        else:
            _in.accept_and_append ()
    _in.end_breadcrumb ("NotDquotes")
    return _in.return_string_pop ()






#####

import sys

class InCharacter:
    def __init__ (self, c='', position=0):
        self.c = c
        self.position = position

class Breadcrumb:
    def __init__ (self, name, depth, pos):
        self.name = name
        self.depth = depth
        self.position = pos
        
class CharacterStream:
    # we put input characters in a cache 
    # when pattern matching is successful, we grab (accept) the string in the cache and reset the cache
    # when pattern matching is unsuccessful, we simply rewind the stream to the front and try again
    
    def __init__ (self):
        self.stdin_position = 0
        self.cache = ""
        self.cache_index = None
        self.getc

    def getc (self):
        # ensure that the next character is in the cache
        # if the cache is not empty and the index is in bounds, then the character is already in place
        # else, get a character from stdin and append it to the cache
        # for convenience EOF is a character and is defined above
        if (len (self.cache) == 0) or (len (self.cache) == (self.cache_index + 1)):
            c = sys.stdin.read (1)
            if 1 > len (c):
                c = EOF
            self.stdin_position += 1
            self.cache = [InCharacter (c=c, position=self.stdin_position)]
            self.cache_index = 0
        elif self.cache [self.cache_index] != EOF:
            self.cache_index += 1
        else:
            pass

    def current_char (self):
        return self.cache [self.cache_index]

    def rewind (self):
        self.cache_index = 0

    def clear (self):
        self.cache = ""
        self.cache_index = None

    def accept (self):
        r = self.cache
        self.clear ()


class Receptor:
    # A receptor parses the input stream of characters and keeps track of how it got there and what it is working on.
    # A receptor uses rules that can call other rules (so, we need to use stacks, to keep everything separated).
    # Each rule begins a fresh string and builds it up.
    # When a rule finishes, it pops its own string off of the string stack and puts it onto the return stack - the caller
    #  deals with the returned string (typically by adding it to its own string). The caller must delete the returned value
    #  from the return stack. Note that the caller can further parse the returned string, if it so wishes.

    def __init__ (self):
        self.instream = CharacterStream ()
        self.string_stack = []
        self.return_stack = []
        self.breadcrumb_stack = []
        self.breadcrumb_wip_stack = []
        self.breadcrumb_wip_depth = 0
        
    def push_new_string (self):
        self.string_stack.append ("")
        
    def return_string_pop (self):
            self.return_stack.append (self.string_stack.pop ())

    def begin_breadcrumb (self, name):
        self.breadcrumb_wip_depth += 1
        b = Breadcrumb (name, self.breadcrumb_wip_depth, self.current_input_position ())
        self.breadcrumb_wip_stack.append (b)
        
    def end_breadcrumb (self, name):
        self.breadcrumb_stack.append (self.breadcrumb_wip_stack.pop ())
        self.breadcrumb_wip_depth -= 1

    def append (self, s):
        self.string_stack [-1].append (s)
        
    def accept_and_append (self):
        s = self.instream.accept ()
        self.append (s)

    def peek (self, s):
        if self.peek_recursively (s):
            self.instream.rewind ()
            return True
        else:
            self.instream.rewind ()
            return False

    def append_returned_string (self):
        s = self.return_stack.pop ()
        self.append (s)

    def need_and_append (self, s):
        if self.peek (s):
            self.append (s)
        else:
            self.error (s)

    def maybe_append (self, s):
        if self.peek (s):
            self.append (s)
            return True
        else:
            return False

    def error (s):
        print (f'\x1B[101mReceptor error at input position {self.breadcrumb_wip_stack [-1].position}\x1B[0m')

def _begin ():
    global _in
    _in = InputStream ()
    
_begin ()
Das2json ()
