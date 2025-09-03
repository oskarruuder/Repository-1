print("valitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B:"
      " Vähennyslasku \n C: Kertolasku \n D: Jakolasku")

print("yhteenlasku", A + B)
print("vähennyslasku", A - B)
print("kertolasku", A * B)
print("desimaalijakolasku", A / B)

if valinta == "A":
    print("yhteenlasku", A + B)
elif valinta == "B":
    print("yhteenlasku", a - b)
elif valinta == "C":
    print("kertolasku", a * b)
elif valinta == "D":
    print("Desimaalijakolasku", a / b)
else:
    print("Valintasi oli virheellinen.")

a = float(input("anna ensimmäinen luku"))
b = float(input("anna toinen luku"))