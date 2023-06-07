
class Covek(ime: String, prezime: String, godine: Int) {
  def getIme(): String = this.ime

  def getPrezime(): String = this.prezime

  def getGodine(): Int = this.godine

  override def toString: String = "Ja sam " + this.ime + " " + this.prezime
}

object HelloWorld {
  def main(args: Array[String]): Unit = {
    println("Hello World!")

    val c1 = new Covek("Marko", "Maric", 25)
    println(c1)
    print(c1.getIme())
  }
}
