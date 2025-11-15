#Suomen tärkeimpien lentoasemien ICAO-koodit ovat muun muassa Helsinki-Vantaan lentoaseman (EFHK),
# Rovaniemen lentoaseman (EFRO),
# Oulun lentoaseman (EFOU),
# Kittilän lentoaseman (EFKT) ja Kuopion lentoaseman (EFKU) koodit

lentoasemat = {"EFHK":"Helsinki","EFRO":"Rovaniemi","EFOU":"Oulu","EFKT":"Kittilä","EFKU":"Kuopio"}

while True:
    aloitus = input("Haluatko A syöttää uuden lentoaseman, B hakea jo syötetyn lentoaseman tiedot C vai lopettaa: ")
    if aloitus == "A":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
    elif aloitus == "B":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoasema:", lentoasemat[icao])
        else:
            print("Lentoasemaa ei löytynyt.")
    elif aloitus == "C":
        print("Ohjelma lopetetaan.")
        break

