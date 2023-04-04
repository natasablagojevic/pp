import Data.Maybe

-- konstruktor kasnog tipa bez parametara
data StepenStudija = OsnovneStudije 
					| MasterStudije 
					| DoktorskeStudije
					deriving (Show, Eq)

data KratkiStepenStudija = Kratko StepenStudija

instance Show KratkiStepenStudija where
	show (Kratko OsnovneStudije) = "BSc"
	show (Kratko MasterStudije) = "MSc"
	show (Kratko DoktorskeStudije) = "PhD"

data Student = MkStudent {
	indeks:: String,
	ime:: String,
	prezime:: String,
	stepen:: StepenStudija
}

instance Show Student where
	show = formatirajStudenta

formatirajStudenta:: Student -> String
formatirajStudenta s = (indeks s) ++ " - " ++ (ime s) ++ "[" ++ (show (stepen s)) ++ "]"

-- MkStudent "11/2020" Petar Peric OsnovneStudije

instance Eq Student where
	s1 == s2 = (indeks s1) == (indeks s2)


type Rezultat = (Student, Maybe Int)

rezultat:: Student -> Int -> Rezultat
rezultat s p = (s, Just p)

initResults:: [Student]	-> [Rezultat]
initResults s = map (\t -> (t, Nothing)) s

ponistitiSve::	[Rezultat] -> [Rezultat]
ponistitiSve r = map (\t -> (fst r, Nothing))

ponistiStudenta:: [Rezultat] -> Student -> [Rezultat]
ponistiStudenta res s = foldr updateStudent [] res
	where updateStudent tmpS tmpR = if fst tmpS == s then (s, Nothing):tmpR else tmpS:tmpR

