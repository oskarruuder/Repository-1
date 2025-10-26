import random

def noppa (tahkot):
    return random.randint(1,tahkot)

tahkojen_määrä = int(input("Anna nopan tahkojen määrä: "))

heittojen_määrä = 0

while True:
    heitto = noppa(tahkojen_määrä)
    heittojen_määrä += 1
    print(heitto)
    if heitto == tahkojen_määrä:
        break

print(f"Heittoja yhteensä: {heittojen_määrä}")