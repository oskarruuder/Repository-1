nimijoukko = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi =="":
        break

    if nimi in nimijoukko:
        print ("aiemmin syötetty nimi:")
    else:
        print("Uusi nimi")
        nimijoukko.add(nimi)

print("\nSyötetyt nimet:")
for n in nimijoukko:
    print(n)


