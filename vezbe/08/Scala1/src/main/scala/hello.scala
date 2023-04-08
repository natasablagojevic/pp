import java.util.concurrent.ThreadLocalRandom
import scala.util.Random.nextLong

class Film {
  var naslov: String = ""
  var trajanje: Int = 0
  var godina: Int = 0

  def this(nas:String, tr: Int, gd: Int) {
    this()
    this.naslov = nas
    this.godina = gd
    this.trajanje = tr
  }

  def getNaslov: String = this.naslov
  def getGodina: Int = this.godina
  def getTrajanje: Int = this.trajanje

  override def toString: String = s"${this.naslov} ${this.trajanje} ${this.godina}"
}

// nasledjuje metode i polja
// promenljive su vidjenje u nasledjenoj klasi
// package vidljivost
class CrtaniFilm extends Film{
  var animator: String = _

  def this(ns: String, tr: Int, gd: Int, an: String) {
    this()
//    super.this()

    this.naslov = ns
    this.trajanje = tr
    this.godina = gd
    this.animator = an
  }

  def getAnimator: String = this.animator

  override def toString: String = super.toString + s" Anmator: ${this.animator}"
}


class Konobar(name: String, brojStolova: Int) extends Thread{
  override def run(): Unit = {
    for (i <- 0 to brojStolova) {
      Thread.sleep(ThreadLocalRandom.current(), nextLong(0, 1))
      println(s"Konobar ${this.name} usluzio je sto ${i}.")
    }

    println(s"Konobar ${this.name} je otisao kuci. Kraj smene!")
  }
}


object hello {
  def main(args: Array[String]): Unit = {
    println("Hello")

    val n = 100
    var s = 0
    var i = 0

    while (i < n) {
      s += i
      i += 1
    }

    println(s"suma: $s")

    val filmovi: Array[String] = new Array[String](3)
    filmovi(0) = "Monte video bog te video"
    filmovi(1) = "Lajanje na zvezde"
    filmovi(2) = "Avatar 2"

    println("-----------------")
    println("Welcome to restoran Babaroga")
    var ivan: Konobar = new Konobar("Ivan", 5)
    var petar: Konobar = new Konobar("Petar", 5)
    var janko: Konobar = new Konobar("Janko", 5)
    var milan: Konobar = new Konobar("Milan", 7)

    ivan.start()
    petar.start()
    janko.start()
    milan.start()

    ivan.join()
    petar.join()
    janko.join()
    milan.join()

  }
}
