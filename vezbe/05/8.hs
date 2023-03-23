-- ceo deo korena
ceoDeo x = ceoDeoUtil x 1
	where
		ceoDeoUtil x i 
		| i*i > x = i-1
		| otherwise = ceoDeoUtil x (i+1)
