-- interfejs, template
-- qsort :: Ord a => [a] -> [a]
-- qsort lst = (qsort manji) ++ (qsort veci)
	-- -- let p = head lst in ...
	-- where p = head lst
		-- manji = [e | e <- lst, e < p]
		-- veci = [e | e <- lst, e >= p]

-- zip = velicina najmanje liste
 
qsort' :: Ord a => [a] -> [a]
qsort' [] = []
qsort' lst@(p:xs) = (qsort' manji) ++ (qsort' veci)
	where 
		manji = [e | e <- lst, e < p]
		veci = [e | e <- lst, e >= p]

-- lambda funkcije
-- takeWhile (\x x-> x < 3) [1..10]

-- uklanja sa pocetka dokle god vazi uslov
-- dropWhile uslov lista
-- dropWhile (<3) [1..10]

-- uzima elemente dokle god vazi uslov
-- takeWhile uslov lista
-- takeWhile (<3) [1..10]

-- Foldable - kolekcija

-- proverava da li je lista prazna
-- null list
