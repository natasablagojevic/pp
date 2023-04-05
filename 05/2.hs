f:: Num a => a -> a -> a
f x y = x + 3*y - x*y

-- g(x, y) = max(|a|, |b|)

g:: (Num a, Ord a) => a -> a -> a
g x y = max (abs (x)) (abs (y))