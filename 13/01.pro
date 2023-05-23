% dodajPocetak(E, L, L1)
dodajPocetak(E, L, L1):- L1 = [E|L].
% dodajPocetak(E, L, [E, L]).

% dodajKraj(E, L, L1).
dodajKraj(E, [], [E]).
dodajKraj(E, [G|R], L):- dodajKraj(E, R, L1), L = [G|L1].

% obrisiPrvi(L, L1)
obrisiPrvi([], _):- fail.
obrisiPrvi([_|R], R).

% obrisiPoslednji(L, L1)
obrisiPoslednji([], _):- fail.
obrisiPoslednji([_], []):- !.
obrisiPoslednji([G|R], [G|L1]):- obrisiPoslednji(R, L1).

% maksimum(L, M)
maksimum([], _):- fail.
maksimum([G], G):- !.
maksimum([G|R], M):- maksimum(R, M1), G >= M1, M is G, !.
maksimum([G|R], M):- maksimum(R, M1), G < M1, M is M1.

% bude na ispitu
% zagonetke
% k(boja, nacionalnost, jelo, pice, ljubimac)

% Da li je E u liti L?
clan(E, [E|_]).
clan(E, [_|R]):- clan(E, R).

% da i je X odmah desno nakon Y u listi L?
% desno(X, Y, L)
desno(X, Y, [Y, X|_]).
desno(X, Y, [_|R]):- desno(X, Y, R).

% da li su X i Y jedno pored drugog u listi L?
% pored(X, Y, L)
pored(X, Y,[X, Y|_]).
pored(X, Y, [Y,X|_]).
pored(X, Y, [_|R]):- pored(X, Y, R).

kuce(L):-
    L = [
        k(_,norvezanin,_,_,_),
        k(plava,_,_,_,_),
        k(_,_,_,mleko,_),
        k(_,_,_,_,_),
        k(_,_,_,_,_)
    ],
    clan(k(crvena, englez,_,_,_), L),
    clan(k(_,spanac,_,_,pas), L),
    clan(k(zelena,_,_,kafa,_), L),
    clan(k(_,ukrajunac,_,caj,_), L),
    desno(k(zelena,_,_,_,_), k(bela,_,_,_,_), L),
    clan(k(_,_,spagete,_,puz), L),
    clan(k(zuta,_,pica,_,_), L),
    pored(k(_,_,piletina,_,_), k(_,_,_,_,lisica), L),
    pored(k(_,_,pica,_,_), k(_,_,_,_,konj), L),
    clan(k(_,_,brokoli,narandza,_), L),
    clan(k(_,japanac,susim,_,_), L),
    clan(k(_,_,_,_,zebra), L),
    clan(k(_,_,_,voda,_), L).

zagonetka(X, Y):- kuce(L), clan(k(_,X,_,_,zebra), L),
                  clan(k(_, Y,_, voda,_), L).