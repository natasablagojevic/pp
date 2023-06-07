
% imamo 5 kuca 
% k(boja, nacionalnost, pice, jela, ljubimci)

clan(E, [E|_]).
clan(E, [_|R]):- clan(E, R).

pored(X, Y, [X,Y|_]).
pored(X, Y, [Y,X|_]).
pored(X, Y, [_|R]):- pored(X, Y, R).

% X je desno od Y
desno(X, Y, [Y, X|_]).
desno(X, Y, [_|R]):- desno(X, Y, R).

zagonetka(L):-
    L = [
        k(_,norvezanin,_,_,_),
        k(plava,_,_,_,_),
        k(_,_,mleko,_,_),
        k(_,_,_,_,_),
        k(_,_,_,_,_)
    ], 
    clan(k(crvena, englez,_,_,_), L),
    clan(k(_,spanac, _,_,pas), L),
    clan(k(zelena,_,kafa,_,_), L),
    clan(k(_,ukrajunac, caj,_,_), L),
    clan(k(_,_,_,spagete, puz), L),
    clan(k(zuta,_,_,pica,_), L),
    clan(k(_,japanac,_,susi,_), L),
    clan(k(_,_,narandza, brokoli,_), L),
    pored(k(_,_,_,piletina,_), k(_,_,_,_,lisica), L),
    pored(k(_,_,_,pica,_), k(_,_,_,_,konj), L),
    desno(k(zelena,_,_,_,_), k(bela,_,_,_,_), L).

resenje(X, Y):- zagonetka(L), clan(k(_,X,_,_,zebra), L), clan(k(_,Y,voda,_,_), L).


