#Tästä tehtävästä en ole ihan varma että menikö oikein.

vuosi = int(input("Anna vuosiluku? "))
if vuosi % 4 == 0:
    print("Antamasi vuosi on karkausvuosi.")
elif vuosi % 400 == 0:
    print("Antamasi vuosi on karkausvuosi.")
else:
    print("Antamasi vuosi ei ole karkausvuosi.")
