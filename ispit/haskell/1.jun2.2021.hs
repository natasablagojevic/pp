import Data.Char

najduza:: [String] -> String 
najduza lst = snd $ maximum $ [(length t, t) | t <- lst]

umanji:: String -> String 
umanji str = map (toLower) str 

-- razdvoj _ [] = []
-- razdvoj sep str = razdvajanje str []
--     where razdvajanje [] acc = [revrse acc]
--           razdvajanje (x:xs) acc =
--           if x == sep then reverse acc : razdvajanje xs []
--           else razdvajanje xs (x:acc)


razdvoj :: Char -> String -> [String]
razdvoj _ [] = []
razdvoj sep str = go str []
  where
    go [] acc = [reverse acc]
    go (x:xs) acc
      | x == sep = reverse acc : go xs []
      | otherwise = go xs (x:acc)

spoj:: String -> [String] -> String
spoj _ [] = []
spoj _ [x] = x
spoj sep (x:xs) = x ++ sep ++ spoj sep xs