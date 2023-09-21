import random

print("Välkommen till tärning\nEtt spel kostar 1kr\nVinstplan:\ntvå lika - 5kr\nen sexa - 3kr\nstege - 3kr")
svar = input("Välj sätt in pengar (i), eller avsluta (a): ")
if svar == "i":
    pengar = int(input("Hur mycket vill du lägga in? (skriv bara siffror): "))
    pengar = pengar - 1
elif svar == "a":
    pengar = 0
else:
    print("Skriv i eller a")
dice1 = random.randrange(1, 7)
dice2 = random.randrange(1, 7)

while pengar > -1:
    print(dice1, dice2)
    if dice1 == 6 or dice2 == 6:
        print("6-vinst + 3kr")
        pengar = pengar + 3
    elif dice1 + 1 == dice2:
        print("stege-vinst + 3kr")
        pengar = pengar + 3
    elif dice1 == dice2:
        print("Vinst + 5kr")
        pengar = pengar + 5
    else:
        print("Förlust")
    print("Du har nu", str(pengar) + "kr.")
    svar = input("Vill du spela (s), sätta in pengar (i), eller avsluta (a)? ")
    if svar == "s":
        pengar = pengar - 1
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        continue
    elif svar == "i":
        antal = int(input("Hur mycket vill du sätta in? (skriv bara i siffror): "))
        pengar = pengar + antal
        pengar = pengar - 1
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        continue
    elif svar == "a":
        break
    else:
        print('Skriv "s", "i", eller "a"')
print("Du avslutade med", str(pengar) + "kr")
print("Hejdå!")