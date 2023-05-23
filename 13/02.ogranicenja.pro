% Prolog Constraint
% Sudoku:
% X X X     X X X   X X X
% X X X     X X X   X X X
% X X X     X X X   X X X

% X X X     X X X   X X X
% X X X     X X X   X X X
% X X X     X X X   X X X

% X X X     X X X   X X X
% X X X     X X X   X X X
% X X X     X X X   X X X

/*
    PROLOG CONSTRAINT
    1. Generisanje promenljivih i domena:
        X in D, X :: D, Vars in D, Vars :: D
        D 1..10, 1..2..30
    2. Generisanje ogranicenja:
        1. General:
            alldiferent(Vars), alldistinct(Vars),
            atmost(N, L, V), atleast(N, L, V), exactly(N, L, V)
        2. Arithmetics:
            E1 R E2
            E1, E2 arithmetic expression
            R #=, #\=, #>, #>=, #<, #=<
            min(L), max(L), max(E1, E2), sum(L), etc.
    3. Resavanje
            labeling(vars), labeling([minimize], vars)
*/

primer(Vars):- 
    Vars = [X, Y, Z],
    X :: 1..3,
    [Y, Z] :: 5..2..11,
    Y #> Z,
    alldifferent(Vars),
    labeling(Vars).

kvadrati(Vars):-
    Vars = [X],
    X :: 1..100,
    Y*Y #= X,
    labeling(Vars).


% ABCDE, min(A+2B-3C+4D-5E)

petocifren:-
    Vars = [A, B, C, D, E],
    Vars :: 0..9,
    A #\= 0,
    alldifferent(Vars),
    labeling([minimize(A + 2*B - 3*C + 4*D - 5*E)], Vars),
    Broj is 10000*A+1000*B+100*C+10*D+E,
    write(Broj).

% Magicni kvadrat
% A B C
% D E F
% G H I

magicni(Vars):-
    Vars = [A, B, C, D, E, F, G, H, I],
    Vars :: 0..9,
    A + B + C #= 15,
    D + E + F #= 15,
    G + H + I #= 15,
    A + D + G #= 15,
    B + E + H #= 15,
    C + F + I #= 15,
    A + E + I #= 15, 
    C + E + G #= 15,
    labeling(Vars),
    write(A), write(' '), write(B), write(' '), write(C), nl,
    write(D), write(' '), write(E), write(' '), write(F), nl,
    write(G), write(' '), write(H), write(' '), write(I), nl, nl.