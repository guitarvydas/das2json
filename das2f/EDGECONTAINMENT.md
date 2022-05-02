an edge goes from one port to another

an edge is contained in a component if (any of the below):
1. both ports are directly contained in the component (i.e. by direct children, edge from child to child)
2. an edge goes from a Container's input port to the input port of a child(s)
3. an edge goes from a Child to the output port of a Container
4. an edge goes from a Container's input directly to its own output (infrequently occurring edge case)

Care must be taken not to claim ownership of edges that are wholly-owned by children (or their children, or, ...)

- contains_edge1
- contains_edge2
- contains_edge3

There is a bug in contains_edge (probably 1).  Case 2 is not handled correctly and generates multiple facts that are the same.  I suspect that some of the other cases are not handled correctly, either.

Instead of reading relational assembly code (PROLOG), I will begin afresh by drawing diagrams of what is needed.

![Edge Containment Cases](evaluation.png)
