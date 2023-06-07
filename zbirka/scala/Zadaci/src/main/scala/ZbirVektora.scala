import java.util.Scanner
import scala.Array.ofDim

class Saberi(v1: Array[Int], v2: Array[Int], res: Array[Int], start: Int, end: Int) extends Thread {
  override def run(): Unit = {
    for (i <- start until end)
      res(i) = v1(i) + v2(i)
  }
}

object ZbirVektora {
  def main(args: Array[String]): Unit = {

    val sc: Scanner = new Scanner(System.in)

    println("Unesite dimenziju vektora: ")
    val n = sc.nextInt()

    println("Unesite vektor 1: ")
    val v1 = ofDim[Int](n)
    for (i <- 0 until n)
      v1(i) = sc.nextInt()

    println("Unesite vektor 2: ")
    val v2 = ofDim[Int](n)
    for (i <- 0 until n) {
      v2(i) = sc.nextInt()
    }

    var res = ofDim[Int](n)

    val tids = new Saberi(v1, v2, res, 0, n)

    tids.start()

    tids.join()


    /** Stampanje rezultata */
    for (i <- 0 until n)
      print(res(i) + " ")
    println()

  }
}
