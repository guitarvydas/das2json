### Example
Grammar that pattern-matches `.drawio` files.
#### Text
```
AppDiagramsEncodedNet{
TabbedDiagrams = Header Diagram+ Trailer
Header = "<" "mxfile" encodedChar+
Trailer = "</mxfile>"
Diagram = "<diagram" Attribute* ">" encodedChar+ "</diagram>"
Attribute = alnum+ "=" attributeValue
string= "\"" notDQ* "\""
notDQ = ~"\"" any
encodedChar = ~"<" any		   
attributeValue = number | string
number = digit+
}
```
#### Diagram
![[drawio-grammar.svg]]
## Glue Formatter
### Example
Formatter that calls `support.decodeMxDiagram ()` for matched `Diagram` block
#### Text
TabbedDiagrams [h @d t] = [[${d}]]
Header [k k2 @ec] = [[${k}${k2}${ec}]]
Trailer [k] = [[${k}]]
Diagram [k @a k2 @ec k3] = [[${k}${a}${k2}\n${support.decodeMxDiagram(ec)}\n${k3}\n]]
Attribute [@an k s] = [[\ ${an}${k}${s}]]
string [q1 @cs q2] = [[${q1}${cs}${q2}]]
notDQ [c] = [[${c}]]
encodedChar [c] = [[${c}]]
attributeValue[x] = [[${x}]]
number [n] = [[${n}]]

Rules:
1. Each rule corresponds to grammar rule (same name).
2. Parameter list contains 2 kinds of variables
	a. regular (flat) variables
	b. variables prefixed by `@` denoting \*/+/? in corresponding grammar rule.

Glue walks parse tree *down* then back *up*.  

On way back up, it constructs a single string using JS *template string* syntax enclosed in double-brackets `[[...]]`.

Each Glue rule returns one string.

[More details in Glue manual].
# Example
## DSL 1
(I use the term *SCN* instead of *DSL* ; *SCN* means "Solution Centric Notation")
### Line-oriented syntax
```
# layer 0
  var x
  x = 7
# layer 2
  var y
  y = x
  print 7
```
### Text Blocks
`Prep` will find 2 text blocks in the above.

The first block will be
```
# layer 0
  var x
  x = 7
```

and, the second block will be
```
# layer 2
  var y
  y = x
  print 7
```
### Desired Python:
```
#!/usr/bin/env python
x = 7
y = x
print (y)
```
### Step 1 - Develop and Debug Grammar
`scn1.ohm`

![[grammar scn1.ohm Screen Shot 2022-01-07 at 3.20.47 PM.png]]

![[layer 0 Screen Shot 2022-01-07 at 3.20.53 PM.png]]

![[layer 1 Screen Shot 2022-01-07 at 3.20.59 PM.png]]
#### GOTCHA
This grammar requires that the last line be terminated with a newline.

We will avoid fixing this problem to keep the example simple.

