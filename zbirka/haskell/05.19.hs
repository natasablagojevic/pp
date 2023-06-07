-- fibs:: Int -> Int
-- fibs n  
--     | n == 0 || n == 1 = 1
--     | otherwise = fibs(n-1) + fibs(n-2)


fib:: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib(n-1) + fib(n-2)