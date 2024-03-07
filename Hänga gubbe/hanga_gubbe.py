import random

ord = ['regnbåge', 'hemlig', 'dator', 'mobil', 'skärm', 
       'tavla', 'penna', 'skola', 'lärare', 'katt', 'hund', 
       'kofot', 'skruv', 'jägare', 'skog', 'fisk', 'hav', 'sjö', 'flod', 'vatten',
       'båt', 'fartyg', 'flygplan', 'bil', 'cykel', 'motorcykel', 'buss', 'tåg', 'spårvagn',
       'taxi', 'lastbil', 'skåpbil', 'ambulans', 'brandbil', 'polisbil', 'helikopter', 'flygplan',
       'fågel', 'fjäril', 'blomma', 'träd', 'buske', 'gräs', 'jord', 'sand', 'sten', 'klippa',
       'berg', 'dal', 'slätt', 'kulle', 'bergstopp', 'höjd', 'dalgång', 'ravin', 'klyfta', 'grotta',
       'håla', 'tunnel', 'bro', 'väg', 'gata', 'gränd', 'torg', 'park', 'skogsdunge', 'skogsbryn',
       'skogskant', 'skogsväg', 'skogstig', 'skogssjö', 'skogstjärn', 'skogsbäck', 'skogsfågel',]

word = random.choice(ord)
guesses = 0

print('Välkömen till hänga gubbe! Du har 7 försök på dig att gissa ordet. Lycka till!')
u = "_" * len(word)
print(u)
i = 0
while i < 7:
    bokstav = input("Gissa en bokstav: ")
    if bokstav in word:
        for j in range(len(word)):
            if bokstav == word[j]:
                u = u[:j] + bokstav + u[j+1:]
        print(u)
    else:
        guesses += 1
        print(f"Du har {7 - guesses} försök kvar.")
        print(u)
        i += 1
    if "_" not in u:
        print("Grattis! Du har gissat rätt ordet!")
        break
if guesses == 7:
    print("Tyvärr, du klarade det inte. Bättre lycka nästa gång!")
    print(f"Ordet var: {word}")

