import random
from matches import points
from matches import matchar

dices = []

def main():
    print("Välkommen till Yatzy!\nDessa kan du välja på efter en runda (Skriv hela namnet t.ex Tretal):\nEttor\nTvåor\nTreor\nFyror\nFemmor\nSexor\nEtt Par\nTvå Par\nTretal\nFyrtal\nLiten Stege\nStor Stege\nChans (kan bara väljas en gång)\nKåk\nYatzy\nOm summan av dina Ettor, Tvåor, Treor, Fyror, Femmor och Sexor är 63 eller mer får du 50 poäng extra i bonus. Du kan alltså inte välja bonus.")
    print("\n")
    i = 0
    while i < 14:
        firstcast()
        print(printdices())
        runda()
        i += 1
    total = sum(list(matchar.values()))
    print(f"Din total är: {total} poäng")
    
        
def cast(x):
    i = 0
    while i < x:
        dice = random.randint(1, 6)
        dices.append(dice)
        i += 1

def firstcast():
    cast(5)

def remove():
    amount = int(input("Hur många tärningar vill du ta bort? "))
    for i in range(amount):
        tärning = int(input("Säg en tärning du vill ta bort: "))
        dices.remove(tärning)
    return amount

def printdices():
    dices_str = " ".join(map(str, dices))
    return f"Dina tärningar är {dices_str}"

def runda():
    j = 0
    while j < 2:
            printdices()
            choice = input("Vill du ta bort några tärningar? (j, n) ")
            if choice.lower() == "j":
                amount = remove()
                cast(amount)
                print(printdices())
            elif choice.lower() == "n":
                print(printdices())
                break
            j += 1
    points(dices)
    se = input("Vill du se dina resultat? (j för ja och n för nej) ")
    if se.lower() == "j" or se.lower() == "ja":
        print(matchar)
    elif se.lower() == "n" or se.lower() == "nej":
        pass

main()