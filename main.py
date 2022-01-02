"""
1. Feladat
Készíts egy rövid programot, amely 1 és 3 között generál véletlenszámot, majd összehasonlítja ezt a felhasználó által megadott, szintén ebbe a tartományba eső számmal! Az összehasonlítás eredményéről tájékoztassa a felhasználót!
"""
gondolt_szám = int(input('Adjon meg egy EGÉSZ számot 1-3-ig! '))

import random
random_szam = random.randint(1,3)

if gondolt_szám == random_szam :
  print ('Jó tipp!')
elif gondolt_szám != random_szam :
  print('A tipp helytelen!')
if gondolt_szám > 3 :
  print ('MONDOM 1-től 3-ig!!!')

print ('A gép által gondolt szám:',random_szam)