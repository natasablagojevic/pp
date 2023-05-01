import com.sun.org.apache.xpath.internal.operations.Bool

class Film{
  var naslov: String = "-"
  var trajanje: Int = 0
  var godina: Int = 0

  def this(naslov: String, trajanje: Int, godina: Int) = {
    this()
    this.naslov = naslov
    this.trajanje = trajanje
    this.godina = godina
  }

  // getters
  // cisti metodi
  def getNaslov: String = this.naslov
  def getTrajanje: Int = this.trajanje
  def getGodina: Int = this.godina



  override def toString: String = "Film " + naslov + " iz " + godina + " traje " + trajanje
}

class CrtaniFilm extends Film {
  var autor: String = "-"

  def this(naslov: String, trajanje: Int, godina: Int, autor: String) = {
    this()
    this.naslov = naslov
    this.trajanje = trajanje
    this.godina = godina
    this.autor = autor
  }
  override def toString: String = "Crtani: " + super.toString() + ". Autora: " + autor
}

object hello {
  def main(args: Array[String]): Unit = {
    // 1.
    println("Hello world")
    // jednostruki komentari
    /* viselinijski komentar */

    // 2. Promenljive
    /*
    *   var - variable (mogu menjati vrednosti)
    *   val - value (promenljive koje su const koje ne menjaju vrednosti)
    *
    * */

    val c : Int = 43
    var x: Int = 32

    x += c
  // c += x

    println("val c: " + c)
    println("var x: " + x)

    // 3. grananje

    if (x > 0 && x < 10)
        println("jednocifreni")
    else if (x >10 && x < 100)
      println("dvocifren")
    else
      println("trocifren")

    // 4. stringovi
    val film: String = "Harry Poter"
    println("Film " + film + " je niska duzine " + film.length() + " karaktera")

    // indentacija stringova
    println(s"Film $film je niska")
    println(
      """
        |Ovo je
        |ispis u
        |vise linija!
        |""".stripMargin)

    // 5. WHILE
    var trajanje:Int = 206
    var sati: Int = 0

    while (trajanje >= 60) {
      sati += 1
      trajanje -= 60
    }

    println(s"Trajanje film $sati sati i $trajanje minuta")

    // 6. FOR
    // [0, 10)
    for (i <- 0 until 10)
      print(i)
    println()

    // [0, 10]
    for (i <- 0 to 10)
      print(i)
    println()

    // [0, 10)
    for (i <- Range(0, 10))
      print(i)
    println()

    // kolekcijsko iteriranje
    for (c <- "asfghiau")
      print(c)
    println()
    println()
    // 7. NIZOVI
    var filmovi: Array[String] = new Array[String](4)
    filmovi(0) = "Zikina dinastija"
    filmovi(1) = "Varljivo leto '69"
    filmovi(2) = "Munje"
    filmovi(3) = "Cao inspektore"


    // 8. FUNKCIJE
    /*
    * def imeFunkcije(arg1: Tip1, .., argN: TipN): povratnaVrednost = {
    *   TeloFunkcije
    * }
    * */

    ispisiFilmove(filmovi)
    ispisiFilmoveSortirano(filmovi)

    // 9. OOP KONCEPTI
    /*
    * class ImeKlase {
    *   teloKlase
    * }
    *
    * class ImeKlase(argumentiKonstruktora) {
    *   teloKlase
    * }
    * */

    val f: Film = new Film("Tom and Jarry", 30, 1990)
    val p: CrtaniFilm = new CrtaniFilm("Code Lyoko", 25, 2010, "Volt Disney")
    println(f)
    println(p)
  }

  /*
  *   Povratni tip ne mora da se navodi, jer on na osnovu tela
  *   funkcije moze da zakljuci
  * */
  def ispisiFilmove(filmovi: Array[String]): Unit = {
    println("Filmovi: ")
    for (film <- filmovi)
      println(film)
    println()

  }

  def ispisiFilmoveSortirano(filmovi: Array[String]): Unit = {
    println("Filmovi sortirano: ")
//    for (film <- filmovi.sortWith(sortirajLT))
//      println(film)
//    println()

    for (film <- filmovi.sortWith((f1: String, f2: String) => { if (f1.compareTo(f2) < 0) true else false}: Boolean))
      println(film)
    println()
  }

  def sortirajLT(f1: String, f2: String): Boolean = {
    if (f1.compareTo(f2) < 0)
      return true
    else
      return false
  }
}
