import Data.List

presek:: Eq a => [a] -> [a] -> [a]
presek lst1 lst2 = nub(filter (`elem` lst2) lst1)

maxl:: Ord a => [a] -> a
maxl lst = maximum lst

ind:: Eq a => a -> [a] -> Int
ind x lst = go 1 lst 
    where 
        go _ [] = -1
        go i (y:ys) 
            | x == y = i
            | otherwise = go (i+1) ys

umetni:: [a] -> a -> [a]
umetni [] x = []
umetni [y] _ = [y]
umetni (y:ys) x =  y : x : umetni ys x