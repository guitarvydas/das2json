# Synopsis

`PREP` is a command-line tool that applies macro expansion to blocks of text delineated by REGEXs.

Macros are written in Ohm-JS, a variant of PEG (more powerful than REGEX).

Expansion is recursive, enabling expansion pipelines.

# Other Technologies Used in Prep

`Prep` uses Ohm-JS and Glue[^1].

[^1]:`Glue` is a text-to-text formatter add-on to Ohm-JS, written in Ohm-JS.

`Prep` applies macro expansion recursively as is done in Common Lisp and Racket macros.
# Prep Syntax
[[PREP Syntax - Command Line]]
[[PREP Syntax - REGEX]]
[[PREP Syntax - Pattern Matching Spec - Grammar]]

# Examples

## Example 1 - Basics
Very simple example to show the basics:
[[Example 1]]

## Example 2 - Macros
Macros (textual):
[[Example 2]]
[[Obsolete Example 2]]

# Status
- experimental
- WIP
- based on earlier work, e.g. prep <- pre <- pfr <- glue
- being used in d2py (diagrams to Python)
	- d2py uses d2f (diagrams to factbase) which uses `prep`
	- d2py uses d2j (diagrams to JSON)


# Appendix - Github
[prep github](https://github.com/guitarvydas/prep)
# Appendix - Glue
[GLUE Presentation](https://guitarvydas.github.io/2021/04/11/Glue-Tool.html)
[glue manual](https://guitarvydas.github.io/2021/03/24/Glue-Manual.html)
[ABC Example](https://guitarvydas.github.io/2021/09/15/ABC-Glue.html)

# Appendix POCs
## Appendix D2PY
[WIP Diagrams-to-Python](https://github.com/guitarvydas/d2py)
[POC App/shu-das2py](https://github.com/guitarvydas/app/tree/master/shu-das2py)
## Appendix D2J
[POC Diagrams to JSON](https://github.com/guitarvydas/app/tree/master/das2j)
## SHU das2bash
(SHU == Shu portion of ShuHaRi)
[POC shu-das2bash](https://github.com/guitarvydas/app/tree/master/shu-das2bash)
## SHU das2cl
[POC shu-das2cl](https://github.com/guitarvydas/app/tree/master/shu-das2cl)

# Appendix - Syntax is Cheap
WIP [[Syntax is Cheap]]
