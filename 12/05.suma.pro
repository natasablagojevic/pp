% suma prvih n prirodnih brojeva
% suma(X, S)

suma(1, 1):- !.
suma(N, S):- N > 0, N1 is N-1, suma(N1, S1), S is N+S1. 