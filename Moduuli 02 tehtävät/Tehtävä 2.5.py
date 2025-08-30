LUOTI_GRAMMOINA = 13.3
NAULA_LUOTEINA = 32
LEIVISKA_NAULOINA = 20

leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

kokonaisluodit = (leiviskat * LEIVISKA_NAULOINA * NAULA_LUOTEINA +naulat * NAULA_LUOTEINA +luodit)

grammat = kokonaisluodit * LUOTI_GRAMMOINA

kilogrammat = int(grammat // 1000)
jäännösgrammat = round(grammat % 1000, 2)

print("Massa nykymittojen mukaan: {kilogrammat} kg)".format(kilogrammat=kilogrammat))




