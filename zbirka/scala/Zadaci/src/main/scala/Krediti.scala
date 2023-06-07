import java.io.File
import java.util.Scanner
import java.util.concurrent.ConcurrentLinkedQueue
import java.util.concurrent.atomic.AtomicLong
import scala.concurrent.forkjoin.ThreadLocalRandom

class Sluzbenice(kamata: Int, kapital: AtomicLong,
                 redKlijenata: ConcurrentLinkedQueue[Klijent],
                 zaduzeniKlijenti: ConcurrentLinkedQueue[Klijent])
      extends Thread {
  override def run(): Unit = {
    while (true) {
      var k: Klijent = redKlijenata.poll()

      if (k == null)
        return

      println("Klijent: " + k.getIme() + " razgovara sa sluzbenicom.")
      Thread.sleep(ThreadLocalRandom.current().nextInt(1,10)*1000)

      kapital.synchronized{
        if (k.getPozajmica() > kapital.get())
          println("Klijent " + k.getIme() + " ne moze dobiti kredit")
        else {
          k.setDug(k.getPozajmica()*((100f+kamata.toFloat)/1000.0f))

          val novKapital = kapital.get() - k.getPozajmica()
          kapital.set(novKapital)

          println("Klijent: " + k.getIme() + " je dobio kredit od " + k.getPozajmica() + " sa kamatom: " + k.getDug() )
          zaduzeniKlijenti.add(k)
        }
      }
    }
  }
}

class Klijent(ime: String, pozajmica: Int) {
  var dug: Float = 0.0f
  def getIme(): String = this.ime
  def getPozajmica(): Int = this.pozajmica
  def getDug(): Float = dug

  def setDug(d: Float): Unit = {
    this.dug = d
  }
}

object Krediti {

  def main(args: Array[String]): Unit = {
    var sc: Scanner = new Scanner(System.in)

    print("Uneti pocetni kapital: ")
    var kapital = new AtomicLong(sc.nextInt())

    val savedKapital = kapital.get()

    print("Unesite kamatnu stopu: ")
    var kamata: Int = sc.nextInt()

    print("Broj zaposlenih sluzbenica: ")
    var brojSluzbenica: Int = sc.nextInt()

    sc = new Scanner(new File("/home/natasa/Desktop/Fakultet/6_sem/pp/zbirka/scala/Zadaci/src/test/scala/red_klijenata.txt"))
//    ConcurrentLinkedQueue

    val sluzbenice = new Array[Sluzbenice](brojSluzbenica)

    val redKlijenata = new ConcurrentLinkedQueue[Klijent]()
    val zaduzeniKlijenti = new ConcurrentLinkedQueue[Klijent]()

    while (sc.hasNext())
      redKlijenata.add(new Klijent(sc.next(), sc.nextInt()))

    for (i <- sluzbenice.indices)
      sluzbenice(i) = new Sluzbenice(kamata, kapital, redKlijenata, zaduzeniKlijenti)

    for (s <- sluzbenice)
      s.start()

    for (s <- sluzbenice)
      s.join()

    var ukZaduzenje: Float = 0f
    val it = zaduzeniKlijenti.iterator()
    while (it.hasNext)
      ukZaduzenje += it.next().getDug()

    println(s"Banka je zaradila ${ukZaduzenje - savedKapital}")
  }

}
