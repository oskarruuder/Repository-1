import random

oikea_luku = random.randint(1, 10)

print("Arvaa tietokoneen valitsema luku (1-10):")

arvaus = 0
while arvaus != oikea_luku:
    arvaus = int(input("Anna arvauksesi: "))
    if arvaus < oikea_luku:
        print("Liian pieni arvaus")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus")
    else:
        print("Oikein!")




