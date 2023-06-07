type Stek a = [a]

push:: Stek a -> a -> Stek a
push s x = x : s 

top:: Stek a -> Maybe a 
top (x:_) = Just x
top [] = Nothing 

pop:: Stek a -> (Maybe a, Stek a)
pop (x:xs) = (Just x, xs)
pop [] = (Nothing, []) 

-- ne radi zastooo??
stekMap:: Stek a -> (a -> b) -> Stek b
stekMap s f = map f s  

-- ne radii zastooo???
poredi:: Stek a -> Stek a 
poredi s = [x | (i, x) <- zip [0..] s, even i]