import org.apache.spark.SparkContext

object SkalarniProizvod {
  def main(args: Array[String]): Unit = {

    val path1: String = "jashf"
    val path2: String = "kjf"

    /** CONFIGURATE */
    val config: SparkConfig = new SparkConf()
      .setAppName("Skalarni Proizvod")
      .setMaster("local[4]")
    val ctx: SparkContext = new SparkContext()

    /** MAIN */
    val v1 = ctx.textFile(path1).flatMap(l => l.split(", ")).map(e => e.toInt).repartiton(3)
    val v2 = ctx.textFile(path1).flatMap(l => l.split(", ")).map(e => e.toInt).repartition(3)

    val sp: Int = v1.zip(v2).map(p => p._1 * p._2).reduce((a, b) => a + b)

    ctx.stop()

    println(s"Skalarni proizvod je: $sp")
  }
}
