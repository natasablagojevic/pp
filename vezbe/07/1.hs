type Tacka = (Float, Float)

tacka:: Float -> Float -> Tacka
-- tacka x y = (x,y)
tacka x y = (,) x y

o :: Tacka
o = tacka 0.0 0.0

getX:: Tacka -> Float
getX = fst

getY:: Tacka -> Float
getY = snd

type Putanja = [Tacka]

putanja:: [Tacka] -> Putanja
putanja = id

duzinaPutanje:: Putanja -> Int
-- duzinaPutanje p = length p
duzinaPutanje = length 

translirajTacku:: Tacka -> Float -> Float -> Tacka
translirajTacku p dx dy = tacka (getX p + dx) (getY p + dy)

rastojanje:: Tacka -> Tacka -> Float
rastojanje p q = sqrt ( (getX p - getX q)^2 + (getY p - getY q)^2)


uKrugu:: Float -> Putanja -> Putanja
uKrugu r p = [t | t <- p, rastojanje o t < r]

uKrugu':: Float -> Putanja -> Putanja
uKrugu' r p = filter (\t -> rastojanje o t < r) p
--					  lambda f-ja

uKrugu'' r p = filter rastojanjeOdOManjeR p
	where rastojanjeOdOManjeR t = rastojanje o t < r

translirajPutanju:: Putanja -> Float -> Float -> Putanja
translirajPutanju p dx dy = map (\t -> translirajTacku t dx dy) p


nadovezi:: Tacka -> Putanja -> Putanja
nadovezi t p = p ++ [t]

nadovezi':: Tacka -> Putanja -> Putanja
nadovezi' t p = reverse (t: reverse p)

spoji:: Putanja -> Putanja -> Putanja
spoji = (++)

centroid:: Putanja -> Tacka
centroid p = tacka (sum (map getX p) / (fromIntegral (length p))) (sum (map getY p) / (fromIntegral (length p))) 

centroid' p = tacka (prosek osaX) (prosek osaY)
	where osaX = map getX p
		  osaY = map getY p
		  prosek l = sum l / (fromIntegral (length l))

kvandrat:: Tacka -> Int
kvandrat t = 
	| getX t > 0 && getY t > 0 = 1
	| getX t < 0 && getY t > 0 = 2
	| getX t < 0 && getY t < 0 = 3
	| getX t > 0 && getY t < 0 = 4
	 
kvandratPutanje:: Putanja -> Bool
kvandratPutanje p = if sviIsti then head kvadranti else 0 
	where 
		  sviIsti = all (\t -> t == head kvadranti) kvadranti
		  kvadranti = map kvadrant p

tackeUKvandratu:: Int -> Putanja -> Kvadrat
tackeUKvandratu k = filter (\t -> kvandrat t == k)
-- 							 t element kolekcije p
