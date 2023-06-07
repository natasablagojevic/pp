pozicije :: Eq a => a -> [a] -> [Int]
pozicije x [] = []
pozicije x l = [i | (x1, i) <- zip l [0..n], x == x1]
    where n = length l

-- 05.62.hs 

qsort :: Ord a => [a] -> [a]
qsort [] = []
qsort (x:xs) = qsort smallSort ++ middleSort ++ qsort bigSort
    where smallSort = [a | a <- xs, a < x]
          middleSort = [a | a <- xs, a == x] ++ [x]
          bigSort = [a | a <- xs, a > x]

-- 05.63.hs 

brisiPonavljanja [] = []
brisiPonavljanja (x:xs) = x : brisiPonavljanja(dropWhile (==x) xs) 

-- 05.64.hs 

istiArtikli :: Eq a => [a] -> [[a]]
istiArtikli [] = []
istiArtikli (x:xs) = (x : (takeWhile (==x) xs)) : istiArtikli(dropWhile (==x) xs) 

-- 05.65.hs 

broj [] = 0
broj (x:xs) = x * 10^(length xs) + broj xs  

obrniBroj [] = 0
obrniBroj (x:xs) = (obrniBroj xs)*10 + x 

-- 05.66.hs 

parovi [] = ([],[])
parovi lst = foldr (\(a,b) (c,d) -> (a:c, b:d)) ([],[]) lst