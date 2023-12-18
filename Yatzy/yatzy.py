import random
from matches import points, mathcar

dices = []

def main():
    global dices
    print("Välkommen till Yatzy!\nDessa kan du välja på efter en runda (Skriv hela namnet t.ex Tretal):\nEttor\nTvåor\nTreor\nFyror\nFemmor\nSexor\nEtt Par\nTvå Par\nTretal\nFyrtal\nLiten Stege\nStor Stege\nChans (kan bara väljas en gång)\nKåk\nYatzy\nOm summan av dina Ettor, Tvåor, Treor, Fyror, Femmor och Sexor är 63 eller mer får du 50 poäng extra i bonus. Du kan alltså inte välja bonus.")
    print("\n")
    i = 0
    while i < 14:
        firstcast()
        printdices()
        i += 1
        runda()
        

def cast(x):
    for i in range(x):
        dice = random.randint(1, 6)
        dices.append(dice)


def firstcast():
    cast(5)

def remove():
    amount = int(input("Hur många tärningar vill du ta bort? "))
    for i in range(amount):
        tärning = input("Säg en tärning du vill ta bort: ")
        dices.remove(tärning)
    return amount

def printdices():
    dices_str = "".join(dices)
    return f"Dina tärningar är {dices_str}"

def runda():
    while j < 2:
            printdices()
            choice = print("Vill du ta bort några tärningar? (j, n)")
            if choice.lower() == "j":
                amount = remove()
                cast(amount)
            elif choice.lower() == "n":
                print(printdices())
                points(dices)
                break
            j += 1

main()