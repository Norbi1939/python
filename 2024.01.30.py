print()

#fájl megnyítása

f = open("awsd.txt", "r", encoding="UTF-8")

adatok = []

# kétdimenziós lista (mátrix) létrehozása
for sor in f:
    adatok.append(sor.replace("\n", "").strip().split())

#adatok konvertálása a mátrixban

i = 0
while i < len(adatok):
    j = 0
    while j < len(adatok[i]):
        adatok[i][j] = int(adatok[i][j])
        j += 1
    i += 1


"""

#1.feladat#

A példában látható módon írjuk ki az adatszerkezet tartalmát!
PÉLDA:
1.adatsor: -1 2 54 12 89 -78 -34 78 92 13
2.adatsor: 23 45 -23 -78 -98 45 67 89
...
3.adatsor: -1 -11 -67
"""


i = 0
while i < len(adatok):
    j = 0
    print(f"{i + 1}.adatsor : ", end=" ")
    while j < len(adatok[i]):
        print(adatok[i][j], end=" ")
        j += 1
    print()
    i += 1




"""

#2.feladat:#

Melyik a leghosszabb adatsor?
PÉLDA:
A leghosszabb adatsor: 4. (14.sor)
"""

maxÉrték = len(adatok[0])
maxhely = 0

i = 1
while i < len(adatok):
    if len(adatok[i]) > maxÉrték:
        maxÉrték = len(adatok[i])
        maxhely = i
    i += 1

print(f" a leghosszabb adatsor: {maxhely + 1}. ({maxÉrték} adat)")

"""
#3.feladat (HF):#
Igaz-e, hogy van olyan adatsor, amelyikben bármely két egymás követő elem
értékének a különbsége 5?
PÉLDA:
nem igaz állítás.
vagy
igaz az állítás: 4.sor (13. és 14.elem)
"""

adatok = 0
szerepel = False



if szerepel:
    print(f"igaz az állitás: {}.sor({}. és {}. elem")
else:
    print("Nem igaz az álíítás")



f.close()

print()








Ł