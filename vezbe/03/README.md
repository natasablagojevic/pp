# Funkcije viseg reda

* Funkcije viseg reda su:
  1. MAP - mapira elemente kolekcije
  2. FILTER - filtrira elemente po nekom kriterijumu
  3. REDUCE - sazima kolekciju u jedan broj
  4. ZIP - spaja dve liste u jednu, tako sto uzima po jedan element iz obe liste

* Ove funkcije moraju da primaju **kolekciju koja je iterabilna**
* Mogu da se koriste lambda funkcije
    * Sintaksa:
    >lambda argumenti : telo funkcije
  

# Ogranicenja

* Prvo je potrebno importovati biblioteku **constraint**:
  >import constraint 
  
* Svaka ogranicenja se zasnivaju na istom principu, tako sto:
  1. Definisemo problem
     >problem = constraint.Problem()
  2. Definisemo promenljive
     >problem.addVariable(promenljiva, domen) 
  
     >problem.addVariables(promenljive, domen)
  3. Definicija ogranicenja i dodavanje ogranicenja
     * definicija se najcesce satoji ili iz vec postojece funkcije iz **constraint**-a ili iz nase f-je
     * ako mi sami definisemo ogranicenje, potrebno je da:
        1. ako je ogranicenje zadovoljeno, vratimo **True**
        2. a ako nije **False**, ali ono ne mora eksplicitno da se navodi
       
     >problem.addConstraint(f_ja_ogranicenja, promenljive_redom)
    
     >problem.addConstraint(constraint.AllDifferentConstraint()) 
     
     >problem.addConstraint(constraint.ExactSumConstraint()) 
    
     >problem.addConstraint(constraint.MinSumConstraint()) 
      
     >problem.addConstraint(constraint.InSetConstraint()) 
      
     >problem.addConstraint(constraint.MaxSumConstraint()) 

# Notes:
* **prednosti** constraint ogranicenja:  lakse je za programiranje, moje je da definisem problem, a alat ce da resi

* **mana** constraint: nije efikasno jer se desava kombinatorna eksplozija i to kosta mnogo

* map, filter, reduce:  **funkcije viseg reda**, mogu da prime argument kao funkciju ili da vrate funkciju

    * map : na sve elemente primeni funkciju <br>
    * filter : izfiltriraj listu po nekom zadatom kriterijumu <br>
    * reduce : sazimam sve elemente u jednu vrednost <br>
