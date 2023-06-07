list_all :: Foldable t => (a -> Bool) -> t a -> Bool
list_all = all

-- 05.47.hs 

obrni :: [a] -> [a]
obrni = reverse


-- 05.48.hs 

sufiks :: [a] -> [[a]]
sufiks = scanr (:) []

-- 05.49.hs 

prefiks :: [a] -> [[a]]
prefiks lst = map reverse (reverse $ scanr (:) [] $ reverse lst)  

-- 05.51.hs 

quickSort :: Ord a => [a] -> [a]
quickSort [] = []
quickSort (x:xs) = smallSort ++ [x] ++ bigSort 
    where 
        smallSort = [a | a <- xs, a <= x]
        bigSort = [a | a <- xs, a > x]