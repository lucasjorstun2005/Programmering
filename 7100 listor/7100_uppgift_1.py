import random

resultat = []

for dice in range(10):
    dice = random.randrange(1, 7)
    resultat.append(dice)

reultat = resultat.sort()
print(resultat)

print("Summan av talen:", sum(resultat))
print("Medelvärdet av talen:", sum(resultat) / len(resultat))
print("Minsta värdet:", resultat[0])
print("Största värdet:", resultat[-1])

sexor = resultat.count(6)
print(f"Antal sexor: {sexor}")

print("Vanligaste numret:", max(set(resultat),key=resultat.count))