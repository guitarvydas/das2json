# Example 3
I use many different languages and can't keep their sub-syntaxes straight.

One example is loops.  Loops are especially troublesome, since they are usually little DSLs within each language.

Some languages provide `for(...;...;..)` loops that are meant to work with variables, while some other languages also provide `for ... in ...` loops that loop through data structures.

The most general loop I have seen consists of
```
loop
  ...
  exit when <condition>
  ...
end loop
```

`PREP` lets me build a tiny DSL for loops and to use that same syntax in many languages.

For purposes of example, let's make a `loop ... exit when (...) ... end loop` construct that can be used in two wildly different languages, say Python and Racket[^1].

[^1]: Racket has full-fledged macros, but, they are based on lists, not characters.  Ohm-JS macros can be used on text files.
# Requirements
The `loop ... exit when (...) ... end loop` needs to capture all loops of the given form, but must leave everything else alone.