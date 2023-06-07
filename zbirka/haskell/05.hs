suma:: Int -> Int
suma n = 
    if n == 0 then 0
    else n + suma(n-1)

suma':: Int -> Int
suma' n = sum lista
    where lista = [1..n]

suma'':: Int -> Int 
suma'' n 
    | n == 0 = 0
    | otherwise = n + suma(n-1)