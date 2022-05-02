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

desired algorithm:
for every item with kind=edge => Edge
  Edge.source => SourceName
  Edge.target => TargetName
  normalizeName (SourceName) => Source  ## normalize name in case there are synonyms
  normalizeName (TargetName) => Target  ## ''
  case
	child-to-child-edge: Parent ≣ (either Source or Target).parent
	child-to-parent-edge: Parent ≣ Target.parent
	parent-to-child-edge: Parent ≣ Target.parent
    self-to-self-edge: Parent ≣ self
	else fail-match
  end case

normalizeName(X) ≣ if X has a synonym, then the normalizedName is the longer name, else the normalizedName is X

edge (E) {
  child-to-child-edge (normalizedName (E.source) => X, normalizedName (E.target) => Y) ≣ X.parent = Y.parent
  child-to-parent-edge (normalizedName (E.source) => Child, normalizedName (E.target) => Parent) ≣ Child.parent = Parent
  parent-to-child-edge (normalizedName (E.source) => Parent, normalizedName (E.target) => Child) ≣ Child.parent = Parent
  self-to-self-edge (normalizedName (E.source) => Self, normalizedName (E.target) => Self) ≣ success.
}

---
contains_edge1:

## query
    das_fact(kind,Edge,edge)
    das_fact(kind,Parent,rectangle)
    diagram_fact(source,Edge,SourceLongID)
	diagram_fact(synonym,Source,SourceLongID)
	das_fact(direct_contains,Rect,Source)
	das_fact(direct_contains,Parent,Rect)
## display
das_fact(direct_contains,${Parent},${Edge}).

reading:
for every item with kind=edge => "Edge"
  Parent == kind(
---
contains_edge2:

## query
    das_fact(kind,Edge,edge)
    diagram_fact(source,Edge,SourceLongID)
	diagram_fact(synonym,Source,SourceLongID)
    diagram_fact(target,Edge,TargetLongID)
	diagram_fact(synonym,Target,TargetLongID)
	(das_fact(direction,Source,input) ; das_fact(direction,Source,pervasiveinput))
	(das_fact(direction,Target,input) ; das_fact(direction,Target,pervasiveinput))
    das_fact(kind,Parent,rectangle)
	das_fact(direct_contains,Parent,Source)
## display
das_fact(direct_contains,${Parent},${Edge}).
  
---
contains_edge3:
## query
    das_fact(kind,Edge,edge)
    diagram_fact(source,Edge,SourceLongID)
	diagram_fact(synonym,Source,SourceLongID)
    diagram_fact(target,Edge,TargetLongID)
	diagram_fact(synonym,Target,TargetLongID)
	(das_fact(direction,Source,output) ; das_fact(direction,Source,pervasiveoutput))
	(das_fact(direction,Target,output) ; das_fact(direction,Target,pervasiveoutput))
    das_fact(kind,Parent,rectangle)
	das_fact(direct_contains,Parent,Target)
## display
das_fact(direct_contains,${Parent},${Edge}).
  


