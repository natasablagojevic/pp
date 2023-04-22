import java.io.File
import java.util.Scanner
import java.util.concurrent.{ConcurrentLinkedQueue, ThreadLocalRandom}
import java.util.concurrent.atomic.AtomicLong

class Sluzbenica(id: Int,
                 kapital: AtomicLong, kamata: Int, klijenti: ConcurrentLinkedQueue[Klijent],
                 duznici: ConcurrentLinkedQueue[Klijent]) extends Thread {
  override def run(): Unit = {
    val klijent = klijenti.poll()
    if (klijent == null) {
      println(s"Sluzbenica $id zavrsila smenu")
    }

    println(s"${klijent.getIme} na salteru broj $id")

    kapital.synchronized {
      if (klijent.getPozajmica < kapital.get()) {
        /** RAZGOVOR NA SALTERU */
        Thread.sleep(ThreadLocalRandom.current().nextInt(1, 10) * 1000)

        /** AZURIRAJ DUG */
        klijent.setDug(klijent.getPozajmica * (100f + kamata) / 100f)

        /** AZURIRAJ KAPITAL */
        kapital.synchronized {
          val noviKapital = kapital.get() - klijent.getPozajmica
          kapital.set(noviKapital)
        }

        /** ODOBRI POZAJMICU */
        println(s"Klijentu ${klijent.getIme} ODOBRENA je pozajmica od ${klijent.getPozajmica} eur")
        println(s"Zarada banke na ovom klijentu bice: ${klijent.getDug - klijent.getPozajmica} eur")
        duznici.add(klijent)

      }
    }

  }
}

class Klijent(ime: String, pozajmica: Int) {
  var dug: Float = 0
  def getIme: String = ime
  def getPozajmica: Int = pozajmica
  def getDug: Float = dug
  def setDug(novDug: Float): Unit = {
    dug = novDug
  }
}
object Krediti {
  def main(args: Array[String]): Unit = {
    println("--- Banka ---")

    /** UCITAVANJE PODATAKA */
    val sc = new Scanner(System.in)
    println("Unesite kapital, kamatnu stopu, i broj sluzbenica redom: ")
    val kapital = new AtomicLong(sc.nextInt())
    val kamata = sc.nextInt()
    val n = sc.nextInt()

    /** UCITAVANJE KLIJENATA */
    val klijenti_path = "/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/09/Scala/src/test/scala/klijenti.data"
    val sck = new Scanner(new File(klijenti_path))
    val klijenti = new ConcurrentLinkedQueue[Klijent]()

    while (sck.hasNextLine()) {
      klijenti.add(new Klijent(sck.next(), sck.nextInt()))
    }

    /** SLUZBENICE */
    val sluzbenice = new Array[Sluzbenica](n)
    val duznici = new ConcurrentLinkedQueue[Klijent]()
    for (i <- sluzbenice.indices) {
      sluzbenice(i) = new Sluzbenica(i, kapital, kamata, klijenti, duznici)
    }

    /** RAD BANKE */
    for (s <- sluzbenice)
      s.start()

    for (s <- sluzbenice)
      s.join()

    /** DOBIT */
    var noviKapital: Float = kapital.get()
    val iter = duznici.iterator()
    while (iter.hasNext) {
      noviKapital += iter.next().getDug
    }

    println(s"Status banke: $noviKapital")



  }
}

/*
  KLADIONICA
  I)
  for (k <- kladionicari)
    k.start( )

  II)
  sleep(100)
  rezultat.get

  III)
//  sve niti koje cekaju na utakmice oslobodi dalje
  utakmice.notifyAll()

  IV)
  for (k <- kladionicar)
    k.join( )

  KLADIONICAR
  I)
  ...
  utakmice.wait()
  ...



*/
