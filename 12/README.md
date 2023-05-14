 Logicko programiranje

- **Deklerativna paradigma** - dovoljno je samo opisati problem

- Zasniva se na logici prvog reda

- path: **/opt/BProlog/bp** na ispitu treba naci i tu raditi logicko programiranje

            % linijski komentar
            /* viselinijski komentar */

- REDOM:
            
            compile('fajl)
            load('fajl')
            halt - izlaz
            cl('fajl') - kompajlira i loduje

Term:
    - Konstante
        - Atomi (abc, a112, aAAA, ..)
        - Brojevi (11, 23.3, ..)
    - Promenljive (X, Y, _a (anonimna promenljiva))
    - Kompozitni termovi (f(t1, ..., tn)) 

- Hornoive klauze:
    - Cinjenice = atomicna formula (p(t1, ..., tn)) 
    - Pravila (H:- B1, B2, .., Bn) = definisanje zakljucivanja - ako vazi **B1, .., Bn** onda vazi i **H** = 
    - Upiti 

- Program (niz Hornoive klauzula)