-- prviNegativni:: [a] -> [b]
prviNegativni :: (Ord a, Num a) => p -> [a] -> [a]
prviNegativni l = takeWhile (<0)

suma :: (Foldable t, Num a) => t a -> a
suma = sum