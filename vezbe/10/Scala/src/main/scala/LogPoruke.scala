//import org.apache.spark.rdd.RDD
//import org.apache.spark.{SparkConf, SparkContext}
//
//object LogPoruke {
//  def main(args: Array[String]): Unit = {
//    val path: String = "/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/10/Scala/src/test/scala/log.txt"
//
//    /** CONFIGURATE */
//    val config: SparkConf = new SparkConf()
//      .setAppName("Log Poruka")
//      .setMaster("local[4]")
//    val ctx: SparkContext = new SparkContext()
//
//    /** MAIN */
//    val dataRDD: RDD[String] = ctx.textFile(path)
//    val outData = dataRDD.filter(l => l.startsWith("[WARN]") || l.startsWith("[INFO]") || l.startsWith("[ERROR]"))
//      .map(l => {
//        val lData: Array[String] = l.split(" ")
//        (lData(0), lData.drop(1).mkString(" "))
//      }).groupByKey()
//      .map(t => (t._1, t._2.size))
//      .collect()
//
//    /** ENDDING CONTEXT */
//    ctx.stop()
//
//    /** RESULT */
//    println(outData.mkString("\n"))
//  }
//}
