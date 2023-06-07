import Data.Maybe
import Data.Either 

-- 05.56.hs

glava:: [a] -> Maybe a
glava [] = Nothing 
glava (x:_) = Just x 

rep:: [a] -> Maybe [a] 
rep [] = Nothing 
rep (_:xs) = Just xs 

-- 05.57.hs 
glava':: [a] -> Either String a  
glava' [] = Left "Prazna lista"
glava' (x:_) = Right x

rep':: [a] -> Either String [a]
rep' [] = Left "Prazna lista"
rep' (_:xs) = Right xs

