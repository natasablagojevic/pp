import java.io.File
import java.util.Scanner
import java.util.concurrent.ConcurrentLinkedQueue
import java.util.concurrent.atomic.AtomicInteger


class Sluzbenica(kapital: AtomicInteger, kamata: Int, klijenti: ConcurrentLinkedQueue[Klijent], zaduzeni: ConcurrentLinkedQueue[Klijent]) extends Thread {
  override def run(): Unit = {
    while (true) {
      var klijent: Klijent = klijenti.poll()

      if (klijent == null)
        return

      println(s"Klijent ${klijent.getIme} razgovara sa sluzbenicom.")

      /** Kriticna sekcija - moze da se desi da sluzbenica da novac koji ne postoji */
      kapital.synchronized {
        if (klijent.getNovac > kapital.get()) {
          println(s"\tKlijent ${klijent.getIme} ne dobija pozajmicu od banke.")
        } else {
          Thread.sleep(5000)

          println(s"\tKlijent ${klijent.getIme} dobija pozajmicu od banke.")

          val noviKapital: Int = kapital.get() - klijent.getNovac
          kapital.set(noviKapital)

          klijent.setDug(klijent.getNovac * (100 * kamata) / 100f)

          zaduzeni.add(klijent)
          println(s"\t\tKlijent ${klijent.getIme} je dobio pozajmicu od banke.")
        }
      }
     }
  }
}
class Klijent(ime: String, novac: Int) {
  var dug: Float = 0

  def getIme: String = ime
  def getNovac: Int = novac
  def getDug: Float = dug

  def setDug(noviDug: Float): Unit = {
    this.dug = noviDug
  }

  override def toString: String = s"$ime = ($novac) - [${this.dug}]\n"
}

object Banka {
  def main(args: Array[String]): Unit = {
    /** UCITAVANJE PODATAKA */
    var sc: Scanner = new Scanner(new File("/home/natasa/Desktop/Fakultet/6_sem/pp/09/Scala/src/main/scala/klijenti.txt"))

    // deljena struktura - mora da bude konkuretna i da imamo konkuretne operacije
    val klijenti: ConcurrentLinkedQueue[Klijent] = new ConcurrentLinkedQueue[Klijent]()
    val zaduzeni: ConcurrentLinkedQueue[Klijent] = new ConcurrentLinkedQueue[Klijent]()

    while (sc.hasNextLine) {
      klijenti.add(new Klijent(sc.next(), sc.nextInt()))
    }

    println(klijenti)
    println(zaduzeni)
    /** Ekspozitura */
    sc = new Scanner(System.in)
    print("Kapital: ")
    val kapital: AtomicInteger = new AtomicInteger(sc.nextInt())

    print("Kamata: ")
    val kamata: Int = sc.nextInt()

    print("Broj sluzbenica: ")
    val n: Int = sc.nextInt()

    /** KREIRANJE SLUZBENICA - INICIJALIZACIJA */
    val sluzbenica: Array[Sluzbenica] = new Array[Sluzbenica](n)
    for (i <- 0 until n) {
      sluzbenica(i) = new Sluzbenica(kapital, kamata, klijenti, zaduzeni)
    }

    /** START */
    for (s <- sluzbenica)
      s.start()

    /** JOIN */
    for (s <- sluzbenica)
      s.join()

    /** ISPIS REZULTATA */
    println("Rezultat: ")
    println(klijenti)
    println(zaduzeni)
  }
}
