def gallona(maara):
    return maara * 3.785

while True:
    maara = int(input("Anna gallona määrä: "))
    if maara < 0:
        break
    litrat = gallona(maara)
    print(f"{maara} gallonaa on{litrat: .2f} litraa")


