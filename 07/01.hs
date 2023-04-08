-- Primer 1
data BulovskiTip = Tacno | Netacno 

-- Primer 2
data Oblik = Kvadrat Float 
            | Pravougaonik Float Float 
            | Krug Float 
            | Trougao Float Float Float 
            deriving Show 

-- Primer 3
data Ljubimac = MkLjubimac {
    -- getteri = implicitna definicija gettera
    ime:: String, 
    godine:: Int
} deriving Show

-- Primer 4
data Zivotinja = Pas | Macka | Papagaj deriving Eq
data LjubimacAdv = MkLjubimacAdv {
    -- redefinicija argumenata
    -- ne smemo da imamo iste nazive
    imeAdv:: String, 
    godineAdv:: Int,
    tip:: Zivotinja
}

-- Primer 4
data Paralelogram = MkParalelogram {
    a:: Int,
    b:: Int
} 
-- deriving Show

instance Show Paralelogram where 
    show p = "Paralelogram sa stranicama: " ++ (show (a p)) ++ " i " ++ (show (b p))

instance Eq Paralelogram where 
    (==) p1 p2 = (a p1) == (a p2) && (b p1) == (b p2)