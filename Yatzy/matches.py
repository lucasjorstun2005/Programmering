from collections import Counter

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

    # Räkna antalet ettor och lägg in det i värdet för ettor, (Samma algoritm gäller för 2or, 3or, 4or, 5or, och 6or)
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
        # Initiera en counter som räknar tärningarna
        d = Counter(dices)

        # Initiera en lista av par samt en variabel för att kolla att det är ett par
        par = []
        t = 0

        # En loop för tärningarna och räkningen av lika tärningar
        for dice, count in d.items():

            # Lägger till ett par i par-listan
            par.append(dice * 2)

            # Om det finns ett par, lägg till summan av paret i t-variabeln och breaka
            if len(par) == 1:
                t = sum(par)
                break
        # Om paret är större än 0 lägg till summan av det i värdet av par
        if t > 0:
            matchar['Par'] += t
        
        # Annars, stryk par, alltså att par == 0
        else:
            print("Stryker Ett par")

    elif svar.lower() == "två par" or svar.lower() == "tvåpar":
        # Initiera räknaren
        dice_count = Counter(dices)
        
        # Gör en lista för paren och en variabeln för totalen av paren
        pairs = []
        totalt = 0

        # Loopa igenom tärningarna
        for dice, count in dice_count.items():
            # Om det finns 2 stycken lika tärningar, lägg till dem i par-listan
            if count >= 2:
                pairs.append(dice * 2)
                
                # Om det finns 2 par, lägg till summan av paren i totalen
                if len(pairs) == 2:
                    totalt = sum(pairs)
                    break
            
        # Om totalen är större än noll, gör värdet på tvåpar till totalen
        if totalt > 0:
            matchar['Tvåpar'] += totalt
        else:
            print("Stryker Tvåpar")

    elif svar.lower() == "tretal" or svar.lower() == "triss":
        # Initiera räknare
        tärning_räknare = Counter(dices)

        # Loopa igenom tärningar
        for dice, count in tärning_räknare.items():
            # Om det finns 3 lika tärningar
            if count >= 3:
                # Gör värdet av tretal till värdet av tärningarna
                matchar['Tretal'] = 3 * dice
        # Stryk tretal om det inte finns 3 lika
        if matchar['Tretal'] == 0:
            print("Stryker Tretal")
    
    elif svar.lower() == "fyrtal":
        # Initera räknare
        dice_counts = Counter(dices)
        # Loopa tärningarna
        for dice, count in dice_counts.items():
            # Om det finns 4 lika, gör värdet av fyrtal till värdet av tärningarna
            if count >= 4:
                matchar['Fyrtal'] = 4 * dice

        if matchar['Fyrtal'] == 0:
            print("Stryker Fyrtal")
    
    elif svar.lower() == "chans":
        # Chans är bara sunmman av alla tärningar
        matchar['chans'] = sum(dices)

    elif svar.lower() == "liten stege" or svar.lower() == "litenstege":
        # Sortera tärningarna
        dices = dices.sort()
        
        # Conditional för tärningarna där de ska vara i ordningen för att det ska vara en liten stege
        if dices[0] == 1 and dices[1] == 2 and dices[2] == 3 and dices[3] == 4 and dices[4] == 5:
            # Värdet för liten stege är summan av tärningarna, det är alltid 15
            matchar['Liten stege'] = sum(dices)
        else:
            # Om det inte är en liten stege, stryk den
            print("Stryker liten stege")
    
    elif svar.lower() == "stor stege" or svar.lower() == "storstege":
        # Sortera tärningarna
        dices = dices.sort()

        # Conditional för tärningarna där de ska vara i ordningen för stor stege
        if dices[0] == 2 and dices[1] == 3 and dices[2] == 4 and dices[3] == 5 and dices[4] == 6:
            # Värdet för stor stege är summan av tärningarna, vilket alltid är 20
            matchar['Stor stege'] = sum(dices)
        else:
            # Om det inte är en stor stege, stryk den
            print("Stryker stor stege")
        
    elif svar.lower() == "kåk":
        # Initiera räknare
        dice_counts = Counter(dices)

        # Kolla så att det bara finns 2 värden på tärningarna, t.ex [5, 5, 5, 3, 3]
        if len(dice_counts) == 2:
            counts = list(dice_counts.values())

            # Kolla så att ett värde framkommer 3 gånger och det andra värdet 2 gånger
            if (3 in counts) and (2 in counts):
                matchar['Kåk'] = sum(dices)
            else:
                print("Stryker kåk")

        else:
            print("Stryker kåk")
        
    elif svar.lower() == "yatzy":
        # Initiera räknare
        dice_counts = Counter(dices)

        # Loopa igenom tärningarna
        for dice, count in dice_counts.items():

            # Kolla om alla tärningar är lika
            if count == 5:

                # Värdet på yatzy blir 50 då yatzy alltid ger 50 poäng
                matchar['Yatzy'] = 50

        if matchar['Yatzy'] == 0:
            print("Stryker yatzy")
    
    # Conitional för bonus där ifall värdet av ettor, tvåor, treor, fyror, femmor, och sexor är större eller lika med 63, får man en bonus på 50 poäng
    if matchar['Ettor'] + matchar['Tvåor'] + matchar['Treor'] + matchar['Fyror'] + matchar['Femmor'] + matchar['Sexor'] >= 63:
        matchar['Bonus'] = 50
    



            
        
        
    # Totalen är summan av alla värden på matcharna
    total = sum(matchar)

    # Returnera värdet av total till yatzy.py
    return total