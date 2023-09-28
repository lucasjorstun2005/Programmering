tal1 = input("Skriv ett tal: ")
tal1 = int(tal1)
tal2 = input("Skriv ett till tal: ")
tal2 = int(tal2)

if tal1 > tal2:
    print("Tal 1 är större")
elif tal1 < tal2:
    print("Tal 2 är större")
elif tal1 == tal2:
    print("Talen är lika stora")