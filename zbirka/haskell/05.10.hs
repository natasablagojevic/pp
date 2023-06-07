nzd:: Int -> Int -> Int 
nzd a b = 
    if b == 0 then a 
    else nzd b tmp
    where tmp = mod a b
    

-- tmp = a % b
-- a = b
-- b = tmp