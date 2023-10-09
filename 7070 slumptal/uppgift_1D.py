import random

print("Welcome to tärning\Ett spel kostart 1 krona.\nVinstplan:\ntvå lika - 5kr\nen sexa - 3 kr\nstege - 3 kr")

svar = input("Välj sätt in pengar (i), eller avsluta (a)")
if svar == "i":
    pengar = int(input("Hur mycket vill du sätta in?"))
    print("Ditt saldo är", pengar + "kr")
elif svar == "a":
    print("Hejdå")
else:
    print("Svara med i eller j")
dice1 = random.randrange(5, 6)
dice2 = random.randrange(6, 7)

while pengar > 0:
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
print("Hejdå!")