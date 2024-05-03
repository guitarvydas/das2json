_in = None
EOF = chr (0)


def das2json ():
    global _in
    Spaces () # Spaces "<" Stuff
    _in.need ("<")
    _in.echo ()
    Attributes ()
    if _in.peek (">"):
        _in.accept () # ">" ? Content "</" Stuff ">"
        _in.echo ()
        Content ()
        _in.need ("</")
        _in.echo ()
        Stuff ()
        _in.need (">")
        _in.echo ()
    elif _in.peek ("/>"):
        _in.accept () # "/>" ?
        _in.echo ()
    else:
        _in.syntax_error ()

def Content ():
  while True:
      Spaces ()
      if _in.peek ("</"):
          break
      elif _in.peek ("<"):
          das2json ()
      else:
          Stuff ()
          
            
def Attributes ():
    while True:
        if _in.peek ("style="):
            _in.accept ()
            String ()
            _in.clear_collector ()
        elif _in.peek (">"):
            break
        elif _in.peek ("/>"):
            break
        elif _in.peek (EOF):
            break
        else:
            _in.accept ()
            _in.echo ()

def Stuff ():
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
            _in.accept ()
            _in.echo ()

def Spaces ():
    global EOF
    while True:
        if _in.peek (" "):
            _in.accept ()
            _in.echo ()
        elif _in.peek ("\t"):
            _in.accept ()
            _in.echo ()
        elif _in.peek ("\n"):
            _in.accept ()
            _in.echo ()
        elif _in.peek (EOF):
            break
        else:
            break
        
def String ():
    _in.need ('"')
    _in.collect ()
    NotDquotes ()
    _in.need ('"')
    _in.collect ()

def NotDquotes ():
    while True:
        if _in.peek ('"'):
            break
        else:
            _in.accept ()
            _in.collect ()


#####
import sys

class Token:
    def __init__ (self, c='', position=0):
        self.c = c
        self.position = position
    
class InputStream:
    def __init__ (self):
        self.stdin_position = 0
        self.most_recently_accepted = None
        self.afresh ()
        self.collector = ""
        
    def afresh (self):
        self.cache = []
        self.cache_index = -1
        self.getc ()

    def rewind (self):
        self.cache_index = 0

    def getc (self):
        if len (self.cache) == 0:
            c = sys.stdin.read (1)
            if 1 > len (c):
                c = EOF
            self.stdin_position += 1
            self.cache = [Token (c=c, position=self.stdin_position)]
            self.cache_index = 0
        elif len (self.cache) == (self.cache_index + 1):
            c = sys.stdin.read (1)
            self.stdin_position += 1
            self.cache.append (Token (c=c, position=self.stdin_position))
            self.cache_index += 1
        else:
            self.cache_index += 1

    def current_token (self):
        return self.cache [self.cache_index]

    def echo (self) :
        for tok in self.most_recently_accepted:
            print (f'{tok.c}', end='')
            
    def collect (self) :
        for tok in self.most_recently_accepted:
            self.collector = self.collector + tok.c
            
    def echo_collection (self) :
        print (f'{self.collector}', end='')
        self.clear_collector ()

    def clear_collector (self):
        self.collector = ""
            
    def accept (self):
        # do something with cached tokens, then start afresh
        # ...
        self.most_recently_accepted = self.cache
        if EOF == self.current_token ().c:
            print ("\x1B[101m*** error: at EOF\x1B[0m")
            sys.exit (1)
        # ... start afresh
        self.afresh ()

    def syntax_error (self,s):
        print (f'\x1B[101m*** syntax error wanted "{s}", but, got {self.ftok (self.current_token ())}\x1B[0m')
        sys.exit (1)

    def need (self, s):
        if self.peek (s):
            self.accept ()
            return True
        else:
            self.syntax_error (s)
            return False
        
    def peek (self, s):
        if self.peek_rec (s):
            self.rewind ()
            return True
        else:
            self.rewind ()
            return False
        
    def peek_rec (self, s):
        global EOF
        if 0 == len (s):
            if EOF == self.current_token ().c:
                return True
            else:
                return False
        elif s [0] == self.current_token ().c:
            if 1 == len (s):
                return True
            else:
                self.getc ()
                return self.peek_rec (s [1:])
        else:
            return False

    def ftok (self, tok):
        global EOF
        c = tok.c
        if c == ' ':
            c = "' '"
            h = hex (ord (tok.c))
        elif c == '\t':
            c = "<unprintable>"
            h = hex (ord (tok.c))
        elif c == '\n':
            c = "<unprintable>"
            h = hex (ord (tok.c))
        elif c == EOF:
            c = "*EOF*"
            h = "?"
        elif c == "":
            c = "<empty>"
            h = "?"
        else:
            h = hex (ord (tok.c))
        return f'{c} {h} at {tok.position}'

def _begin ():
    global _in
    _in = InputStream ()
    
_begin ()
das2json ()
