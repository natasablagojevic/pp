type Tacka = (Float, Float) 

-- konstruktor
-- ako promenimo API, sve pada u vodu i mora sve izpocetka
-- apstrahovali smo konstruktor
tacka :: Float -> Float -> Tacka
-- taxka x y = (x, y)
tacka = (,)

-- getteri
x:: Tacka -> Float
-- x = fst
x (p, _) = p

-- getter
y:: Tacka -> Float
y = snd
-- y (_, )

{-
F-ja tip	
-}
o :: Tacka
o = tacka 0.0 0.0

type Putanja = [Tacka]

putanja:: [Tacka] -> Putanja
-- putanja ts = ts
putanja = id

duzinaPutanje:: Putanja -> Int
-- Int		=== Int
-- duzinaPutanje p = length p
duzinaPutanje = length

translirajTacku:: Tacka -> Float -> Float -> Tacka
translirajTacku t dx dy = tacka (x + dx) (y + dy)

rastojanje:: Tacka -> Tacka -> Float
rastojanje (x1, y1) (x2, y2) = sqrt ((x1-x2)^2 + (y1-y2)^2)


uKrugu:: Float -> [Tacka] -> [Tacka]
