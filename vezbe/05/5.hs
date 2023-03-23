sqrtI:: Int -> Double
sqrtI x = sqrt (fromIntegral x)

printMax:: (Double, Double) -> Double
printMax p = max (fst p) (snd p)

-- zahteva dve kordinate
-- konkretniji zahtev
printMax':: (Double, Double) -> Double
printMax' (a, b) = max a b


(&&):: Bool -> Bool -> Bool
(&&) True True = True
(&&) _ _ = False
-- and True True = True
-- and False _ = False
-- and True False = False
