/*
    Godina je prestupna ako:
        - je deljiva sa 400
        - je deljiva sa 4 i ne sa 100
*/

prestupna(X):- X mod 400 =:= 0.
prestupna(X):- X mod 4 =:= 0, X mod 100 =\= 0.

/*
    brdana(januar, 2021, X) -> X je 31
*/

brdana(januar, _, 31).

brdana(februar, X, 28):- not(prestupna(X)), !.
brdana(februar, X, 29):- prestupna(X).

% I ovo je dobro resenje:
% brdana(februar, X, 29):- prestupna(X), !.
% brdana(februar, X, 28).

brdana(mart, _, 31).
brdana(april, _30).
brdana(maj, _, 31).
brdana(jun, _, 30).
brdana(jul, _, 31).
brdana(avgust, _, 31).
brdana(septembar, _, 30).
brdana(oktobar, _, 31).
brdana(novembra, _, 30).
brdana(decembar, _, 31).

