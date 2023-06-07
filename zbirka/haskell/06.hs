-- parMax p
parMax:: (Double, Double) -> Double 
parMax p = 
    if fst p > snd p then fst p 
    else snd p

parMax':: (Double, Double) -> Double
parMax' (x, y) = 
    if x > y then x
    else y 

parMax'':: (Double, Double) -> Double 
parMax'' p 
    | fst p > snd p = fst p 
    | otherwise = snd p