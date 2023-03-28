map (+1) [1..10]
filter
all
any

suma lst = foldl (\acc e -> acc + e) 0 lst
suma = foldl (\acc e -> acc + e) 0 
suma = foldl (+) 0

-- uzmi prvi element kao akomulator
suma = foldl1 (+)

max = foldl1 max

spoji ls rs = foldl (:) rs  ls
spoji ls rs = foldl (flip : ) ls rs
spoji ls rs = foldr (:) ls rs

foldr
