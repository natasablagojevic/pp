import Data.Maybe 
import Data.Either 
import qualified Data.ByteString as List

data StepenStudija = Osnovne 
                    | Master 
                    | Doktorske
                    deriving (Show, Eq)  

data Student = MkStudent {
    indeks:: String,
    ime:: String,
    prezime:: String,
    stepen:: StepenStudija 
    }

data Rezultat = MkRezultat {
    brojPoena:: Maybe Int 
}


instance Show Student where
    show (MkStudent idx i p s) = i ++ " " ++ p ++ " broj indeksa: " ++ idx  

instance Eq Student where 
    (==) (MkStudent idx1 i1 p1 s1) (MkStudent idx2 i2 p2 s2) = 
        idx1 == idx2 




s1 = MkStudent "159/2020" "Natasa" "Blagojevic" Osnovne
s2 = MkStudent "160/2019" "Milica" "Vasic" Osnovne
s3 = MkStudent "123/2022" "Dejana" "Lukic" Osnovne
s4 = MkStudent "143/2022" "Jakov" "Peric" Master
s5 = MkStudent "168/2020" "Andjelina" "Josic" Master 
s6 = MkStudent "384/2023" "Strahinja" "Pantic" Doktorske

students = [s1, s2, s3, s4, s5, s6]

-- rezultati studenti = [(indeks x, 0) | x <- studenti]
rezultati :: [Student] -> [(Student, Maybe a)]
rezultati studenti = [(x, Nothing) | x <- studenti]

poeni s r = 
    case mi of Nothing -> Left $ (indeks s) ++ "Ne studira na fakultetu"
               (Just i) -> Right $ snd $ r !! i 
    where mi = List.elemIndex s $ map fst r 