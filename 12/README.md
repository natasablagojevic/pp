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

- Sve sto Prolog radi jeste da pokusava da **generise neka resenja**, pretragom baze cinjenica i pravila koja su definisana

- **Sve sto se navede smatra se da je tacno, sve sto se ne navede smatra se da je netacno** 

- Sve sto prolog radi jeste dodeljivanje vrednosti promenljivoj tako da vazi

- Provera tipa:

            atom(11) - da li je atom
            atomic(11.4) - da li je atom ili broj
            number(23) - da li je broj
            float(23.1) - da li je razlomljeni broj
            var(X) - da li je promenljiva
            nonvar(X) - 



            = unifikabilnost (prisustvo promenljivih i dodelu vrednosti promenljivih, u cilju postizanja logicki tacno)
            == indeticka jednakost

