import java.io.File
import java.util.Scanner
import scala.Array.ofDim

class Mnozilac(vrsta1: Array[Int], mat2: Array[Array[Int]], res: Array[Int]) extends Thread {

  var k: Int = mat2.length * mat2(1).length / vrsta1.length
  var m: Int = vrsta1.length
  override def run(): Unit = {
    for (i <- 0 until k)
      res(i) = skProizvod(i)
  }

  def skProizvod(j: Int): Int = {
    var sum = 0;
    for (i <- 0 until m)
      sum += vrsta1(i) * mat2(i)(j)

    sum
  }
}

object MnozenjeMatrica {
  def main(args: Array[String]): Unit = {
    val m1_path = "/home/natasa/Desktop/Fakultet/6_sem/pp/zbirka/scala/Zadaci/src/test/scala/matrica1.txt"
    val m2_path = "/home/natasa/Desktop/Fakultet/6_sem/pp/zbirka/scala/Zadaci/src/test/scala/matrica2.txt"

    val sc1: Scanner = new Scanner(new File(m1_path))
    val sc2: Scanner = new Scanner(new File(m2_path))

    val n = sc1.nextInt()
    val m1 = sc1.nextInt()

    val m2 = sc2.nextInt()
    val k = sc2.nextInt()

    if (m1 != m2) {
      println("Greska! Ne mozemo pomnoziti matrice!")
      return ;
    }

    val mat1 = ofDim[Int](n, m1)
    val mat2 = ofDim[Int](m2, k)
    val res = ofDim[Int](n, k)

    for (i <- 0 until n)
      for (j <- 0 until m1)
        mat1(i)(j) = sc1.nextInt()

    for (i <- 0 until m2)
      for (j <- 0 until k)
        mat2(i)(j) = sc2.nextInt()

    val mnozioci = new Array[Mnozilac](n)

    for (i <- 0 until n)
      mnozioci(i) = new Mnozilac(mat1(i), mat2, res(i))

    for (i <- 0 until n)
      mnozioci(i).start()

    for (i <- 0 until n)
      mnozioci(i).join()

    println("Rezultat:")
    for (i <- 0 until n) {
      for (j <- 0 until k)
        print(res(i)(j) + " ")
      println()
    }
  }
}
