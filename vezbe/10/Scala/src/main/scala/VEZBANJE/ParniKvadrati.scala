package VEZBANJE

import org.apache.spark.{SparkConf, SparkContext}

import java.util.Scanner

object ParniKvadrati {
  def main(args: Array[String]): Unit = {

    val conf = new SparkConf()
      .setAppName("Parni Kvadrati")
      .setMaster("local[4]")
    val sk = new SparkContext(config = conf)

    /** MAIN */
    val sc: Scanner = new Scanner(System.in)
    val n = sc.nextInt()
    val niz = (2 to n by 2).toArray

    val nizRDD = sk.parallelize(niz)
    val kniz = nizRDD.map(t => t*t)
      .collect()

  /** KRAJ */
    sk.stop()

    /** REZULTAT */
    for (e <- kniz)
      print(e + " ")
    println()
  }
}
