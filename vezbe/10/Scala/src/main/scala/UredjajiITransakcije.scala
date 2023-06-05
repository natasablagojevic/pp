import org.apache.spark.{SparkConf, SparkContext}

import java.io.{File, PrintWriter}

object UredjajiITransakcije {

 def main(args: Array[String]): Unit = {
   /** LOAD PATH FILE */
   val path: String = "/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/10/Scala/src/test/scala/uredjaji.txt"

   /** CONFIGURATE */
   val config: SparkConf = new SparkConf()
     .setAppName("Koliko se reci pojavljuje u knjizi")
     .setMaster("local[4]")
   val ctx: SparkContext = new SparkContext()

   /** MAIN */
   val dataRDD = ctx.textFile(path)
   dataRDD.map(l => {
     val lArray: Array[String]  = l.split(" ")
      (lArray[0], lArray.drop(1).mkString(" "))
   }).groupByKey()
     .foreach(t => {
       val f: PrintWriter = new PrintWriter(new File("/home/natasa/Desktop/Fakultet/6_sem/pp/vezbe/10/Scala/src/test/scala/" + t._1 + ".txt"))
       f.write("Marka: " + t._1 + ":\n")
       t._2.foreach(s => f.write("\t" + s + "\n"))
       f.close()
     })

   /** STOP */
   ctx.stop()

   /** RESULT */
 }
}
