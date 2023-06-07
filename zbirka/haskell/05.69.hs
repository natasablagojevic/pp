import Language.Haskell.TH.Lib (derivClause)
import Data.Maybe
import Data.Char 

-- 05.69.hs

-- data ParRazlicitih = MkPar {
--     a:: Int,
--     b:: Int
-- }

-- 05.70.hs 

data Krug = MkKrug {
        radius:: Float
    }
    deriving (Show, Eq) 

data Pravougaonik = MkPravougaonik {
        a:: Float,
        b:: Float 
    }
    deriving (Show, Eq)

-- 05.71.hs 

    -- C - pocetak akko se sastoji samo od cifara 
    -- S - pocetak akko se sastoji samo od malih slova 
    -- O - pocetak inace

-- broj [] = Nothing 
broj :: Foldable t => t Char -> Bool
broj lst = all (isDigit) lst 

mala :: Foldable t => t Char -> Bool
mala lst = all (isLower) lst 

sifruj ls = map (\t ->  if (broj t) then "C" ++ t ++ "C"
                        else (
                            if (mala t) then "M" ++ t ++ "M"
                            else "O" ++ t ++ "O"
                        )) ls 