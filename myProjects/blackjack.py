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
    ace_count = 0
    for card in hand:
        score += blackjack_cards[card]
        if card == 'A':
            ace_count += 1
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

def deal_hand(hand):
    card = random.choice(list(blackjack_cards.keys()))
    hand.append(card)
    return hand


def check_blackjack(hand):
    if len(hand) == 2 and calculate_score(hand) == 21:
        return True
    return False

def check_bust(hand):
    if calculate_score(hand) > 21:
        return True
    return False

def check_scores(player_hand, dealer_hand):
    if calculate_score(player_hand) == calculate_score(dealer_hand):
        return "It's a draw"
    elif calculate_score(player_hand) > calculate_score(dealer_hand):
        return "Congratulations you win!"
    elif calculate_score(dealer_hand) > 21:
        return "Dealer went bust. You WIN!"
    elif calculate_score(player_hand) > 21:
        return "You went bust. You LOSE"
    elif check_blackjack(player_hand):
        return "You have a BlackJack. You WIN"
    elif check_blackjack(dealer_hand):
        return "Dealer has a BlackJack. You LOSE"
    else:
        return "You LOSE"


def play_game():
    for _ in range(2):
        deal_hand(my_hand)
        deal_hand(dealer_hand)
    print(f"Your cards are: {my_hand} and your score is: {calculate_score(my_hand)}")
    print(f"Dealer's first card is: {dealer_hand[0]}")

    if check_blackjack(my_hand):
        return "You WIN"
    
    while input("Type 'y' or 'n' if you want more cards: ") == 'y':
        deal_hand(my_hand)
        print(f"Your cards are: {my_hand} and your score is: {calculate_score(my_hand)}")
        if check_bust(my_hand):
            print ("You went over. You LOSE")
            return
        

        
    while calculate_score(dealer_hand) < 17:
        deal_hand(dealer_hand)

    print(f"Your final hand is {my_hand} and your total score is: {calculate_score(my_hand)}")
    print(f"The dealer's final hand is {dealer_hand} and his total score is: {calculate_score(dealer_hand)}")
    print(check_scores(my_hand,dealer_hand))
    

while input("Do you want to play a game of BlackJack? 'y' or 'n'? ") == 'y':
    my_hand = []
    dealer_hand = []
    play_game()