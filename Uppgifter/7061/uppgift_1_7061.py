# Detta är uppgift 1
'''
svar = input("Gissa på ett tal: ")

while svar != "4":
    svar = input("Du svarade fel, gissa på ett annat tal: ")

print("Du gissade rätt")
'''

# Detta är uppgift 2
'''
tal = input("Gissa ett tal: ")
attempts = 0

while int(tal) != 42:
    if int(tal) < 42:
        print("För litet.")
    elif int(tal) > 42:
        print("För stort.")
    tal = input("Gissa på ett till tal: ")
    attempts = attempts + 1
print("Du behövde", str(attempts), "försök för att gissa rätt")
'''

# Detta är uppgift 3
'''
svar = input("Vad heter Norges huvudstad? ") 
attempts = 3
while svar.lower() != "oslo":
    attempts = attempts - 1
    print("Du har", str(attempts), "försök kvar.")
    if attempts == 0:
        print("Du har slut på försök, spelet är slut.")
        break
    elif svar == "oslo":
        print("Rätt svar, bra jobbat!")
        break
    svar = input("Gör ett till försök, Vad heter Norges huvudstad? ")
'''

# Detta är bonusuppgiften
'''
def ar_primtal(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

tal = int(input("Skriv in ett tal: "))

if ar_primtal(tal):
    print(f"{tal} är ett primtal!")
else:
    print(f"{tal} är inte ett primtal.")
'''