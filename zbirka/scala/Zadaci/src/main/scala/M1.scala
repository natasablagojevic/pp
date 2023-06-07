import java.io.File
import java.util.Scanner
import scala.Array.ofDim

class Mnozenje(vrsta1: Array[Int], mat2: Array[Array[Int]], res: Array[Int], m: Int, k: Int) extends Thread {
  override def run(): Unit = {
   for (i <- 0 until k)
    res(i) = skalarnoMnozenje(i)
  }

  def skalarnoMnozenje(j: Int): Int = {
    var sum = 0
    for (i <- 0 until m)
      sum += vrsta1(i) * mat2(i)(j)

    sum
  }
}

object M1 {
  def main(args: Array[String]): Unit = {
    val path1 = "/home/natasa/Desktop/Fakultet/6_sem/pp/zbirka/scala/Zadaci/src/test/scala/matrica1.txt"
    val path2 = "/home/natasa/Desktop/Fakultet/6_sem/pp/zbirka/scala/Zadaci/src/test/scala/matrica2.txt"

    val sc1: Scanner = new Scanner(new File(path1))
    val sc2: Scanner = new Scanner(new File(path2))

    val n: Int = sc1.nextInt()
    val m1: Int = sc1.nextInt()
    val m2: Int = sc2.nextInt()
    val k: Int = sc2.nextInt()

    val mat1 = ofDim[Int](n, m1)
    val mat2 = ofDim[Int](m2, k)
    val res = ofDim[Int](n, k)

    /** Ucitavanje mat1 */
    for (i <- 0 until n)
      for (j <- 0 until m1)
        mat1(i)(j) = sc1.nextInt()

    /** Ucitavanje mat2 */
    for (i <- 0 until m2)
      for (j <- 0 until k)
        mat2(i)(j) = sc2.nextInt()

    var mnozenje = new Array[Mnozenje](n)
    for (i <- 0 until n)
      mnozenje(i) = new Mnozenje(mat1(i), mat2, res(i), m1, k)

    for (i <- 0 until n)
      mnozenje(i).start()

    for (i <- 0 until n)
      mnozenje(i).join()

    /** Ispisivanje rezultata */
    for (i <- 0 until n) {
      for (j <- 0 until k)
        print(res(i)(j) + " ")
      println()
    }

  }
}
