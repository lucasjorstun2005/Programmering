while True:
    tal = input("Mata in ett tal: ")
    tal = int(tal)
    if tal < 10:
        print("ental")
    elif tal <= 99 and tal >= 10:
        print("Tvåsiffrigt tal")
    elif tal >= 100 and tal <= 999:
        print("Tresiffrigt tal")
    elif tal < 0:
        print("negativt tal")
    else:
        print("Fyrsiffrigt tal eller mer")
    svar = input("Vill du säga ett till tal? (y,n) ")
    if svar == "y":
        continue
    elif svar == "n":
        break