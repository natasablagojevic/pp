import Data.Maybe
import Data.Either
import Data.List as List (elemIndex)

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

-- konstruktor sa argumentima
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
ponistitiSve r = map (\t -> (fst t, Nothing)) r

ponistiStudenta:: [Rezultat] -> Student -> [Rezultat]
ponistiStudenta res s = foldr updateStudent [] res
	where updateStudent tmpS tmpR = if fst tmpS == s then (s, Nothing):tmpR else tmpS:tmpR

-- MkStudent "123/2020" "Jovan" "Jovanovic" OsnovneStudije
-- MkStudent "123/2020" "Marko" "Maric" OsnovneStudije
-- MkStudent "1/2020" "Petar" "Peric" OsnovneStudije


poeni:: Student -> [Rezultat] -> Either String (Maybe Int)
poeni s results = 
	case idx of 
		Nothing -> Left (indeks s ++ " ne polaze PPI.")
		Just i -> Right (snd (results !! i))
	where idx = List.elemIndex s (map fst results)
