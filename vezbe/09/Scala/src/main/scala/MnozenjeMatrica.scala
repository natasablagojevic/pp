import java.io.{File, PrintWriter}
import java.util.Scanner

class Mnozilac(vrsta1: Array[Int], matrica2: Array[Array[Int]], rez: Array[Int]) extends Thread {
  override def run(): Unit = {
    for (j <- 0 until rez.length) {
      rez(j) = skalarniProizvod(j)
    }
  }

  def skalarniProizvod(j: Int): Int = {
    var suma = 0

    // vrsta1.length
    for (i <- vrsta1.indices) {
      suma += vrsta1(i) * matrica2(i)(j)
    }

    suma
  }
}

object MnozenjeMatrica {
  def main(args: Array[String]): Unit = {
    println("Konkuretno mnozenje matrica")

    val path1 = "/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/09/Scala/src/test/scala/matrica1.txt"
    val path2 = "/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/09/Scala/src/test/scala/matrica2.txt"
    val out_path = "/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/09/Scala/src/test/scala/matrica_out.txt"

    val sc1: Scanner = new Scanner(new File(path1))
    val sc2:Scanner = new Scanner(new File(path2))
    val pw: PrintWriter = new PrintWriter(new File(out_path))

    val n: Int = sc1.nextInt()
    val m1: Int = sc1.nextInt()

    val m2: Int = sc2.nextInt()
    val k: Int = sc2.nextInt()

    if (m1 != m2) {
      println("Greska! Matrice nisu odgovarajucih dimenizja!")
      return
    }

    val matrica1 = Array.ofDim[Int](n, m1)
    val matrica2 = Array.ofDim[Int](m2, k)
    val rez = Array.ofDim[Int](n, k)

    for (i <- 0 until n)
      for (j <- 0 until m1)
        matrica1(i)(j) = sc1.nextInt()

    for (i <- 0 until m2)
      for (j <- 0 until k)
        matrica2(i)(j) = sc2.nextInt()

//    for (i <- 0 until n) {
//      for (j <- 0 until m1)
//        print(matrica1(i)(j) + " ")
//      println()
//    }

    /** RACUNAJE MATRICE */

    val mnozioci = new Array[Mnozilac](n)

    for (i <- 0 until n) {
      mnozioci(i) = new Mnozilac(matrica1(i), matrica2, rez(i))
    }

    for (i <-  mnozioci.indices)
      mnozioci(i).start()

    for (i <- mnozioci.indices)
      mnozioci(i).join()

    for (i <- 0 until n) {
      for (j <- 0 until m1)
        print(rez(i)(j) + " ")
      println()
    }
  }

}
