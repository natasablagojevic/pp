import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

object PetocifreniBrojevi1 {
 def main(args: Array[String]): Unit = {
   val path: String = "/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/10/Scala/src/test/scala/brojevi.txt"

   val config: SparkConf = new SparkConf()
     .setAppName("Petocifreni Brojevi")
     .setMaster("local[4]")
   val ctx: SparkContext = new SparkContext()

   /** MAIN */
   val dataRDD: RDD[String] = ctx.textFile(path)
   val n: Long = dataRDD.filter(l => l.length == 5).count()

   ctx.stop()

   /** ISPIS REZULTATA */
   println(s"Broj petocifrenih brojeva je $n")
 }
}
