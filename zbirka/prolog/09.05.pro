res(Vars):-
    Vars = [X, Y, Z],
    X:: 1..90,
    Y:: 2..4..60,
    Z:: 1..10..100,
    X #>= Z,
    2*X+X*Y+Z #=< 34,
    labeling(Vars),
    write(X), write(' '), write(Y), write(' '), write(Z), nl.
     