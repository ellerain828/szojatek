"""
https://loma.info.hu/index.php/programozas/programozas-feladatok/20-szojatek
feladat megoldása
"""

#1. feladat - file importálása

with open("szoveg.txt", "r", encoding="utf8") as file:
    words = [line.rstrip("\n") for line in file]
    words = list(dict.fromkeys(words))

#2. feladat - mgh-k vizsgálata
    
chosenword = input("Szó: ")

vowels = ["a", "e", "i", "o", "u"]

contains = True

for letters in chosenword:
    if letters in vowels:
        contains = True
        break
    else:
        contains = False

if contains == True:
    print("Van benne magánhangzó.")
else:
    print("Nincs benne magánhangzó.") #Van egyáltalán ilyen szó?xd

print()

#3. feladat - szavak számának vizsgálata
    
wordsamount = len(words)
print(f"Az állomány {wordsamount} szót tartalmaz.")

print()

#4. feladat - leghosszabb szó vizsgálata

longestword = words[0]

for i in range(wordsamount):
    if len(words[i]) > len(longestword):
        longestword = words[i]

print(f"A leghosszabb szó a(z) {longestword}, hosszúsága {len(longestword)} karakter.")

print()

#5. feladat - szavak kezdőbetűje és vége "a"

startswaendswa = []

for i in words:
    if i[0] == "a" and i[-1] == "a":
        startswaendswa.append(i)

print(" ".join(startswaendswa))

print(f"{len(startswaendswa)}/{wordsamount}: {len(startswaendswa) / wordsamount:.2%} ")

#6. feladat - 5 karakterből álló szavak kigyűjtése .txt fileba

lenght5 = []

for i in range(wordsamount):
    if len(words[i]) == 5:
        lenght5.append(words[i])

with open("otkarakteres.txt", "w", encoding="utf8") as wfile:
    wfile.writelines("\n".join(lenght5) + "\n")
