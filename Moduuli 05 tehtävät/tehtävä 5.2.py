luvut = []

while True:
    syöte = input("anna lukuja: ")
    if syöte =="":break
    luvut.append(int(syöte))

luvut.sort(reverse=True)
viis_suurinta = luvut[:5]
for luku in viis_suurinta:
    print(luku)

