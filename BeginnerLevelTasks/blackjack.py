import random

blackjack_cards = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11
}

def calculate_score(hand):
    score = 0
    ace_counter = 0

    for card in hand:
        score += blackjack_cards[card]
        if card == 'A':
            ace_counter += 1
    while score > 21 and ace_counter > 0:
        score -= 10
        ace_counter -= 1
    return score

def deal_hand(hand):
    card = random.choice(list(blackjack_cards.keys()))
    hand.append(card)
    return hand

def check_bust(hand):
    if calculate_score(hand) > 21:
        return True
    return False

def check_blackjack(hand):
    if calculate_score(hand) == 21:
        return True
    return False

def check_score(player_hand, dealer_hand):
    if calculate_score(player_hand) == calculate_score(dealer_hand):
        return "DRAW"
    elif check_blackjack(player_hand):
        return "You WIN"
    elif check_bust(player_hand):
        return "You LOSE"
    elif check_bust(dealer_hand):
        return "Dealer out. You WIN"
    elif calculate_score(player_hand) > calculate_score(dealer_hand):
        return "You WIN"
    else:
        return "You LOSE"
    

def play_game():
    for _ in range(2):
        deal_hand(my_hand)
        deal_hand(dealer_hand)
    print(f"Your hand is: {my_hand} and your score is: {calculate_score(my_hand)}")
    print(f"Dealer has {dealer_hand[0]}")

    if check_blackjack(my_hand):
        return "You WIN"

    while input("Do you want another card? 'y' or 'n' ") == 'y':
        deal_hand(my_hand)
        print(f"Your hand is: {my_hand} and your score is: {calculate_score(my_hand)}")
        if calculate_score(my_hand) > 21:
            print ("You are busted. You LOSE")
            return
    
    while calculate_score(dealer_hand) < 17:
        deal_hand(dealer_hand)
    
    print(f"Your final hand is {my_hand} and your total score is: {calculate_score(my_hand)}")
    print(f"The dealer's final hand is {dealer_hand} and his total score is: {calculate_score(dealer_hand)}")
    print(check_score(my_hand,dealer_hand))



while input("Do you want to play a game of BlackJack? 'y' or 'n' ") == 'y':
    my_hand = []
    dealer_hand = []
    play_game()