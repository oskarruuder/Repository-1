import random

arpakuutiot = int(input("anna arpakuutioiden lukumäärä: "))

summa = 0

for i in range(arpakuutiot):
    heitto = random.randint(1, 6)
    summa += heitto

print("silmalukujen summa on: ", summa)






