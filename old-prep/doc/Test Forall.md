# Synopsis
In this test case, a block starts with one-or-more (`+`) octothorpes (`#`) followed by a space follow by the keyword `forall`.

The block ends with one-or-more octothorpes.

The intent is to isolate the `## forall ...` block and to preprocess it using `forall.ohm` and `forall.glue`, leaving the rest of the text alone (not processed).
# Video
![[forall-a.mp4]]
![[forall-b.mp4]]
![[forall-a.mp4]]
![[forall-c.mp4]]
![[forall-d.mp4]]
![[forall-e.mp4]]
![[forall-f.mp4]]
![[forall-g.mp4]]
![[forall-h.mp4]]
![[forall-i.mp4]]
![[forall-j.mp4]]

# input
markdown file `testforall`
```
# layer kind
## parameters
  ID
  Direction
## imports
  fb
  shapes
  onSameDiagram
  inside
## forall ID as diagram_fact(kind,ID,"ellipse")
    Direction = cond
      diagram_fact(color, ID, "green")  input
      diagram_fact(color, ID, "yellow") output
      diagram_fact(color, ID, "red")    pervasiveinput
      diagram_fact(color, ID, "purple") pervasiveoutput
      else                              "?"
## cond design rule
  ${Direction} === "?"
  all ports must have a direction ; port ${ID} has no direction
## display
  das_fact(direction,${ID},${Direction}).

```
# Forall.ohm
```
forall {
  Main = sharp+ "forall" ident "as" predicate ws* nl* ident "=" "cond" CondClause+ CondElse

  predicate = ident "(" actuals ")" ws*
  CondClause = guard value
  CondElse = "else" value

  guard = predicate
  value = line

  actuals =   "(" actuals ")" -- parenthesized
            | notPAREN+         -- raw

  line = ~sharp notNL* nl

  notPAREN = ~"(" ~")" any

    ident = firstChar restChar*
    firstChar = "A" .. "Z" | "a" .. "z" | "_"
    restChar = "0" .. "9" | firstChar
    nl = "\n"
    sharp = "#"
    notNL = ~nl any
    ws = " " | "\t"
}
```

# Forall.glue
```
Main [@sharps kforall ident kas predicate @ws @nl ident2 keq kcond @CondClauses CondElse]
  = {{ support.pushIdent (_ident2._glue ()); }}
    [[${sharps} query\n${predicate}\n(${CondClauses} ${CondElse})\n]]

predicate [ident klpar actuals krpar @ws] = [[${ident}${klpar}${actuals}${krpar} ]]
CondClause [guard val] = [[${guard} -> ${support.getIdent()} = ${val};]]
CondElse [kelse val] = [[${support.getIdent ()} = ${val}]]

guard [predicate] = [[${predicate}]]
value [line] = [[${line}]]

actuals_parenthesized [klpar actuals krpar] = [[${klpar}${actuals}${krpar}]]
actuals_raw [@notPAREN] = [[${notPAREN}]]

line [@notNL nl] = [[${notNL}]]

notPAREN [c] = [[${c}]]

  ident [c @cs] = [[${c}${cs}]]
  firstChar [c] = [[${c}]]
  restChar [c] = [[${c}]]
  nl [c] = [[${c}]]
  sharp [c] = [[${c}]]
  notNL [c] = [[${c}]]
  ws [c] = [[${c}]]
```

# Command
```
prep '#+ forall' '#+ ' forall.ohm forall.glue --input=testforall --support=${cdir}/support.js
```
# Reading
The block is delimited by the REGEXs
- '#+ forall'
- '#+ '

In this test case, a block starts with one-or-more (`+`) octothorpes (`#`) followed by a space follow by the keyword `forall`.

The block ends with one-or-more octothorpes.

The intent is to isolate the `## forall ...` block and to preprocess it using `forall.ohm` and `forall.glue`, leaving the rest of the text alone (not processed).

The first block is
```
## forall ID as diagram_fact(kind,ID,"ellipse")
    Direction = cond
      diagram_fact(color, ID, "green")  input
      diagram_fact(color, ID, "yellow") output
      diagram_fact(color, ID, "red")    pervasiveinput
      diagram_fact(color, ID, "purple") pervasiveoutput
      else                              "?"
```
which gets formatted as a `## query` block.

`Prep` attempts to pattern-match a 2nd time, but nothing in the re-formatted block matches.

The final result is:

```
# layer kind
## parameters
 ID
 Direction
## imports
 fb
 shapes
 onSameDiagram
 inside
## query
diagram_fact(kind,ID,"ellipse") 
(diagram_fact(color, ID, "green") -> Direction = input;diagram_fact(color, ID, "yellow") -> Direction = output;diagram_fact(color, ID, "red") -> Direction = pervasiveinput;diagram_fact(color, ID, "purple") -> Direction = pervasiveoutput; Direction = "?")
## cond design rule
 ${Direction} === "?"
 all ports must have a direction ; port ${ID} has no direction
## display
 das_fact(direction,${ID},${Direction}).
 ```

 The intent is to rewrite the `## forall` block and to leave everything else alone.  The intent is to cut out and reformat a section, then hand-off the result to another matcher.

 This is a way to "stack" DSLs - to make a pipeline of matcher-reformatters (`prep`) each of which modifies the input in some small way, and, then hands-off the reformatted result.

 [Aside: This test case was created during the development of the `das2f` tool.  The end of the pipeline is a tool called `querydisplay3` that does not understand `forall` blocks.  The intent was to write the Software Architecture of parts of `das2f` in markdown format, then to preprocess the parts until they could be translated into executable code.]

 Note, also, that the command line specifies a support file `support.js` that contains functions called by `forall.glue`.

 Note that every `forall` block will be matched-and-formatted, even if there is more than one `forall` block in the text.  This repetitive matching-replacement is not shown in this simple example.