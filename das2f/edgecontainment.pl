% see evaluation.png

edge_containment(Parent,Edge) :- edge_containment_case_1(Parent,Edge).
edge_containment(Parent,Edge) :- edge_containment_case_2(Parent,Edge).
edge_containment(Parent,Edge) :- edge_containment_case_3(Parent,Edge).
edge_containment(Parent,Edge) :- edge_containment_case_4(Parent,Edge).

edge_containment_case_1(Parent,Edge):-
    das_fact(kind,Edge,edge),
    diagram_fact(source,Edge,SourceLongID),
    normalizedName(SourceLongID,Xport),
    diagram_fact(target,Edge,TargetLongID),
    normalizedName(TargetLongID,Yport),
    
    % belong to same Container
    das_fact(direct_contains,XComponent,Xport),
    das_fact(direct_contains,YComponent,Yport),
    das_fact(direct_contains,Container,XComponent),
    das_fact(direct_contains,Container,YComponent),
    
    Parent = Container.

edge_containment_case_2(Parent,Edge):-
    das_fact(kind,Edge,edge),
    diagram_fact(source,Edge,SourceLongID),
    normalizedName(SourceLongID,ChildPort),
    diagram_fact(target,Edge,TargetLongID),
    normalizedName(TargetLongID,ParentPort),
    
    % Child belongs to Parent Container
    das_fact(direct_contains,ChildComponent,ChildPort),
    das_fact(direct_contains,Container,ParentPort),
    das_fact(direct_contains,Container,ChildComponent),
    
    Parent = Container.

edge_containment_case_3(Parent,Edge):-
    das_fact(kind,Edge,edge),
    diagram_fact(source,Edge,SourceLongID),
    normalizedName(SourceLongID,ParentPort),
    diagram_fact(target,Edge,TargetLongID),
    normalizedName(TargetLongID,ChildPort),
    
    % Child belongs to Parent Container
    das_fact(direct_contains,ChildComponent,ChildPort),
    das_fact(direct_contains,Container,ParentPort),
    das_fact(direct_contains,Container,ChildComponent),
    
    Parent = Container.

edge_containment_case_4(Parent,Edge):-
    das_fact(kind,Edge,edge),
    diagram_fact(source,Edge,SourceLongID),
    normalizedName(SourceLongID,SourcePort),
    diagram_fact(target,Edge,TargetLongID),
    normalizedName(TargetLongID,TargetPort),
    
    das_fact(direct_contains,Container,SourcePort),
    das_fact(direct_contains,Container,TargetPort),
    
    Parent = Container.

normalizedName(LongID,ID):- diagram_fact(synonym,ID,LongID).
normalizedName(ID,ID):- \+ diagram_fact(synonym,ID,_).
