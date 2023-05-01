import java.io.File
import java.util.Scanner
import java.util.concurrent.ConcurrentHashMap
import scala.collection.mutable.ArrayBuffer

class Brojac(pocetak: Int, kraj: Int, linije: ArrayBuffer[String], rezultat: ConcurrentHashMap[Char, Int]) extends Thread {
  override def run(): Unit = {
    /** Prolazimo kroz linije */
    for (i <- pocetak until kraj) {
      val a = linije(i).count(_ == 'A')
      val t = linije(i).count(_ == 'T')
      val g = linije(i).count(_ == 'G')
      val c = linije(i).count(_ == 'C')

      /** !!!! Sinhronizacija brojaca! - OBAVEZNOOO!!!!! */
      /** Na staru vrednost dodajemo onoliko koliko smo izbrojali */
      rezultat.synchronized {
        /** KRITICNA SEKCIJA */
        rezultat.replace('A', rezultat.get('A') + a)
        rezultat.replace('T', rezultat.get('T') + t)
        rezultat.replace('G', rezultat.get('G') + g)
        rezultat.replace('C', rezultat.get('C') + c)
      }
    }
  }

  override def toString: String = s"Brojac $pocetak - $kraj."
}

object DNK {
  def main(args: Array[String]): Unit = {

    /** UCITAVANJE PODATAKA */
    val sc: Scanner = new Scanner(new File("/home/natasa/Desktop/Fakultet/6_sem/pp/09/dna.txt"))

    val linije = new ArrayBuffer[String]()
    while (sc.hasNext()) {
      linije.append(sc.nextLine())
    }

    val n: Int = linije.length
    println("Duzina DNK sekvence je: " + n)

    /** SETUP ENV */
    val scin: Scanner = new Scanner(System.in)
    println(s"Broj fizickih procesora na racunaru: ${Runtime.getRuntime.availableProcessors()}")
    println("Broj niti: ")
    val m: Int = scin.nextInt()
    var brojaci: Array[Brojac] = new Array[Brojac](m)
    var rezultat: ConcurrentHashMap[Char, Int] = new ConcurrentHashMap[Char, Int](4, 0.75f, m)
    rezultat.put('A', 0)
    rezultat.put('T', 0)
    rezultat.put('G', 0)
    rezultat.put('C', 0)

    /** INICIJALIZACIJA */
    val korak: Int = Math.ceil((n.toFloat/m)).toInt
    for (i <- 0 until m) {
      brojaci(i) = new Brojac(i * korak, Math.min((i+1)*korak, n), linije, rezultat)
    }

    for (b <- brojaci)
      println(b)

    /** START */
    for (b <- brojaci)
      b.start()

    /** JOIN */
    for (b <- brojaci)
      b.join()

    /** ISPIS REZULTATA */
    print(rezultat)
  }

}
