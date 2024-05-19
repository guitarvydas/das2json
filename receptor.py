
#####


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
    
    def __init__ (self, instream):
        self.position = 0
        self.instream = instream
        self.clear ()

    def getc (self):
        # ensure that the next character is in the cache
        # if the cache is not empty and the index is in bounds, then the character is already in place
        # else, get a character from instream and append it to the cache
        # for convenience EOF is a character and is defined above
        if len (self.cache) == 0:
            c = self.instream.read (1)
            if 1 > len (c):
                c = self.endchar ()
            self.position += 1
            self.cache = [InCharacter (c=c, position=self.position)]
            self.cache_index = 0
        elif len (self.cache) == (self.cache_index + 1):
            c = self.instream.read (1)
            if 1 > len (c):
                c = self.endchar ()
            self.position += 1
            self.cache.append (InCharacter (c=c, position=self.position))
            self.cache_index += 1
        elif self.cache [self.cache_index] != self.endchar ():
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
        return r

    def current_char (self):
        return self.cache [self.cache_index].c

    def current_input_position (self):
        return self.position

    def cache_toString (self):
        s = ""
        for in_c in self.cache:
            s = s + in_c.c
        return s

    def endchar (self):
        return chr (0)

class Receptor:
    # A receptor parses the input stream of characters and keeps track of how it got there and what it is working on.
    # A receptor uses rules that can call other rules (so, we need to use stacks, to keep everything separated).
    # Each rule begins a fresh string and builds it up.
    # When a rule finishes, it pops its own string off of the string stack and puts it onto the return stack - the caller
    #  deals with the returned string (typically by adding it to its own string). The caller must delete the returned value
    #  from the return stack. Note that the caller can further parse the returned string, if it so wishes.

    def __init__ (self, instream, eh):
        self.instream = CharacterStream (instream)
        self.string_stack = []
        self.return_stack = []
        self.breadcrumb_stack = []
        self.breadcrumb_wip_stack = []
        self.breadcrumb_wip_depth = 0
        self.eh = eh

    def push_new_string (self):
        self.string_stack.append ("")
        
    def return_string_pop (self):
            r = self.string_stack.pop ()
            self.return_stack.append (r)

    def return_ignore_pop (self):
            r = self.string_stack.pop ()
            self.return_stack.append ("")

    def begin_breadcrumb (self, name):
        self.breadcrumb_wip_depth += 1
        b = Breadcrumb (name, self.breadcrumb_wip_depth, self.instream.current_input_position ())
        self.breadcrumb_wip_stack.append (b)
        
    def end_breadcrumb (self, name):
        b = self.breadcrumb_wip_stack.pop ()
        self.breadcrumb_stack.append (b)
        self.breadcrumb_wip_depth -= 1

    def trace (self, s):
        print (f'\x1B[102m{self.breadcrumb_wip_stack [-1].name} depth={self.breadcrumb_wip_stack [-1].depth} pos={self.breadcrumb_wip_stack [-1].position} c="{self.instream.current_char ()}" {s}\x1B[0m')

    def call (self, f):
        f (self) # for future consideration ...
        
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
        return self.instream.endchar () == self.instream.current_char ()

    def endchar (self):
        return self.instream.endchar ()

    def peek_recursively (self, s):
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

            return False

    def pop_return_value (self):
        r = self.return_stack.pop ()
        return r

    def error (self, s):
        b = self.breadcrumb_wip_stack [-1]
        c = self.instream.current_char ()
        c = self.make_printable (c)
        s = self.make_printable (s)
        print (f'\x1B[101mReceptor error at input position {self.instream.current_input_position ()} wanted "{s}" got "{c}" (rule {b.name} beginning at {b.position})"\x1B[0m')
        sys.exit (1)

    def make_printable (self, c):
        if c == self.instream.endchar ():
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
            

