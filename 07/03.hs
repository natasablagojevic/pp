import Data.Maybe
import Data.Either

glava:: [a] -> Maybe a 
glava [] = Nothing
glava (x:_) = Just x

glava':: [a] -> Either String a 
glava' [] = Left "Prazna lista"
glava' (x:_) = Right x