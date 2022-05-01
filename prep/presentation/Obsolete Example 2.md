# Obsolete Example 2
Let's rewrite the grammar to use 2 kinds of tokens:
1. identifiers
2. separators (any character the is not allowed in identifiers, e.g. parentheses, etc.)

## Grammar
```
Scn2 {
  Main = octothorpe+ Statement+
  octothorpe = "#"
  Statement 
    = VarStatement     -- var
    | DisplayStatement -- display
    | ident            -- ident
    | separator        -- other

  VarStatement = "var" ident
  DisplayStatement = "display" Comma_ident* ident

  Comma_ident = ident ","

  ident = idFirst idRest*
  idFirst = "A" .. "Z" | "a" .. "z" | "_"
  idRest = "0" .. "9" | idFirst

  separator = ~idFirst ~octothorpe any
}
```
This grammar is at least as simple as the previous grammar, but it does more.

In this example, we break out "var" statements and "display" statements.

This - simplistic - example shows how we might modify the output code - we will map `display` statements into debug printing function...

## Identity Format
```
Main [@octothorpe @Statement] = [[${octothorpe}${Statement}]]
octothorpe [c] = [[${c}]]
Statement_var [s] = [[${s}]]
Statement_ident [s] = [[${s}]]
Statement_display [s] = [[${s}]]
Statement_other [s] = [[${s}]]

VarStatement [kvar ident] = [[${kvar}${ident}]]
DisplayStatement [kdisplay @Comma_ident ident] = [[${kdisplay}${Comma_ident}${ident}]]

Comma_ident [ident kcomma] = [[${ident}${kcomma}]]

ident [c @cs] = [[${c}${cs}]]
idFirst [c] = [[${c}]]
idRest [c] = [[${c}]]

separator [c] = [[${c}]]
```
### Identity Run
```
$ ../../prep '#+ ' '#+ |$' scn2.ohm scn2.glue <test2.scn
#layer0varx#layer1varyy=xprint(x)displaya,b
$
```
Note that all of the spaces and newlines have disappeared in this identity run.

This is due to the fact that we are using Ohm-JS *syntactic* rules.

This is OK, since we don't want to keep the identity formatter (creating an identity format is a sanity check - it alerts us of typos, etc.  We *could* fix up the output to insert spaces and newlines, but we don't need to waste our time doing this).
