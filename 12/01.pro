% jednolinijski komentar
/* viselinijski komentari */

/*
    Term:
        - Konstante
            - Atomi (abc, a112, aAAA, ..)
            - Brojevi (11, 23.3, ..)
        - Promenljive (X, Y, _a (anonimna promenljiva))
        - Kompozitni termovi (f(t1, ..., tn))
*/

% cinjenica - predikati
zivotinja(slon).
zivotinja(vuk).
zivotinja(zec).
zivotinja(zebra).
zivotinja(mrav).
/*
    Ako postavimo upit: zivotinja(slon) vratice 'yes', jer je u svojoj bazi znanja pronasao da je slon zivotinja i to se 
    tumaci kao tacno
*/

veci(slon, vuk).
veci(vuk, zec).
veci(zec, mrav).

% pravila
je_veci(X, Y):- veci(X, Y).
je_veci(X, Y):- veci(X, Z), je_veci(Z, Y).