### Step 2 - Develop Identity Grammar
`Test1.glue` contains one format rule for each grammar rule.
#### Convert Main Rule
```
  Main = octothorpe+ commentToNL statement+
```
Parameters
```
  Main [@octothorpe commentToNL @statement] = ...
```
Formatting
```
  ... [[${octothorpe}${commentToNL}${statement}]]
```
Completed Main Rule:
```
  Main [@octothorpe commentToNL @statement]
    = [[${octothorpe}${commentToNL}${statement}]]
```
#### Constant
```
  octothorpe [kOctothorpe] = [[${kOctothorpe}]]
```
(convention: use "k" to signify a constant string (not mandatory, any name will do))
#### Single Character Match
```
  nl [kNL] = [[${kNL}]]
```
(aside: it might be "more efficient" to use Ohm-JS built-in fields, but, leave optimization for later (if at all))
#### Not
Not (`~`) creates no parse nodes and does not appear in `.glue` spec.
```
  nonNLchar [notNL any] = [[${any}]]
```
#### Completed Identity Format
```
  Main [@octothorpe commentToNL @statement]
    = [[${octothorpe}${commentToNL}${statement}]]
  octothorpe [kOctothorpe] = [[${kOctothorpe}]]
  commentToNL [line] = [[${line}]]
  statement  [line] = [[${line}]]

  line [@nonNLchar nl] = [[${nonNLchar}${nl}]]
  nl [kNL] = [[${kNL}]]
  nonNLchar [any] = [[${any}]]

```
#### RY (Repeat Yourself)
Contrary to unspoken rule *DRY* (Don't Repeat Yourself), it is desirable to let the parser tell you *where* a match was found.  Rules `commentToNL` and `statement`, both, call rule `line`.  In one case, we want to throw the line away and in the other case we want to output it.
#### Test1.scn
```
# layer 0
  var x
# layer 1
  var y
  y = x
```
#### Run
```
$ ../../prep '#+ ' '#+ |$' scn1.ohm scn1.glue <test1.scn
#layer 0
var x
#layer 1
var y
y = x
```
- Begin REGEX is '#+ ' (1 or more octothorpes followed by space).
- End REGEX is '#+ |$' (next octothorpes or EOF).
- Grammar: `scn1.ohm`
- Format spec: `scn1.glue`
- Input: `test1.scn`

Output <- Input (modulo spaces)
### Change Identity Spec to Suit the Problem
This example is very simplistic for expository purposes. 

In fact this can call be done with REGEXs. 

It is hoped that the reader can infer more interesting use-cases for `prep`.

Ohm-JS (PEG) is "better" than REGEX[^1].

[^1]: Ohm-JS allows calling rules.  REGEX does not.  REGEX specs are usually shorter (1-line) than Ohm-JS specs.  The rule-calling ability of Ohm-JS allows matching *structured* text (see next example) which cannot be done with REGEX.
#### Desired
- delete all #... lines (layer comments)
- delete `var` prefixes
- leave the rest of the code alone.

(Again, this is a trivial example.  Later examples will show more interesting use-cases.)

#### Deleting comment lines
Format rules `commentToEOL` and `octothorpe` are modified to return the empty string.
```
  ...
  octothorpe [kOctothorpe] = [[]]
  commentToNL [line] = [[]]
  ...
```
#### Intermediate Result
```
$ ../../prep '#+ ' '#+ |$' scn1.ohm scn1.glue <test1.scn
var x
var y
y = x
print (x)
```
#### Deleting `var` Keyword
This is most easily done by modifying the grammar and the format specs, to match for a "var ..." statement.
##### New Grammar
```
Scn1 {
  Main = octothorpe+ commentToNL Statement+
  octothorpe = "#"
  commentToNL = line
  Statement 
    = VarStatement
    | line

  VarStatement = "var" ident #(nl)

  ident = idFirst idRest*
  idFirst = "A" .. "Z" | "a" .. "z" | "_"
  idRest = "0" .. "9" | idFirst
  line = nonNLchar* nl
  nl = "\n"
  nonNLchar = ~nl any
}
```
`#(nl)` is syntax that tells Ohm-JS to stop skipping spaces around the rule `nl`. 
##### New Format Spec
```
  Main [@octothorpe commentToNL @statement]
    = [[${octothorpe}${commentToNL}${statement}]]
  octothorpe [kOctothorpe] = [[]]
  commentToNL [line] = [[]]
  Statement  [line] = [[${line}]]

  VarStatement [kvar ident nl] = [[]]

  ident [identFirst @identRest] = [[${identFirst}${identRest}]]
  idFirst [c] = [[${c}]]
  idRest [c] = [[${c}]]

  line [@nonNLchar nl] = [[${nonNLchar}${nl}]]
  nl [kNL] = [[${kNL}]]
  nonNLchar [any] = [[${any}]]
```
##### New Run
```
$ ../../prep '#+ ' '#+ |$' scn1.ohm scn1.glue <test1.scn
y = x
print (x)
$
```
