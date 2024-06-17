from replit import clear

bid_dict = {}


should_continue = True
while should_continue:
    clear()
    print("Welcome to the secret auction program.")
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bid_dict[name] = bid
    another_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if another_bidder == 'no':
        should_continue = False
        max_bid = max(bid_dict.values())
        for key, value in bid_dict.items():
            if value == max_bid:
                print(f"The winner is {key} with a bid of ${value}")
            else:
                continue
