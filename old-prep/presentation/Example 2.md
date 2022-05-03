Let's write a grammar to do more interesting macro pattern-matching.

# Grammar
```
G {
  start = findMacros*
  findMacros =
    | applySyntactic<Macro> -- macro
    | ident                 -- ident               
    | any                   -- any

  Macro = 
    | tIdentMacro "(" ListOf<ident, ","> ")" -- ident
    | tAnythingMacro "(" anystuff* ")"       -- anything

  anystuff =
    | "(" anystuff* ")" -- nested
    | ~"(" ~")" any     -- flat


  
  ident = identFirst identRest*
  identFirst = "A" .. "Z" | "a" .. "z" | "_" 
  identRest = "0" .. "9" | identFirst

  tAnythingMacro = "m" ~identRest
  tIdentMacro = "i" ~identRest

}

```
The above grammar recognizes 2 kinds of macros:
1. macros that expect `ident`s as parameters (`m()`)
2. macros that allow anything inside the parameter list (`i()`).

Kind 2 macros (match anything inside parameter list) use PEG's ability to pattern-match for matching parentheses (see the rule `anystuff`).

Kind 1 macros will pattern-match only identifiers (as defined by the rule `ident`) separated by commas, and, will balk at anything else.

We used `m` and `i` as macro names in this example, but, any names could be used.
# Test Code
```
f
zi(d,e)
i(p,q)
m(r,s)
g
i
(a,
b)
h
```
# Identity Grammar
```
start [@findMacros] = [[${findMacros}]]

findMacros_macro [macro] = [[${macro}]]
findMacros_ident [ident] = [[${ident}]]
findMacros_any   [any]   = [[${any}]]

Macro_ident [name klp CommaSeparatedIdents krp] = [[${name}${klp}${CommaSeparatedIdents}${krp}]]
Macro_anything [name klp @anystuff krp] = [[${name}${klp}${anystuff}${krp}]]

anystuff_nested [klp @anystuff krp] = [[${klp}${anystuff}${krp}]]
anystuff_flat [any] = [[${any}]]

ident [identFirst @identRest] = [[${identFirst}${identRest}]]
identFirst [c] = [[${c}]]
identRest [c] = [[${c}]]

tAnythingMacro [name] = [[${name}]]
tIdentMacro [name] = [[${name}]]

NonemptyListOf [ident @commas @idents] = [[${ident}${commas}${idents}]]```
```
# Run - Identity
```
      

$ ./run.bash 

f

zi(d,e)i(p,q)m(r,s)m(+-*/((()))%(())$)gi(a,b)h

  

$
```
This identity run mushes together anything that is recognized as a macro, but, that's OK.  

Macros use Ohm-JS "syntactic" rules, which skip whitespace, and, leave out whitespace in the output.

This identity run is just a sanity check, so we don't care what it looks like, as long as it seems to resemble the input.

We'll worry about formatting in the non-identity version - the output we care about.

# Format
For purposes of showing how this works, we'll do something useless in the format.

We'll change all `i(...)` macros into `\n--ident-macro <<...>> --` and all `m(...)` macros into `\n--anything-macro <<...>>--`.

The changes are almost trivial, affecting only the Macro_ident and Macro_anything rules ...
```
start [@findMacros] = [[${findMacros}]]

findMacros_macro [macro] = [[${macro}]]
findMacros_ident [ident] = [[${ident}]]
findMacros_any   [any]   = [[${any}]]

Macro_ident [name klp CommaSeparatedIdents krp] = [[\n--ident-macro <<${CommaSeparatedIdents}>>--]]
Macro_anything [name klp @anystuff krp] = [[\n--anything-macro <<${anystuff}>>--]]

anystuff_nested [klp @anystuff krp] = [[${klp}${anystuff}${krp}]]
anystuff_flat [any] = [[${any}]]

ident [identFirst @identRest] = [[${identFirst}${identRest}]]
identFirst [c] = [[${c}]]
identRest [c] = [[${c}]]

tAnythingMacro [name] = [[${name}]]
tIdentMacro [name] = [[${name}]]

NonemptyListOf [ident @commas @idents] = [[${ident}${commas}${idents}]]```
and the run becomes:
```
and the run is:
```
$ ./run.bash
f
zi(d,e)
--ident-macro <<p,q>>--
--anything-macro <<r,s>>--
--anything-macro <<+-*/((()))%(())$>>--g
--ident-macro <<a,b>>--h

$ 
```
# Macro Suggestions
It is possible to use macros to write programs that appear to call functions.

If the functions are macros, they can be expanded into "more efficient" code for particular programming languages.

For example, in [langjam 0002](https://github.com/guitarvydas/jam0002/tree/main/guitarvydas), I built a dataless version of C (called `cmm` - C minus minus).  I used macros that expanded into C statements.