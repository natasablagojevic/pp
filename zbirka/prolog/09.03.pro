primer(Vars):-
    Vars = [D1, D2, D5, D10, D20],
    D1:: 0..50,
    D2:: 0..25,
    D5:: 0..10,
    D10:: 0..5,
    D20:: 0..2,
    D1 + 2*D2 + 5*D5 + 10*D10 + 20*D20 #= 50,
    labeling(Vars).
    % write(D1), write(' '), write(D2), write(' '), write(D5), nl,
    % write(D10), ' ', write(D20)