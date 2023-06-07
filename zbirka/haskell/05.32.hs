import Text.XHtml (p)
type Tacka = (Float, Float)

type Putanja = [Tacka]

tacka:: Float -> Float -> Tacka
tacka x y = (x, y)

o:: Tacka
o = (0.0, 0.0)

getX:: Tacka -> Float
getX = fst

getY:: Tacka -> Float
getY = snd

duzinaPutanje :: Foldable t => t a -> Int
duzinaPutanje = length

translirajTacku :: (Float, Float) -> Float -> Float -> Tacka
translirajTacku (x, y) dx dy = tacka (x+dx) (y+dy)

rastojanje :: Floating a => (a, a) -> (a, a) -> a
rastojanje (x1, y1) (x2, y2) = sqrt ((x1 - x2)^2 + (y1 - y2)^2)

rastojanje' :: Tacka -> Tacka -> Float
rastojanje' t1 t2 = sqrt $ ((getX t1) - (getX t2))^2 + ((getY t1) - (getY t2))^2

uKrugu :: Float -> [Tacka] -> [Tacka]
uKrugu r lista = [t | t <- lista, rastojanje' o t <= r]

translirajPutanje :: [(Float, Float)] -> Float -> Float -> [Tacka]
translirajPutanje p dx dy = [translirajTacku t dx dy | t <- p]

nadovezi :: Tacka -> Putanja -> Putanja
nadovezi t p = (++) p [t]

spojiPutanje :: Putanja -> Putanja -> Putanja
spojiPutanje = (++)

centroid :: [Tacka] -> Tacka
centroid ts = tacka prosekX prosekY
    where prosekX = prosek $ map fst ts 
          prosekY = prosek $ map snd ts 
          prosek lst = (sum lst) / (fromIntegral $ length lst)

kvadrantTacke :: Tacka -> Int 
kvadrantTacke (x, y)
    | x > 0 && y > 0 = 1 
    | x < 0 && y > 0 = 2
    | x < 0 && y < 0 = 3 
    | x > 0 && y < 0 = 4
    | otherwise = 0

tackeUKvadrantu :: Int -> [Tacka] -> [Tacka]
tackeUKvadrantu kv p = [t| t <- p, kvadrantTacke t == kv] 

tackeVanKvandrata :: t -> [Tacka] -> [Tacka]
tackeVanKvandrata kv p = [t | t <- p, kvadrantTacke t /= kv]

maximumi :: [Tacka] -> Tacka
maximumi lst = (maksimum $ map fst lst, maksimum $ map snd lst)
    where maksimum (x:xs) = foldl (\acc e -> if e > acc then e else acc) x xs 