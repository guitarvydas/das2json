# Syntax is Cheap
If you are allowed to use cheap syntax, the way you think about programming changes.

New workflow:
- use macros + toolbox language
- develop multiple notations for a single solution
- base notation on what is *necessary*, not what is *available* in GPLs or DSLs

## Generalized Macro Expansion
Character-based macros
	- not list-only macros
	- PEG (=> Ohm-JS)

Lisp provides powerful macros, but using a list-only syntax.

PEG provides lisp-like power using a character-based syntax.

PEG libraries are available for many languages.

Ohm is better than PEG because Ohm separates grammar from semantics.
## Names are Cheap => Syntax is Cheap
FP teaches us that names are superfluous.

All syntax is superfluous - not just names.

PE (Projectional Editing) strips syntax, leaving only the meat.  PE allows multiple syntaxes for the same meat.
## Learn From Lisp (Racket) Macros
Lisp taught us what makes a good macro DSL and how to expand macros.
- recursive expansion
- tag syntax objects with File and Line numbers (etc.) (Scheme, Racket)
# Toolbox Language
- Machine Readable (reduced emphasis on human-readability)
- kitchen sink - supports any kind of paradigm
- regular syntax - normalized syntax 
	- easy to read (by machine)
	- easy to write (by machine)


## Original Toolbox
Assembler
- machine readable (after conversion to binary)
- kitchen sink
- normalized syntax - triples.  e.g. "MOV R0,R1" is a triple

Static, compilable and typefulness are optimizations.

All languages can be *dynamic*, but only some can be compiled.

Compilable (static, typeful) languages are for Production Engineering, not Design.

## New Toolbox
Lisp
- machine readable
- kitchen sink
	- every paradigm is possible
	- in fact many languages (e.g. Haskell) were first implemented in Lisp
- normalized syntax - Lisp is an *expression language* (every clause results in a value)
- dynamic first
- REPL
- debugging (debuggers well developed over decades)

## Wannabes
### Javascript
- kitchen sink
- supports first-class functions
- easy object creation ("{...}")
- too much syntax
- not an expression language ; needs `return` statements
- dynamic
- protypal inheritance (more general (toolbox-y) than class-based inheritance)
## Python
- too much syntax 
- indentation-based syntax is less machine-readable/writable
- dynamic (good for toolbox-iness)
- supports first-class functions
## Relational Programming
- restricted to a single paradigm (Relational)
- wonderful for pattern-matching higher-level concepts (aka *inference*)
- syntax developed for inferencing
- can support and query triples
- the underlying *mechanism* for relational programming is *exhaustive search* (PROLOG and miniKanren achieve exhaustive search in different ways) (see below)
## OOP
- restricted to a single paradigm (OO)
- the underlying *mechanism* for "message sending" is usually implemented as CALL-RETURN (produces implicit dependencies)
## Haskell
- restricted to a single paradigm (functions, synchronous-only)
- too much syntax
## Markdown
- line oriented
- editors can easily elide layers
- originally meant for prose but can be applied to programs
## Racket
- lisp, but geared towards compilability (==> trade-offs, language usability degradation)
- accidental complexity whack-a-mole, e.g. closures

# Important Paradigms
[Paradigms]()
