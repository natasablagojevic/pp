import java.io.File
import java.util.Scanner

object MnozenjeMatrica {
  def main(args: Array[String]): Unit = {
    println("Paralelno mnozenje matrica")

    // 1. ucitavanje podataka
    val sc1: Scanner = new Scanner(new File("/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/08/Scala/src/main/scala/matrica1.txt"))
    val sc2: Scanner = new Scanner(new File("/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/08/Scala/src/main/scala/matrica2.txt"))

    val n:Int = sc1.nextInt()
    val m1:Int = sc1.nextInt()
    val m2:Int = sc2.nextInt()
    val k: Int = sc2.nextInt()

    if (m1 != m2)
      throw new RuntimeException("matrica nije validnih dimenzija")

    val matrica1: Array[Array[Int]] = Array.ofDim[Int](n, m1)
    val matrica2: Array[Array[Int]] = Array.ofDim[Int](m2, k)

    for (i <- 0 until n) {
      for (j <- 0 until m1)
        matrica1(i)(j) = sc1.nextInt()
    }

    for (i <- 0 until m2) {
      for (j <- 0 until k)
        matrica2(i)(j) = sc2.nextInt()
    }

    // 3. Mnozenje
    val rezultat: Array[Array[Int]] = Array.ofDim(n, k)
    val mnozioci: Array[Mnozilac] = new Array[Mnozilac](n)

    for (i <- 0 until n) {
      mnozioci(i) = new Mnozilac(matrica1(1), matrica2, rezultat(i))
    }

    // pthread_create
    for (i <- 0 until n)
      mnozioci(i).start()

    // pthread_join
    for (i <- 0 until n)
      mnozioci(i).join()

    for (i <- 0 until n) {
      for (j <- 0 until k)
        print(rezultat(i)(j) + " ")

      println()
    }
  }
}
class Mnozilac(vrsta: Array[Int], matrica2: Array[Array[Int]], vrstaR: Array[Int]) extends Thread{
  /** Kreiranje niti **/
  override def run(): Unit = {
    for (i <- vrstaR.indices)
      vrstaR(i) = sp(i)
  }

  /** Skalarni proizvod **/
  def sp(i: Int): Int = {
    var rez: Int = 0
    for (j <- vrsta.indices)
      rez += vrsta(j) * matrica2(j)(i)

    return rez
  }
}