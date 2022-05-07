Hamburger workbench from a draw.io diagram.

usage:
1. make
2. open file `hamburgerD0D.html` in a browswer
3. hit button "hamburger"

expected output:
```
hamburger
extra: bacon
condiments: ketchup,pickles
```

Source code `../testbench.drawio`.

See, also, `../testbenchdb.drawio`, which has various probes plugged into the message paths (they use console.log (message) to output to the browser console).


(see ../json2py/README.md)

NIY (Not Implemented Yet):
1. nets (should be included in the connections)
2. component id's that are unique

## Discussion:
1. nets (should be included in the connections)
   - nets are important for maintaining message delivery semantics on bare hardware
   - implicit synchronization in most current programming languages, e.g. Python, JS, etc. obviate the need for unique nets (since delivery semantics are guaranteed by the epicycle of using implicit synchronization)
	 - this "feature" (implicit synchronization) allows sloppy implementation of cos.js
	 - in fact, a connection *should be*: {sender, net} and net *should be*: [list of receivers]
	 - on bare metal, all receivers on one net need to be locked to prevent message interleaving
	 - in fact, the regular case is a net with exactly one receiver, in which case the locking can be "optimized away" (we need to "lock" only one receiver, which devolves to a no-op (messages cannot interleave by definition)) ; message order is no defined, the only semantic detail is that ALL receivers on a net get the same message "all at once" (without interleaving with other messages)
	 - message delivery is atomic
	 - fan-out === edge case, all receivers must be locked, before delivering message
	 - fan-out is common in hardware, less common in Software Architecture 
		 - can this semantic be preserved by wrapping multiple receivers inside a Container?
		 - a Container must process each message to completion before grabbing another message
		 - i.e. a Container must step all of its children to completion before grabbing another message
2. component id's that are unique
   - currently, the component id is always the same as the prototype name
   - unique component id's allow the same prototype to be used multiple times in one diagram
 
