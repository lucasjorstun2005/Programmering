import random

svar = input("Vill du spela? j/n ")
pengar = input("Hur mycket vill du spela om? ")
dice1 = random.randrange(5, 6)
dice2 = random.randrange(6, 7)

while pengar > 0:
    if svar == "j":
        print(dice1, dice2)
        if dice1 == dice2 and dice1 == 6:
            print("6 vinst")
        elif dice1 + 1 == dice2:
            print("Stege-vinst")
        elif dice2 + 1 == dice1:
            print("Bakåt Stege-vinst")
        elif dice1 == dice2:
            print("Vinst")
        else:
            print("Förlust")
        print("Tack för att du spelade en stund!")
    elif svar == "n":
        print("Det är OK, du kanske vill spela någon annan gång")
    else:
        print("svara med 'j' eller 'n'.")