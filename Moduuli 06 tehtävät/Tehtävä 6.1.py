import random

def noppa ():
    return random.randint(1,6)

while True:
    heitto = noppa()
    print(heitto)
    if heitto == 6:
        break


