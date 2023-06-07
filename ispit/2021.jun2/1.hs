-- najduza lst
-- najduza [x] = x

najduza:: [String] -> String
najduza lst = snd $ maximum $ [(length xs, xs) | xs <- lst] 

-- [izraz | generator, filter]

umanji :: String -> String 
umanji str = [toUpper s | s <- str]
