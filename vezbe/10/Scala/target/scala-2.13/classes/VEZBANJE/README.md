# Distribuirano programiranje

- **Vise racunara** sa kojim grade istu stvar
- stednja resursa, necemo svi odjednom radti kompleksne stvar
- klaster racunari i nude svoje resurse
- socijalne mreze (Instagram) : fizicko skladistenje podataka
- sinhronizacija?
- moje je samo da zadam sta hocu i kako hocu da izracunam i da mi vrate samo rezultat

    - Driver program (main)
    - Klaster racunari
  - SparkContext()
  - RDD podaci (Resilient Distributed Dataset)
    - transformacije: **RDD -> RDD** [map, filter, flatMap, aggregateByKey, sortByKey, ...]
    - akcije:         **RDD -> data** [collect, reduce, take, count, foreach, ...]
  - flatMap preslikavanje: 1u1, 1uVise, 1u0 
- 