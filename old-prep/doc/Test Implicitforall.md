# Synopsis
This test case shows how we wrote a simple wrapper which works on a line-by-line basis.

The meat of the grammar is the rule `main` which has 3 interesting parts
1. the header `sharp+ ws+ "query"
2. the (implicit) forall clause `match`, and,
3. the rest of the clauses, each of which need to be satisfied.

What we wanted was something like
```
if (2.) then
  3....
else 
  error messages
end if
```

The syntax of PROLOG is well-suited to pattern matching, but, PROLOG does not raise an error if any of the clauses in (3) fail (PROLOG fails the match silently).

To get the desired effect, we wanted to use PROLOG pattern-matching syntax, but, needed to wrap each then-clause (3) with extra details.

In this case, the match is easy and the needed extra detail is wrapped by the .glue file.

# input
markdown file `testimplicitforall`
```
# layer kind
## parameters
  X
  Kind
## imports
  shapes
  onSameDiagram
  inside
  names
  ports
  contains
## query
diagram_fact(cell,X,_) 
(diagram_fact(kind,X,"ellipse")  -> Kind = "ellipse";diagram_fact(edge,X,1)  -> Kind = "edge";diagram_fact(root,X,1)  -> Kind = "root"; Kind = "rectangle")
## display
  das_fact(kind,${X},${Kind}).


```

![[implicit-1.mp4]]
# Implicitforall.ohm
The rule `main` is the only - Architecturally - significant line.  The rest of the lines in the grammar are for support and non-Architectural, lower-level details.

The rules in this test were written as lexical rules (lower-case first letter in the names).

It might make an interesting exercise-for-the-reader to convert the top-level rules into syntactic form while preserving the line-by-line matching.

The rules remain in lexical form on the YAGNI[^1] principle.

[^1]: You Ain't Gonna Need It.  The rules - as they stand - are sufficient to implement our implicitforall grammar.  The grammar is fairly simple as it stands.  Maybe, after months of more practice, the rules would be written differently (syntactically) from the outset.

```
implicitforall {
  main = sharp+ ws+ "query" ws* nl+ match ensure+

  match = line
  ensure = line

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

![[implicit-b.mp4]]

![[implicit-c.mp4]]

# Implicitforall.glue
```
main [ @sharps @ws kquery @ws2 @nl Match @Ensures] = [[${sharps}${ws}~${ws2}${Match}${Ensures}]]

match [line] = [[${line}]]
ensure [line] = [[(${line.trim ()}->true ; format(user_error,"querythen failed /${line.trim ()}/~n",[]),abort),\n]]

line [@notNL nl] = [[${notNL}${nl}]]

notPAREN [c] = [[${c}]]

ident [firstChar @restChar] = [[${firstChar}${restChar}]]
firstChar [c] = [[${c}]]
restChar [c] = [[${c}]]
nl  [c] = [[${c}]]
sharp  [c] = [[${c}]]
notNL  [c] = [[${c}]]
ws  [c] = [[${c}]]

```

![[implicit-e.mp4]]

![[implicit-d.mp4]]

# Command
```
prep '#+ query' '#+ ' implicitforall.ohm implicitforall.glue --input=testimplicitforall --support=${cdir}/support.js >temp
```


![[implicit-f.mp4]]
(When I say "numbers" in the above video, I mean "octothorpes"...)

# Reading
The pattern-matcher matches one PROLOG clause, then more PROLOG clauses.

The first clause is taken to be the "forall" clause.  The rest of the clauses are wrapped in detailed syntax that causes non-silent failures, achieving the desired result (in layers).

Note that the rules `match` and `ensure` are identical at the matching level.  The differentiation comes in how the clauses are re-formatted.

In general, programmers are taught the DRY - Don't Repeat Yourself - principle.  In this case, though, we *do* want to repeat ourselves, and, in the process, remember which clauses are the if-clauses and which are the then-clauses.

The grammar makes it easy for us to do this while not repeating the actual operational code.  We simply let `match` and `ensure` call the same sub-rule `line`.  We do the matching work in `line`.  The matching operations appear in only one place - `line` - yet, we can differentiate the "history" of the matching operation in the `.glue` file using the two uber-rules `match` and `ensure`.

[Note to future tool implementors: it would be "nice" to write the grammar, then add refinements only in the .glue file without modifying the original grammar.  We would want to write the grammar so that the grammar doesn't need to know that there is a difference between the kinds of lines, e.g.
- ` main = sharp+ ws+ "query" ws* nl+ line line+
- then, in the .glue file, we might say something like
	-  `main = sharp+ ws+ "query" ws* nl+ line#1 line#2+``
	- where `line#1 = match` and `line#2 = ensure`]
[Note that this *can* already be done in the semantics code using JavaScript state variables, but it would be nicer if the grammar could help with parsing this kind of state.  Another option would be that of allowing grammar stacks - the original grammar produces a parse, then a downstream grammar re-parses the parse at a finer level. (Q: can this already be done with the `prep` tool as things stand?)]

# Wart
The current version of `run.bash` contains a final `sed` line.

This is a left-over from an early version of the `prep` tool.  We wanted a `stop=1` option and had to fake it by transpiling "query" into "~".  Later, the `stop=1` option was added to `prep` which would have obviated the need for this fakery.

Exercise to the reader: rewrite the `implicitfoall` test of `run.bash` to use the `stop=1` option and to remove the final `sed` line (hint: this, also, requires a minor change to the first line in `implicitforall.glue`.)