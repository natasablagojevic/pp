tipJednacine:: Double -> Double  -> Double -> String
tipJednacine 0 _ _ = "Degenerisana"
tipJednacine a b c = 
	if b*b - 4*a*c > 0 then
		"Dva resenja"
	else if b*b - 2*a*c < 0 then
		"Nema resenja"
	else 
		"Jedno dvostruko resenje"

tipJednacine':: Double -> Double  -> Double -> String
tipJednacine' a b c
	| a == 0 = "Degenerisana"
	| d > 0 = "Dva resenja"
	| d < 0 = "Nema resenja"
	| d == 0 = "Jedno resenje"
	where d = b*b - 4*a*c 			-- fiksira vrednost promenljive da ne bismo racunali jednu stvar vise puta
