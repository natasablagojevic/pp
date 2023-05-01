import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

object ParniKvadrati {
  def main(args: Array[String]): Unit = {

    /** SETUP - mora na ispitu */
    val config: SparkConf = new SparkConf()
      .setAppName("ParniKvadrati")
      .setMaster("local[4]")
    val ctx: SparkContext = new SparkContext()

    // main
    println("Unesite broj n: ")
    val n: Int = Console.readInt()
    val data: Array[Int] = (2 to n by 2).toArray
    val dataRDT: RDD[Int] = ctx.parallelize(data)

    val dataProcessed: Array[Int] = dataRDT.map(e => e*e).collect()

    ctx.stop()

    println("Elementi: ")
    println(dataProcessed.mkString(", "))

  }
}