ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.13.10"

lazy val root = (project in file("."))
  .settings(
    name := "Scala"
  )

// https://mvnrepository.com/artifact/org.apache.spark/spark-core
libraryDependencies += "org.apache.spark" %% "spark-core" % "3.4.0"

//libraryDependencies ++= {
//  val sparkVer = "2.4.0"
//  Seq(
//    "org.apache.spark" %% "spark-core" % sparkVer
//  )
//}