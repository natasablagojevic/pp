musko(mihajlo).
musko(stevan).
musko(petar).
musko(mladen).
musko(rajko).

zensko(milena).
zensko(milica).
zensko(jelena).
zensko(senka).
zensko(mina).
zensko(minja).

roditelj(mihajlo, milica).
roditelj(mihajlo, senka).
roditelj(milena, rajko).
roditelj(maja, petar).
roditelj(maja, mina).
roditelj(stevan, mladen).
roditelj(stevan, jelena).
roditelj(milica, mladen).
roditelj(milica, jelena).

% X je majka od Y 
majka(X, Y):- zroditelj(X, Y), zensko(X).

% X je brat od Y
brat(X, Y):- musko(Y), roditelj(Z, X), roditelj(Z, Y). 

% predak
predak(X, Y):- roditelj(X, Y).
predak(X, Y):- roditelj(X, Z), predak(Z, Y).