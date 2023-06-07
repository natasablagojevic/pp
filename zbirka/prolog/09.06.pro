res(Vars):-
    Vars = [T,W,O,F,U,R],
    Vars:: 1..9,
    alldifferent(Vars),
    2*(100*T+10*W+O) #= (1000*F+100*O+10*U+R),
    labeling(Vars).