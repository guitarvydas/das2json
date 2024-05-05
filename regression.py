_r = None
EOF = chr (0)

def Das2json ():
    global _r
    _r.push_new_string ()
    _r.begin_breadcrumb ("Das2json")
    XML ()
    _r.append_returned_string ()
    Spaces ()
    _r.append_returned_string ()
    _r.need (EOF)
    _r.end_breadcrumb ("Das2json")
    return _r.return_string_pop ()

def XML ():
    global _r
    _r.push_new_string ()
    _r.begin_breadcrumb ("XML")
    Spaces ()
    _r.append_returned_string ()
    _r.need_and_append ("<")
    Stuff ()
    _r.append_returned_string ()
    if False:
        pass
    elif _r.maybe_append (">"):
        Content ()
        _r.append_returned_string ()
        _r.need_and_append ("</")
        Stuff ()
        _r.append_returned_string ()
        _r.need_and_append (">")
        pass
    elif _r.maybe_append ("/>"):
        pass
    elif True:
        Stuff ()
        _r.append_returned_string ()
        pass
    _r.end_breadcrumb ("XML")
    return _r.return_string_pop ()

def Content ():
    global _r
    _r.push_new_string ()
    _r.begin_breadcrumb ("Content")
    while True:
        Spaces ()
        _r.append_returned_string ()
        if False:
            pass
        elif _r.peek ("</"):
            break
            pass
        elif _r.peek ("<"):
            XML ()
            _r.append_returned_string ()
            pass
        elif True:
            Stuff ()
            _r.append_returned_string ()
            pass
        
    _r.end_breadcrumb ("Content")
    return _r.return_string_pop ()

def Attributes ():
    global _r
    _r.push_new_string ()
    _r.begin_breadcrumb ("Attributes")
    while True:
        if False:
            pass
        elif _r.peek ("style="):
            _r.accept_and_append ()
            String ()
            _r.append_returned_string ()
            pass
        elif _r.peek (">"):
            break
            pass
        elif _r.peek ("/>"):
            break
            pass
        elif _r.peek (EOF):
            break
            pass
        elif True:
            _r.accept_and_append ()
            pass
        
    _r.end_breadcrumb ("Attributes")
    return _r.return_string_pop ()

def Stuff ():
    global _r
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
        elif _r.peek (EOF):
            break
            pass
        elif True:
            _r.accept_and_append ()
            pass
        
    _r.end_breadcrumb ("Stuff")
    return _r.return_string_pop ()

def Spaces ():
    global _r
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
        elif _r.peek (EOF):
            break
            pass
        elif True:
            break
            pass
        
    _r.end_breadcrumb ("Spaces")
    return _r.return_string_pop ()

def String ():
    global _r
    _r.push_new_string ()
    _r.begin_breadcrumb ("String")
    _r.need_and_append ("\"")
    NotDquotes ()
    _r.append_returned_string ()
    _r.need_and_append ("\"")
    _r.end_breadcrumb ("String")
    return _r.return_string_pop ()

def NotDquotes ():
    global _r
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
        self.clear ()

    def getc (self):
        # ensure that the next character is in the cache
        # if the cache is not empty and the index is in bounds, then the character is already in place
        # else, get a character from stdin and append it to the cache
        # for convenience EOF is a character and is defined above
        if len (self.cache) == 0:
            c = sys.stdin.read (1)
            if 1 > len (c):
                c = EOF
            self.stdin_position += 1
            self.cache = [InCharacter (c=c, position=self.stdin_position)]
            self.cache_index = 0
        elif len (self.cache) == (self.cache_index + 1):
            c = sys.stdin.read (1)
            if 1 > len (c):
                c = EOF
            self.stdin_position += 1
            self.cache.append (InCharacter (c=c, position=self.stdin_position))
            self.cache_index += 1
        elif self.cache [self.cache_index] != EOF:
            self.cache_index += 1
        else:
            pass

    def rewind (self):
        self.cache_index = 0

    def clear (self):
        self.cache = []
        self.cache_index = None
        self.getc ()

    def accept (self):
        r = self.cache_toString ()
        self.clear ()
        #print (f'CharacterStream.accept "{r}"')
        return r

    def current_char (self):
        return self.cache [self.cache_index].c

    def current_input_position (self):
        return self.stdin_position

    def cache_toString (self):
        s = ""
        for in_c in self.cache:
            s = s + in_c.c
        return s


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
            r = self.string_stack.pop ()
            self.return_stack.append (r)

    def begin_breadcrumb (self, name):
        self.breadcrumb_wip_depth += 1
        b = Breadcrumb (name, self.breadcrumb_wip_depth, self.instream.current_input_position ())
        self.breadcrumb_wip_stack.append (b)
        # print (f'\x1B[43mbegin {b.name} depth={b.depth} position={b.position}\x1B[0m')
        
    def end_breadcrumb (self, name):
        b = self.breadcrumb_wip_stack.pop ()
        self.breadcrumb_stack.append (b)
        self.breadcrumb_wip_depth -= 1
        # print (f'\x1B[47mend {b.name} depth={b.depth} position={b.position}\x1B[0m')

    def append (self, s):
        self.string_stack [-1] = self.string_stack [-1] + s
        
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

    def eof (self):
        return EOF == self.instream.current_char ()

    def peek_recursively (self, s):
        global EOF
        if 0 == len (s):
            if self.eof ():
                return True
            else:
                return False
        elif s [0] == self.instream.current_char ():
            if 1 == len (s):
                return True
            else:
                self.instream.getc ()
                return self.peek_recursively (s [1:])
        else:
            return False

    def append_returned_string (self):
        s = self.return_stack.pop ()
        self.append (s)

    def need (self, s):
        if self.peek (s):
            pass
        else:
            self.error (s)

    def need_and_append (self, s):
        if self.peek (s):
            self.accept_and_append ()
        else:
            self.error (s)

    def maybe_append (self, s):
        if self.peek (s):
            self.accept_and_append ()
            return True
        else:
            return False

    def pop_return_value (self):
        r = self.return_stack.pop ()
        return r

    def error (self, s):
        b = self.breadcrumb_wip_stack [-1]
        c = self.instream.current_char ()
        c = make_printable (c)
        s = make_printable (s)
        print (f'\x1B[101mReceptor error at input position {self.instream.current_input_position ()} wanted "{s}" got "{c}" (rule {b.name} beginning at {b.position})"\x1B[0m')
        sys.exit (1)

def make_printable (c):        
    if c == EOF:
        c = "_end"
    elif c == "\n":
        c = "_newline"
    elif c == "\t":
        c = "_tab"
    elif c == " ":
        c = "_space"
    else:
        pass
    return c
            

def _begin ():
    global _r
    _r = Receptor ()
    
_begin ()
Das2json ()
s = _r.pop_return_value ()
print (s)

