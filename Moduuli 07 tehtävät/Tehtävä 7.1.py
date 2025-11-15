vuodenajat = ("Kevät","Kesä","Syksy","Talvi")

kuukaudet = ("Tammikuu","Helmikuu","Maaliskuu","Huhtikuu","Toukokuu","Kesäkuu","Heinäkuu","Elokuu","Syyskuu",
             "Lokakuu","Marraskuu","Joulukuu")

kuukausinumero = int(input("anna kuukausinumero (1-12): "))

if kuukausinumero <1 or kuukausinumero>12:
    print("virheellinen kuukausinumero.")
if kuukausinumero in(3,4,5):
    print (vuodenajat[0]) #Kevät
elif kuukausinumero in (6,7,8):
    print (vuodenajat[1]) #Kesä
elif kuukausinumero in (9,10,11):
    print (vuodenajat[2]) # Syksy
elif kuukausinumero in (12,1,2):
    print (vuodenajat[3]) # Talvi



