import random

cards = [1, 1, 1, 1, 
        2, 2, 2, 2, 
        3, 3, 3, 3, 
        4, 4, 4, 4, 
        5, 5, 5, 5, 
        6, 6, 6, 6, 
        7, 7, 7, 7, 
        8, 8, 8, 8, 
        9, 9, 9, 9, 
        10, 10, 10, 10, 
        11, 11, 11, 11, 
        12, 12, 12, 12, 
        13, 13, 13, 13,]
p_card1 = 0
p_card2 = 0
d_card1 = 0
d_card2 = 0
new_card = []

def main():
    global p_card1, p_card2, d_card2, d_card1, new_card
    p_card1 = deal()
    p_card2 = deal()
    d_card1 = deal()
    d_card2 = deal()
    new_card = []
    i = 0

    player = p_card1 + p_card2
    dealer = d_card1 + d_card2

    print(f"Dina kort: {p_card1}, {p_card2}")
    print(f"Dealer kort: {d_card1},")
    print("\n")
    print(f"Din total: {player}")

    if player > 21:
        print("Du har förlorat")
        return
    
    while True:
        choice = input("Hit or stand? (h, s) ")

        if choice.lower() == "h":
            new_card.append(deal())
            player += new_card[i]
            ess(p_card1, p_card2, d_card1, d_card2, new_card, player, dealer)
            print(print_player(player, p_card1, p_card2, new_card))
            i += 1
            if player > 21:
                print("Du är tjock")
                print("Du har förlorat")
                return
            elif player == 21:
                print("Blackjack!")
                return
            continue
        elif choice.lower() == "s":
            if dealer > 21 and player < 21:
                print(print_player(player, p_card1, p_card2, new_card))
                print(print_dealer(dealer, d_card1, d_card2))
                print("Du har vunnit")
            elif player > dealer:
                print(print_player(player, p_card1, p_card2, new_card))
                print(print_dealer(dealer, d_card1, d_card2))
                print("Du har vunnit")
            elif player < dealer:
                print(print_player(player, p_card1, p_card2, new_card))
                print(print_dealer(dealer, d_card1, d_card2))
                print("Du har förlorat")
            elif player == dealer:
                print(print_player(player, p_card1, p_card2, new_card))
                print(print_dealer(dealer, d_card1, d_card2))
                print("Lika")
            return
        else:
            print("Skriv h eller s.")



def deal():
    kort = 0
    kort = random.choice(cards)
    cards.remove(kort)
    return kort

def print_dealer(dealer, d_card1, d_card2):
    return f"Dealer kort: {d_card1}, {d_card2}\nDealer total: {dealer}"

def print_player(player, p_card1, p_card2, new_card):
    if new_card == []:
        return f"Dina kort: {p_card1}, {p_card2}\nDin total: {player}"
    else:
        new_cards = str(new_card)[1:-1]
        return f"Dina kort: {p_card1}, {p_card2}, {new_cards}\nDin total: {player}"
    
def ess(p_card1, p_card2, d_card1, d_card2, new_card, player, dealer):
    j = -1

    if p_card1 == 1 and player < 21:
        p_card1 == 11
    if p_card2 == 1 and player < 21:
        p_card2 == 11
    if d_card1 == 1 and dealer < 21:
        d_card1 == 11
    if d_card2 == 1 and dealer < 21:
        d_card2 == 11
    if 1 in new_card:
        new_card.remove(1)
        new_card.append(11)
    if p_card1 == 11 and player > 21:
        p_card1 == 1
    if p_card2 == 11 and player > 21:
        p_card2 == 1
    if d_card1 == 11 and dealer > 21:
        d_card1 == 1
    if d_card2 == 11 and dealer > 21:
        d_card2 == 1
    if new_card[j] == 11 and player > 21:
        new_card.remove(j)
        new_card.append(1)
    
    j -= 1





main()