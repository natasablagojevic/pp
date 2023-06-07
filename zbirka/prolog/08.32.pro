clan(X, [X|_]).
clan(X, [_|R]):- clan(X,R).

