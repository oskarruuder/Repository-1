nimi = input("Kerro nimesi:").lower()
if nimi != "matti":
    annokset = int(input("Montako keittoannosta"))
    print(f"kokonaishinta on {annokset * 5.9}")
else :
    print("Seuraava kiitos!")


