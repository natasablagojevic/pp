fibs 0 = 0
fibs 1 = 1
fibs n = fibs(n-1) + fibs(n-2)

fib:: Int -> [Int]
fib n = zipWith (fibs(n)) ()
