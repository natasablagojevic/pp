sumaPrvih :: Int -> Int
sumaPrvih n = 
	if n == 0 then 0 
	else n + sumaPrvih (n-1)

-- cuvari - 'gards'
sumaPrvih' :: Int -> Int 
sumaPrvih' n
	| n == 0 = 0
	| otherwise = n + sumaPrvih' (n-1)


-- Poklapanje obrazaca - Pattern matching
sumaPrvih'':: Int -> Int 
sumaPrvih'' 0 = 0
sumaPrvih'' n = n + sumaPrvih'' (n-1)

sumaPrvih''':: Int -> Int
sumaPrvih''' n = sum [1..n]
