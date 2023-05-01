import java.io.File
import java.util
import java.util.Scanner
import java.util.concurrent.{ConcurrentHashMap, ThreadLocalRandom}
import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer

class Kladionicar(ime: String, novac: Int, tiket: mutable.HashMap[String, Char], utakmice: mutable.HashMap[String, (Float, Float, Float, Char)]) extends Thread {

  var zarada: Float = 0f

  override def run(): Unit = {
    /** Gleda utakmice */
    println(s"$ime start...")

    // locked
    utakmice.synchronized {
      utakmice.wait()
    }

    var pogodjeno: Int = 0
    var kvota: Float = 0f

    for (t <- tiket) {
      if (t._2 == utakmice(t._1)._4) {
        println(s"\tKladionicar $ime je pogodio rezultat utakmice ${t._1}")
        pogodjeno += 1

        if (utakmice(t._1)._4 == '1') {
          kvota *= utakmice(t._1)._1
        } else if (utakmice(t._1)._4 == 'x') {
          kvota *= utakmice(t._1)._2
        } else if (utakmice(t._1)._4 == '2') {
          kvota *= utakmice(t._1)._3
        } else {
          throw new RuntimeException("Invalid game result.")
        }
      } else {
        println(s"\tKladionicar $ime nije pogodio rezultat utakmice ${t._1}")
      }
    }

    if (pogodjeno == 5) {
      println(s"\t\t$ime je prosao tiket: $tiket")
      println(s"\t\tDobitak: ${novac * kvota}")
    } else {
      println(s"\t\t$ime nije prosao tiket: $tiket")
    }

    println(s"$ime end.")

    /** Racuna zaradu */


  }

  override def toString: String = s"[$ime, $novac, $tiket]\n"
}

object Kladionice {
  def main(args: Array[String]): Unit = {
    /** Ucitavanje podataka */

    val sck: Scanner = new Scanner(new File("/home/natasa/Desktop/Fakultet/6_sem/pp/09/Scala/src/main/scala/kladionice.txt"))
    val scu: Scanner = new Scanner(new File("/home/natasa/Desktop/Fakultet/6_sem/pp/09/Scala/src/main/scala/kvote.txt"))

    val utakmice: mutable.HashMap[String, (Float, Float, Float, Char)] = new mutable.HashMap[String, (Float, Float, Float, Char)]()
    while (scu.hasNextLine) {
      utakmice.put(scu.nextLine(), (scu.nextFloat(), scu.nextFloat(), scu.nextFloat(), '-'))
      scu.nextLine()
    }

    println(utakmice)

    val kladionicari: ArrayBuffer[Kladionicar] = new ArrayBuffer[Kladionicar]()
    while (sck.hasNextLine) {
      var ime: String = sck.next()
      var novac: Int = sck.nextInt()
      val tiket: mutable.HashMap[String, Char] = new mutable.HashMap[String, Char]()

      for (i <- 0 until 5) {
        sck.nextLine()
        tiket.put(sck.nextLine(), sck.next()(0))
      }

      kladionicari.append(new Kladionicar(ime, novac, tiket, utakmice))
    }

    println(kladionicari)

    /** START */
    for (k <- kladionicari)
      k.start()

    println("Igranje utakmice ....")
    Thread.sleep(9000)
    println("Utakmice odigrane, rezultati: ")

    val res = Array('1', 'x', '2')
    for (u <- utakmice)
      utakmice(u._1) = (u._2._1, u._2._2, u._2._3, res(ThreadLocalRandom.current().nextInt(0, 3)))

    println(utakmice)

    // unlockede
    utakmice.synchronized{
      utakmice.notifyAll()
    }

    /** JOIN */
    for (k <- kladionicari)
      k.join()

    /** RESULT */
    println("Main END!")
  }
}
