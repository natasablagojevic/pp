izDekadne:: Int -> Integer
izDekadne x osn = izDekadne(div x osn, osn) + (mod x osn)