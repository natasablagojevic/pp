import Data.Maybe
import Data.Either
import Data.List as List (elemIndex,  sortBy)


data StepenStudija = OsnovneStudije
                   | MasterStudije
                   | DoktorskeStudije
                   deriving Eq

instance Show StepenStudija where
    show OsnovneStudije = "BSc"
    show MasterStudije = "MSc"
    show DoktorskeStudije = "PhD"

data Student = MkStudent {
    indeks:: String,
    ime:: String,
    prezime:: String,
    stepen:: StepenStudija
}

instance Eq Student where
    (==) s1 s2 = (indeks s1) == (indeks s2)

instance Show Student where
    show = showUtil

showUtil:: Student -> String
showUtil s = id ++ ": " ++ ip ++ " - " ++ ss
    where id = (indeks s)
          ip = (ime s) ++ " " ++ (prezime s)
          ss = show (stepen s)

type Rezultat = (Student, Maybe Integer)

formiraj:: [Student] -> [Rezultat]
formiraj = map (\s -> (s, Nothing))

ponistiSve:: [Rezultat] -> [Rezultat]
ponistiSve = map (\t -> (fst t, Nothing))

ponistiSingle:: Student -> [Rezultat] -> [Rezultat]
ponistiSingle student = foldr azuriraj []
    where azuriraj elem l = if (fst elem ) == student then (student, Nothing) : l else elem : l

stepena:: StepenStudija -> [Rezultat] -> [Rezultat]
stepena ss = filter (\(s, _) -> (stepen s) == ss)

polozeni:: [Rezultat] -> [Rezultat]
polozeni = filter (\(_,p) -> (parsiraj p) >= 51)
    where parsiraj Nothing = 0
          parsiraj (Just broj) = broj

poeni:: Student -> [Rezultat] -> Either String (Maybe Integer)
poeni s rez = 
    case idx of 
        Nothing -> Left ("Nema studenta u listi")
        (Just i) -> Right (snd (rez !! i))
    where idx = elemIndex s (map (fst) rez)

-- #TODO
-- #DEBUGG
upisi:: Student -> Int -> [Rezultat] -> [Rezultat]
upisi s p rez = 
    if elem s (map (fst) rez) 
        then foldr azuriraj [] rez  
    else (s, Just p) : rez
    where azuriraj elem l = if (fst elem) == s then (s, Just p):l 
                            else elem:l

najbolji:: Int -> [Rezultat] -> [Int]
najbolji n rez = take n (sortBy (flip compare) (map (\(Just p) -> p) (filter (Nothing /= ) (map snd rez))))

-- test 
s1 = MkStudent "41/2014" "Pera" "Peric" OsnovneStudije
s2 = MkStudent "31/2015" "Ana" "Anic" OsnovneStudije
s3 = MkStudent "23/2020" "Nikola" "Nikolic" MasterStudije
s4 = MkStudent "11/2020" "Ivana" "Ivanic" DoktorskeStudije
s5 = MkStudent "44/2020" "Jelena" "Jelenic" OsnovneStudije

stud = [s1, s2, s3, s4, s5]
rez = [(s1, Just 94), (s2, Just 43), (s3, Nothing), (s4, Just 95),(s5, Just 100)]

