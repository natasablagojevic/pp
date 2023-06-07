clan(E, [E|_]).
clan(E, [_|R]):- clan(E, R).

% d(ime, prezime,  vrsta, boja)


drugarice(L):- 
    L = [
        d(milica, _, _, _),
        d(anja, _, _, _),
    ],
    clan(d(_,ranisavljevic,_zelena), L),
    clan(d(_,_,cizme,braon), L),
    not(clan(d(_,cugurovic,cizme,braon), L)),
    not(clan(d(_,_,cipele,pink), L)),
    not(clan(kaca, andonov,cizme,_),L),
    