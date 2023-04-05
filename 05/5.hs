sumaN:: Num a => a -> a 
sumaN n = if n == 0 then 0 else n + sumaN (n-1)

sumaN' :: Num a => a -> a
sumaN' n 
    | n == 0 = 0
    | otherwise = n + sumaN' (n-1)

sumaN'' :: Num a => a -> a
sumaN'' n = 
    if n == 0 then 0
    else n + sumaN'' (n-1) 

sumaN''' Num a => a -> a
sumaN''' 0 = 0
sumaN''' n = n + sumaN''' (n-1)