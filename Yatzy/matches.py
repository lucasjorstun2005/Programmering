from yatzy import dices, printdices

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
        i = 0
        j = 1
        while i < len(dices):
            while j < len(dices):
                if dices[i] == dices[j]:
                    matchar['Par'] += dices[i] + dices[j]
                    break
                j += 1
            j = 0
            i += 1
            break
        if matchar['Par'] == 0:
            print("Stryker Ett par")
        i = 0
        j = 0

    elif svar.lower() == "två par" or svar.lower() == "tvåpar":
        i = 0
        j = 1
        par1 = 0
        par2 = 0
        while i < len(dices):
            while j < len(dices):
                if par1 == 0:
                    if dices[i] == dices[j]:
                        par1 = dices[i] + dices[j]
                elif par1 != 0:
                    if dices[i] == dices[j]:
                        par2 = dices[i] + dices[j]
                j += 1
            j = 0
            i += 1
            break
        matchar['Tvåpar'] += par1 + par2
        if matchar['Tvåpar'] == 0:
            print("Stryker Två Par")
        i = 0
        j = 0

    elif svar.lower() == "tretal" or svar.lower() == "triss":
        i = 0
        j = 1
        k = 2
        while i < len(dices):
            while j < len(dices):
                while k < len(dices):
                    if dices[i] == dices[j] and dices[j] == dices[k]:
                        matchar['Tretal'] = dices[i] + dices[j] + dices[k]
                        break
                    k += 1
                k = 0
                j += 1
            j = 0
            i += 1
            break
        if matchar['Tretal'] == 0:
            print("Stryker Treor")
        i = 0
        j = 0
        k = 0
    
    elif svar.lower() == "fyrtal":
        i = 0
        j = 1
        k = 2
        h = 3
        while i < len(dices):
            while j < len(dices):
                while k < len(dices):
                    while h < len(dices):
                        if dices[i] == dices[j] and dices[i] == dices[k] and dices[h]:
                            matchar['Fyrtal'] = dices[i] + dices[j] + dices[k] + dices[h]
                            break
                        h += 1
                    h = 0
                    k += 1
                k = 0
                j += 1
            j = 0
            i += 1
            break
        if matchar['Fyrtal'] == 0:
            print("Stryker Fyrtal")
        i = 0
        j = 0
        k = 0
        h = 0
    
    elif svar.lower() == "chans":
        matchar['chans'] = sum(dices)
    
    
            
        
        
        
    total = sum(matchar)
    return total