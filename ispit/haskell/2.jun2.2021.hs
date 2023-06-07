data Poklapanje = MkPoklapanje {
    kar:: Char,
    poz:: Int
    }
    -- deriving Show
    
instance Show Poklapanje where 
    show (MkPoklapanje k p) = "Karakter: " ++ show k ++ ", na poziciji: " ++  show p 

getKar:: Poklapanje -> Char 
getKar p = kar p 

getPoz:: Poklapanje -> Int 
getPoz p = poz p 

poklapanjeShow:: Poklapanje -> String 
poklapanjeShow (MkPoklapanje k p) = (show k) ++ " ( " ++ (show p) ++ " ) "

poklapanjeM:: Int -> String -> Maybe Poklapanje
-- poklapanjeM i [] = Nothing
poklapanjeM i str = 
    if i >= 0 && i < length str then Just (MkPoklapanje (str !! i) i )
    else Nothing

poklapanjeE:: Int -> String -> Either String Poklapanje 
poklapanjeE i str 
    | i < 0 || i >= length str = Left "Index error"
    | otherwise = Right (MkPoklapanje (str !! i) i)

pronadjiM:: Poklapanje -> String -> Maybe Bool 
pronadjiM p str 
    | pozicija < 0 || pozicija >= length str = Nothing 
    | otherwise = Just (kar p == str !! pozicija)
    where pozicija = poz p

pronadjiE:: Poklapanje -> String -> Either String Bool 
pronadjiE p str 
    | pozicija < 0 || pozicija >= length str = Left "Index error"
    | otherwise = Right (karakter == str !! pozicija)
    where
        pozicija = poz p
        karakter = kar p