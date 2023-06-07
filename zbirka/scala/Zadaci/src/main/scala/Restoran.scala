import java.util.Scanner
import scala.concurrent.forkjoin.ThreadLocalRandom

class Konobar(ime: String, brStolova: Int) extends Thread{
  override def run(): Unit = {
    for (i <- 0 until brStolova) {
      Thread.sleep(ThreadLocalRandom.current().nextInt(1,10)*1000)
      println("Konobar: " + this.ime + " je usluzio " + i + ". sto.")
    }

    println("Konobar: " + this.ime + " je zavrsio sa posluzivanjem.")
  }
}

object Restoran {
  def main(args: Array[String]): Unit = {
    val sc: Scanner = new Scanner(System.in)

    print("Unesite neusluzen broj stolova u restoranu: ")
    val brojStolova = sc.nextInt()

    val korak = Math.ceil(brojStolova/5.0).toInt

    val marko = new Konobar("Marko", korak)
    val nikola = new Konobar("Nikola", korak)
    val srdjan = new Konobar("Srdjan", korak)
    val mirko = new Konobar("Mirko", korak)
    val djordje = new Konobar("Djordje", brojStolova - 4*korak)

    marko.start()
    nikola.start()
    srdjan.start()
    mirko.start()
    djordje.start()



  }
}
