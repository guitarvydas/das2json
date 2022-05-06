Unfinished

(see ../json2py/README.md)

- wip: rewrite `djson.fmt` for JS in ../json2js

- missing:
  - detail in phraseparser for Ohm-js
  - testbench.js route: route
	- makeNets details (NIY)
	- `var conn7 = {sender:{name: "Order Taker", etag: "food order"}, net: "NIY", receivers:  [{name: "Test Bench", etag: "food order"}] };` should be name: "_me" instead of "Test Bench"
	- `var conn9 = {sender:{name: "Order Taker", etag: "phrase"}, net: "NIY", receivers:  [{name: "Phrase Parser", etag: "phrase"}] };` name: "_me" instead of "Order Taker"
	- 3rd connection in OT from _me.phrase to ...

<!-- ## Theory phrase parser should not generate an implementation (only a signature) -->
<!-- - test: manually remove implementation, run workbench, but don't run make -->
<!-- - conclusion:  -->
<!--   - works better (thru probe 4) -->
<!--   - PhraseParser spelled without _, instead of Phrase_Parser -->

<!-- ## Theory - output on TB will be generated -->
<!-- - test: install output port on TB, manually remove parser implementation -->
<!-- - conclusion: -->
<!--   - created output -->
  
<!-- ## Theory phrase parser should not generate an implementation (only a signature) -->
<!-- - theory: parser being misparsed as Leaf -->
<!-- - test: make, then examine testbenchdb.js and see how the implementation is instantiated -->
<!-- - conclusion: parser is generated as Leaf -->

<!-- - test: examine testbenchdb.json and see if parser has a body -->

<!-- - test: create testbench6.json containing only parser, run make, examine -->

## Theory - probe can be duplicated
- test: change all probe[1-4] to be the same
- conclusion:
  -
  



 
