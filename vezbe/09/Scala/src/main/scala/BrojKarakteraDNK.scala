import java.io.File
import java.util.Scanner
import java.util.concurrent.ConcurrentHashMap
import scala.collection.mutable.ArrayBuffer

/** Broji baze u linije[poc, kraj) */
class Brojac(poc: Int, kraj: Int, linije: ArrayBuffer[String], res: ConcurrentHashMap[Char, Int]) extends Thread {
  override def run(): Unit = {
    for (i <- 0 until kraj) {
      val a: Int = linije(i).count(_ == 'A')
      val g: Int = linije(i).count(_ == 'G')
      val c: Int = linije(i).count(_ == 'C')
      val t: Int = linije(i).count(_ == 'T')

      // samo jedna nit moze da pritupi kriticnoj sekciji u jednom trenutku
      /** Synchronized kljucna rec za zakljucavanje kriticne sekcije */
      res.synchronized {
        res.replace('A', res.get('A' + 'a'))
        res.replace('G', res.get('G' + 'g'))
        res.replace('C', res.get('C' + 'c'))
        res.replace('T', res.get('T' + 't'))
      }
    }
  }
}

object BrojKarakteraDNK {
  def main(args: Array[String]): Unit = {
    println("Pariranje BIO podataka")

    val sc = new Scanner(System.in)

//    ConcurrentHashMap

    /** UCITAVANJE NITI*/
    println("Unesite broj niti: ")
    val n = sc.nextInt()

    /** UCITAVANJE PODATAKA */
    val data_path = "/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/09/Scala/src/test/scala/bio_data.log"
    val linije = new ArrayBuffer[String]()
    val scf = new Scanner(new File(data_path))

    while (scf.hasNextLine()) {
      linije.append(scf.nextLine())
    }

    val l = linije.length
    println("Obradjijemo BIO podatke duzine: " + l)

    /** REZULTAT*/
    val res = new ConcurrentHashMap[Char, Int](4)
    res.put('A', 0)
    res.put('G', 0)
    res.put('T', 0)
    res.put('C', 0)

    val korak: Int = math.ceil(l.toDouble/n).toInt
//    val duzina: Int = new Array[Brojac](n)
    val brojac = new Array[Brojac](n)
    for (i <- 0 until n) {
      brojac(i) = new Brojac(i*korak, Math.min((i+1)*korak, l), linije, res)
    }

    for (b <- brojac)
      b.start()

    for (b <- brojac)
      b.join()

    println(res)
  }
}
