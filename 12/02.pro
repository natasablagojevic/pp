% abs(X, Y) where Y <- |X|
% abs(5, Y) -> Y = 5
% abs(-4, Y) -> Y = 4

abs(X, Y):- X >= 0, Y is X.
abs(X, Y):- X < 0, Y is -X.

abs1(X, X):- X >= 0.
abs1(X, Y):- X < 0, Y is -X.


abs2(X, X):- X >= 0.
abs2(X, Y):- Y is -X.

abs3(X, X):- X >= 0, !.
abs3(X, Y):- Y is -X.

abs4(X, X):- X >= 0, !, write('iza').
abs4(X, Y):- Y is -X.

abs5(X, X):- X >= 0, !.
abs5(X, -X).