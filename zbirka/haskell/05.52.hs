import Distribution.Backpack.PreModuleShape (PreModuleShape)
-- 05.52.hs 

-- Tacno i Netacno su samo konstruktori
data BulovskiTip = Tacno | Netacno 

-- 05.53.hs 

data Oblik = Kvadrat Float 
    | Pravougaonik Float Float 
    | Krug Float 
    | Trougao Float Float Float 
    deriving Show 

-- 05.54.hs 

data Zivotinja = Pas | Macka | Papagaj 

data Ljubimac = MkLjubimac {
    ime:: String, 
    godine:: Int, 
    tip:: Zivotinja
    }

-- 05.55.hs 

data Pravougaonik1 = MkPravougaonik1 {
    a:: Int,
    b:: Int
}

instance Show Pravougaonik1 where 
    show (MkPravougaonik1 a b) = "(" ++ show a ++ "," ++ show b ++ ")" 

instance Eq Pravougaonik1 where 
    (==) (MkPravougaonik1 a1 b1) (MkPravougaonik1 a2 b2) = 
        (a1 == a2 && b1 == b2) || (a1 == b2 && b1 == a2)

