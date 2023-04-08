# Uvod u Scala

  # **Promenljive**
   - **var** - variable (mogu menjati vrednosti)
   - **val** - value (promenljive koje su const, koje ne mogu menjati vrednosti) <br>
   val film: **String** = "Harry Poter" <br>
   - indentaija stringova <br>
   println(**s**"Film $film je niska") <br> 
   
   **println("""  <br>
     | Ovo je  <br>
     | ispis u  <br>
     | vise linija  <br>
     |""".stripMargin)**
    
  # Petlje
  ## WHILE
    val trajanje: Int = 206 
    var sati:Int = 0 
    while (trajanje >= 60) { 
      sati += 1 
      trajanje -= 60 
    } 
    println(s"Trajanje filma $sati sati i $trajanje minuta") 
    
  ## FOR
    [0, 10)
    for (i <- 0 until 10)
      print(i + " ")
     println()
     
     [0, 10]
     for (i <- 0 to 10)
      print(i + " ")
     println()
     
     [0, 10)
     for (i <- Range(0, 10))
      print(i + " ")
     println()
     
      kolekcijska:
      for (c <- "ashjfg")
        print(c + " ")
       println()

  # FUNKCIJE
      def imeFunkcije(arg1: Tip1, ..., argN: TipN): PovratnaVrednost = {
       teloFunkcije
      }
      
  # OOP KONCEPTI 
      class ImeKlase {
        // konstruktor 
        def this(...) = {
          // bazni konstruktor
          this()
          this.atribut1 = vr1
          this.atribut2 = vr2 
          ...
          this.atrinutN = vrN
        }
      }
      
      class ImeKlase {
        teloKlase
      }
      
      class ImeKlase(argumentiKonstruktora) {
        teloKlase
      }
