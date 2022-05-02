DaS to Factbase.

DaS is Diagrams to Syntax.

Factbase is currently implemented as a file full of PROLOG facts. (It could be implemented using maps or something else, or miniKanren, or, ...).  The salient feature is that we store atomic facts in a factbase, then use code snippets to walk the factbase like barnacles. The code creates new facts (molecules created from atoms) and shoves them back into the factbase (pruning facts from a factbase is only an optimization, not a requirement).

This was originally written using a bunch of small queries, written as .md files then converted into PROLOG->JavaScript pipelines (`layer_*.md` -> `layer*query.bash`).

I'm iterating the logic (AKA debugging :-).  Currently, there is something wrong with the way that edge containment is detected.  See my working notes in `EDGECONTAINMENT.md`.

[It is *never* possible to figure it all out only by "thinking about it" (that is called "Waterfall development"), although some people can go further than I could. At some point, iteration is necessary. If only, to step upwards and to create a better notation for the problem, then solving the problem at a higher level and solving even more interesting problems that become apparent when the lower levels are elided...]
