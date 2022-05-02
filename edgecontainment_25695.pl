:- use_module(library(http/json)).
?- consult("fb.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das2json/das2f/shapes.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das2json/das2f/onSameDiagram.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das2json/das2f/inside.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das2json/das2f/names.pl").
?- consult("/Users/tarvydas/quicklisp/local-projects/das2json/das2f/ports.pl").

?- consult("/Users/tarvydas/quicklisp/local-projects/das2json/das2f/edgecontainment.pl").

query_helper(Parent,Edge) :- edge_containment(Parent,Edge).

query:-
(bagof([Parent,Edge],query_helper(Parent,Edge),Bag),
json_write(user_output,Bag,[width(128)])
)
;
json_write(user_output,[],[width(123)]).
