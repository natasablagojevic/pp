/*
    Lista:
        - []
        - .(G, R)

    ex: [], .(1, []), .(1, .(2, [])), ..
        [a, b, c] same as: .(a, .(b, .(c, [])))

    Unifikacija:
        - [G|R]
        - [G1, G2|R]
        - ... 
*/

% sadrzi(X, L)
sadrzi(X, [X|_]).
sadrzi(X, [G|R]):- sadrzi(X, R).

sadrzi1(X, [G|R]):- X == G, sadrzi(X, R).

% suma(L, S).
suma([], 0).
suma([G|R], S):- suma(R, S1), S is G + S1.

duzina([], 0).
duzina([G|R], S):- duzina(R, S1), S is 1 + S1.

% as(L, AS)
as([], 0).
as([G|R], S):- duzina([G|R], D), suma([G, R], Z), S is Z/D.

% ucitaj(N, L)
% u L ucitavam listu od N elemenata

ucitaj(N, _):- N < 0, !.
ucitaj(0, []).
ucitaj(N, [G|R]):- N >0, write('elem: '), read(G),  N1 is N-1, ucitaj(N1, R).