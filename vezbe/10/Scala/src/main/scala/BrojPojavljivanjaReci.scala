import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}
//import org.apache.spark.sql.SparkConf
object BrojPojavljivanjaReci {
  def main(args: Array[String]): Unit = {

    val path: String = "/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/10/Scala/src/test/scala/knjiga.txt"

    /** CONFIGURATE */
    val config: SparkConf = new SparkConf()
      .setAppName("Koliko se reci pojavljuje u knjizi")
      .setMaster("local[4]")
    val ctx: SparkContext = new SparkContext()

    /** MAIN */
    val dataRDD: RDD[String] = ctx.textFile(path)
      .flatMap(l => l.split(" "))
      .filter(l => l.length > 0)
      .map(s => {
        var sout: String = s
        if (s.endsWith("\"")) {
          sout = s.substring(0, s.length-1)
        }
        if (s.startsWith("\"")) {
          sout = s.substring(1)
        }

        sout
      })
      .map(e => (e, 1))
      .reduceByKey((a, b) => a+b)
      .sortByKey()
//      .saveAsTextFile("/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/10/Scala/src/test/scala/knjiga_result.txt")


    /** END */
    ctx.stop()

    /** PRINT RESULT */

  }
}
