# Haskell

- lambda racun osnova funckionalnog programiranja
- u haskelu je sve funkcija
- konstata je fja
- kompozicija fije sve sto radimo
- f-ja osnova svega
- **Strogo tipiziran** - nema implicitnih konverzija; sve mora da se slaze i da se navede (bolja optimizacija koda) (haskell, c, java)
- funkcija je preslikavanje
- naziv funkcije mora da pocinje malim slovom

- **Tipski razred** je skup tipova koji implementiraju neku od operacija (predefinisanje operacija), kompajler dedukuje najopstiji tip
    - Eq ('==', '!=')
    - Ord ('<', '<=', '>=', '>', 'min', 'max', ...) + Eq
    - Num ('+', '-', '*', 'abs', 'fromIntegral', ...) + Ord
    - Integral ('div', 'mod') + Num
    - Fractional ('/', 'recip') + Num

- **Karijeve funkcije** 
- **Asocijativnost** primene operacija (sleva u desno)
- Zagrada je desno asocijativna

- **Tipovi**:
    1. Bool
    2. Char, String 
    3. Int, Integer
    4. Float, Double

- **Kompozicija je sve**

- Rekurzija je sve
- Guard equations