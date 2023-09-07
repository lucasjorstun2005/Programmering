
name = input("Vad är ditt namn? ")
cash = int(input("Hur mycket pengar har du? "))

if cash > 100000:
    print(name, "du är rik. Man kommer långt med", str(cash) + "kr på kontot")
else:
    print(name, "du är inte rik. Man kommer inte långt med", str(cash) + "kr på kontot")