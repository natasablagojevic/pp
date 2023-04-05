import Data.Maybe
import Data.Either
-- data Maybe a = Nothing | Justa a

glava:: [a] -> Maybe a
glava [] = Nothing
-- glava l = Just (head l)
glava (x:_) = Just x

rep:: [a] -> Maybe [a]
rep [] = Nothing
rep (_:xs) = Just xs

-- -------------------------------------
-- prosirenje tipa + nothing
-- data Either a b = Left a | Right b

glava':: [a] -> Either String a
glava' [] =  Left "Lista je prazna. Glava liste nije definisana"
glava' (x:_) = Right x

rep':: [a] -> Either String [a]
rep' [] = Left "Lista je prazna. Rep liste nije definisan"
rep' (_:xs) = Right xs
