from yatzy import dices, printdices
from collections import Counter

dices = dices
matchar = {
    'Ettor': 0,
    'Tvåor': 0,
    'Treor': 0,
    'Fyror': 0,
    'Femmor': 0,
    'Sexor': 0,
    'Par': 0,
    'Tvåpar': 0,
    'Tretal': 0,
    'Fyrtal': 0,
    'Chans': 0,
    'Kåk': 0,
    'Liten stege': 0,
    'Stor stege': 0,
    'Yatzy': 0,
    'Bonus': 0,

}


def points(dices):
    svar = input("Vad vill du sätta poäng i (Se till att vara ärlig)? ")
    if svar.lower() == "ettor":
        for i in dices:
            if i == 1:
                matchar['Ettor'] += 1
        if matchar['Ettor'] == 0:
            print("Stryker Ettor")

    elif svar.lower() == "tvåor":
        for i in dices:
            if i == 2:
                matchar['Tvåor'] += 2
        if matchar['Tvåor'] == 0:
            print("Stryker Tvåor")

    elif svar.lower() == "treor":
        for i in dices:
            if i == 3:
                matchar['Treor'] += 3
        if matchar['Treor'] == 0:
            print("Stryker Treor")

    elif svar.lower() == "fyror":
        for i in dices:
            if i == 4:
                matchar['Fyror'] += 4
        if matchar['Fyror'] == 0:
            print("Stryker Fyror")

    elif svar.lower() == "femmor":
        for i in dices:
            if i == 5:
                matchar['Femmor'] += 5
        if matchar['Femmor'] == 0:
            print("Stryker Femmor")

    elif svar.lower() == "sexor":
        for i in dices:
            if i == 6:
                matchar['Sexor'] += 6
        if matchar['Sexor'] == 0:
            print("Stryker Sexor")

    elif svar.lower() == "ett par" or svar.lower() == "par" or svar.lower() == "ettpar":
        d = Counter(dices)

        par = []
        t = 0

        for dice, count in d.items():
            par.append(dice * 2)
            if len(par) == 1:
                t = sum(par)
                break
        if t > 0:
            matchar['Par'] += t
        else:
            print("Stryker Ett par")

    elif svar.lower() == "två par" or svar.lower() == "tvåpar":
        dice_count = Counter(dices)
        
        pairs = []
        totalt = 0

        for dice, count in dice_count.items():
            if count >= 2:
                pairs.append(dice * 2)
                if len(pairs) == 2:
                    totalt = sum(pairs)
                    break
        if totalt > 0:
            matchar['Tvåpar'] += totalt
        else:
            print("Stryker Tvåpar")

    elif svar.lower() == "tretal" or svar.lower() == "triss":
        tärning_räknare = Counter(dices)
        for dice, count in tärning_räknare.items():
            if count >= 3:
                matchar['Tretal'] = 3 * dice
        if matchar['Tretal'] == 0:
            print("Stryker Tretal")
    
    elif svar.lower() == "fyrtal":
        dice_counts = Counter(dices)
        for dice, count in dice_counts.items():
            if count >= 4:
                matchar['Fyrtal'] = 4 * dice
        if matchar['Fyrtal'] == 0:
            print("Stryker Fyrtal")
    
    elif svar.lower() == "chans":
        matchar['chans'] = sum(dices)
    
    
            
        
        
        
    total = sum(matchar)
    return total