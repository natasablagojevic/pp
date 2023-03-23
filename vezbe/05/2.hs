{-
	Osnovni tipovi:
	- Bool 
	- Int
	- Integer
	- Float
	- Double
	- Char
	- String

	Tipski razredi:
	- EQ 			(==, !=)
	- ORD 			(>, >=, < , <=)
	- NUM			(+, -, *)
	- INTEGRAL		(mod, div)
	- FRACTIONAL	(/, recip)
-}

-- dupliraj :: Num t => t -> t
dupliraj x = 2*x

-- dupliraj' :: Num t => t -> t
dupliraj' x = (*) 2 x

-- mod3 :: Integral t => t -> t
mod3 x = x `mod` 3

-- mod3 :: Integral t => t -> t
mod3' x = mod x 3

dupliraj'' = (*) 2
dupliraj''' = (*2)

minus2 x = x - 2
-- minus2':: Num a => a -> a
minus2' x = (-) x 2

-- zbog 2 je integer
-- minus2'':: Integer -> Integer
minus2'':: Num a => a -> a
minus2'' = (-) 2


minus2''' = (-2)
