pozitivni:: [Int] -> [Int]
pozitivni l = filter (\t -> (>=) t 0) l

pozitivni':: [Int] -> [Int]
pozitivni' l = [s | s <- l, s >= 0]