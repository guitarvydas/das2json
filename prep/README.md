# Synopsis

Source code transpiler that works on blocks of text bracketed by REGEXPs, using PEG to transpile the blocks.

[The documentation contains videos.  For now: pull the repo, view documentation in Obsidian.]

# Usage

prep 're-begin' 're-terminate' ohm-spec glue-spec \<in \>out

prep 're-begin' 're-terminate' ohm-spec glue-spec --input=in

prep 're-begin' 're-terminate' ohm-spec glue-spec --support=fname [...]

prep 're-begin' 're-terminate' ohm-spec glue-spec --cycles=1 [...]

prep 're-begin' 're-terminate' ohm-spec glue-spec --exclusive [...]

prep 're-begin' 're-terminate' ohm-spec glue-spec --show [...]

prep 're-begin' 're-terminate' ohm-spec glue-spec --trace [...]

Expansion is recursive except when --cycles is specified. When --cycles is specified, an internal counter is initialized to 0 and counts upward +1 for every expansion cycle. Expansion terminates when (counter >= stop). 

The option `--exclusive` causes `prep` to exclude the terminator match from the code blocks

The option `--show` causes `prep` to show text blocks before and after expansion

The option `--trace` causes `prep` to show entry and exit of rules.

See `run.bash` 

# Examples

See `run.bash`.

![[doc/all-tests.mp4]]
![[doc/Test1]]
![[doc/Test2]]
![[doc/Test 3]]
![[doc/Test 4]]
![[doc/Test 5]]
![[doc/Test Forall]]
![[doc/Test Implicitforall]]

# Recursive Expansion
N.B. The expanding is done recursively.  

If you need to expand a block into another block which contains the same begin-regex, the expansion will go into an infinite loop. 

Use the --stop=1 option to prevent infinite loops.  Infinite loops occur when the expanded code looks like like text blocks, e.g. the begin-regex matches the expanded block.

If you want to run a grammar over the complete file, use a begin-regexp of `'.'`, an end-regex of `'$'` and `--stop=1`.  For example:
```
${prep} '.' '$' ???.ohm ???.glue --stop=1 <???
```

# Documentation

See [Ohm-JS documentation](https://github.com/harc/ohm) for how to write an Ohm spec.

See [Glue Tools](https://guitarvydas.github.io/2021/04/11/Glue-Tool.html) for how to write a Glue Spec.

See JavaScript Regex documentation for how to write begin/terminate REGEXs.

