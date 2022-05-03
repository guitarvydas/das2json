# Synopsis

Source code transpiler that works on blocks of text bracketed by REGEXPs, using PEG to transpile the blocks.

# Usage

pre 're-begin' 're-terminate' ohm-spec glue-spec <in >out

pre 're-begin' 're-terminate' ohm-spec glue-spec --input=in

pre 're-begin' 're-terminate' ohm-spec glue-spec --support=fname [...]

pre 're-begin' 're-terminate' ohm-spec glue-spec --stop=1 [...]

pre 're-begin' 're-terminate' ohm-spec glue-spec --grammarname=<name of grammar> [...]

Expansion is recursive except when --stop is specified. When --stop is specified, an internal counter is initialized to 0 and counts upward +1 for every expansion cycle. Expansion terminates when (counter >= stop). 

When using multiple grammars and inheritance, use --grammarname= to specify the name of the grammar to be used.

See `run.bash` 

# Examples

See `run.bash`

# test1:
- input=ac
- blockbegin=a
- blockend=c
- block="a"
- replacement=*   // a is replaced by *
- result=*c

# Recursive Expansion
N.B. The expanding is done recursively.  

If you need to expand a block into another block which contains the same begin-regex, the expansion will go into an infinite loop. 

An example of how to handle this case is in test6, e.g. expand `query` into `~`, then later, used `sed` to put the `query` back, noting that `~` will not trigger a re-expansion, i.e. `## query` is mapped to `## ~` then later re-mapped to `## query`.

# Documentation

See [Ohm-JS documentation](https://github.com/harc/ohm) for how to write an Ohm spec.

See [Glue Tools](https://guitarvydas.github.io/2021/04/11/Glue-Tool.html) for how to write a Glue Spec.

See JavaScript Regex documentation for how to write begin/terminated REGEXs.

