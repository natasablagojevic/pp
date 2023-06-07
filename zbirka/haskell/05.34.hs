parni:: Int -> Int -> [Int]
parni a b = filter (\t -> (mod) t 2 == 0) [a..b]

neparni:: Int -> Int -> [Int] 
neparni a b = filter (\t -> (mod) t 2 == 1) [a..b]