# steps
0. [done] use in.txt, create forall.txt
1. [done] create forall.ohm
2. [done] create forall.glue
3. [done] test conversion using "pfr forall.txt forall.ohm forall.glue support.js"
4. [done] clone parse.js into pre.js
5. [done] test pre.js "pre forall.ohm forall.glue <in.txt"

# pre2
## trigger expansion with a regexp
	the trigger remains as part of the chunk handed to the expander
	
the code in note2.md use two expanders - "forall" and "design rule"
the goal is to pipeline the two expanders, then hand the result to querdisplay2


