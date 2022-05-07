# layer kind
## parameters
  ID
  Direction
## imports
  fb
  shapes
  onSameDiagram
  inside
## forall ID as diagram_fact(kind,ID,"ellipse")
    Direction = cond
      diagram_fact(color, ID, "green")  input
      diagram_fact(color, ID, "yellow") output
      diagram_fact(color, ID, "red")    pervasiveinput
      diagram_fact(color, ID, "purple") pervasiveoutput
      else                              "?"
## design rule
  Direction is "?"
  "all ports must have a direction ; port ${ID} has no direction"
## display
  das_fact(direction,${ID},${Direction}).


should expand to

# layer direction
## parameters
  ID
  Direction
## imports
  fb
  shapes
  onSameDiagram
  inside
## query
diagram_fact(kind,ID,"ellipse") 
(diagram_fact(color, ID, "green")  -> Direction = input;diagram_fact(color, ID, "yellow")  -> Direction = output;diagram_fact(color, ID, "red")  -> Direction = pervasiveinput;diagram_fact(color, ID, "purple")  -> Direction = pervasiveoutput; Direction = "?")
## cond
  Direction is "?" 
  all ports must have a direction ; port ${ID} has no direction
## display
  das_fact(direction,${ID},${Direction}).


.js
if (Direction === "?") {
  console.error (`all ports must have a direction ; port ${ID} has no direction\n`);
} else {
  console.log (`das_fact(direction,${ID},${Direction}).`);
}

--or?--
# layer kind
## parameters
  ID
  Direction
## imports
  fb
  shapes
  onSameDiagram
  inside
## query
diagram_fact(kind,ID,"ellipse") 
(diagram_fact(color, ID, "green")  -> Direction = input;diagram_fact(color, ID, "yellow")  -> Direction = output;diagram_fact(color, ID, "red")  -> Direction = pervasiveinput;diagram_fact(color, ID, "purple")  -> Direction = pervasiveoutput; Direction = "?")
## cond display
  Direction is "?" 
  all ports must have a direction ; port ${ID} has no direction
  das_fact(direction,${ID},${Direction}).
