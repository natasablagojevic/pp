len:: [a] -> Int 
len [] = 0
len l = 1 + len (tail l) 