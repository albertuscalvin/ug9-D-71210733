alassegitiga =int(input("masukkan alas atap : "))
tinggiatap =int(input("masukkan tinggi atap : "))
tinggitembok =int(input("masukkan tinggi tembok : "))
segitiga =(tinggiatap * alassegitiga) / 2
kotak = tinggitembok * tinggitembok
luas = segitiga + kotak
semen = luas / 5
print(f'rumah tersebut membutuhkan {semen} sak semen')
