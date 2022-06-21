'''
Európa, Python_3. feladatsor
9 részfeladat 18 pont

A feladat kezdetekor, majd minden feladat során futtatni kell a unit teszteket.
(pipa a baloldali menüsávon, majd a kék Run tests gomb megnyomása)
A feladat beadásához a képernyő jobb felső részén a SUBMIT gombot kell megnyomni.
A main.py fájlt nem szabad módosítani.
A feladat megoldása során az eu.py fájlban kell létrehozni a kért Eu osztályt és a függvényeket.

Feladatok: 

1. Osztály létrehozása Eu: néven az eu.py fájlban
2. A forrast_beolvas_feldolgoz_listaval_visszater(fname) függvény létrehozása az eu.py fájlban. Bemenő paraméter a fájl neve.
3. A tagallamok_szama_2018(lista) függvény létrehozása az eu.py fájlban.
4. A csatlakozasok_szama_az_evben(lista) függvény létrehozása az eu.py fájlban.
5. A csatlakozasok_szama_a_honapban(lista) függvény létrehozása az eu.py fájlban.
6. Az orszag_csatlakozasi_datuma(lista) függvény létrehozása az eu.py fájlban.
7. Az utoljara_csatlakozott_orszag(lista) függvény létrehozása az eu.py fájlban.
8. A legtobb_csatlakozas_honapja(lista) függvény létrehozása az eu.py fájlban.
9. A tagallamok_szama_az_adott_evben(lista) függvény létrehozása az eu.py fájlban.
'''



#1. Az Eu osztály létrehozása:
class Eu:
  def __init__(self,sor):
    orszag, datum = sor.strip().split(";")
    self.orszag = orszag
    self.datum  = datum
    self.ev     = int(datum[ : 4])
    self.honap  = int(datum[5: 7])
    self.nap    = int(datum[8:10])
      
# -------------------------------------------------------
# 2. Forrast beolvas, feldolgoz listaval visszater. Bemenő paraméter a fájl neve.
def forrast_beolvas_feldolgoz_listaval_visszater(fname):
    with open(fname,"r",encoding="utf8") as f:
        return [ Eu(sor) for sor in f ]
          
# -------------------------------------------------------
# 3. A tagállamok száma 2018-ban a BREXIT előtt, tehát Az Egyesült királyság még tag.
def tagallamok_szama_2018(lista):
    return len(lista)

#--------------------------------------------------------

# 4. 
def csatlakozasok_szama_az_evben(lista, ev):
    return len( [sor for sor in lista if sor.ev == ev] )
    
#--------------------------------------------------------

# 5.
def csatlakozasok_szama_a_honapban(lista, honap):
    return sum( [1 for sor in lista if sor.honap == honap] )
   
#--------------------------------------------------------

# 6. 
def orszag_csatlakozasi_datuma(lista, orszag):
    datum = [sor.datum for sor in lista if sor.orszag == orszag]
    if datum:
        return datum[0]
    else:
        return None
    
#--------------------------------------------------------
# 7.
def utoljara_csatlakozott_orszag(lista):
    return max(lista, key=lambda x: x.datum).orszag

#--------------------------------------------------------

# 8.
def legtobb_csatlakozas_honapja(lista):
    honapok = dict()
    for sor in lista:
        honapok[sor.honap] = honapok.get(sor.honap, 0) + 1
    return max(honapok, key=honapok.get)

#--------------------------------------------------------

# 9.
def tagallamok_szama_az_adott_evben(lista, ev):
    evek = dict()
    for sor in lista:
        if sor.ev <= ev:
            evek[sor.ev] = evek.get(sor.ev, 0) + 1
    return sum(evek.values())
