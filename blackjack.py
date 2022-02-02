import random

# Function to create the initial deck
def generate_deck(num_decks = 1):
    new_deck = []
    suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
    for i in range(1, 14):
        new_cards = []
        # Specify the Ace, Jack, Queen, King. Maybe a cleaner way to do this?
        if i == 1:
            # for suit in suits:
            #     new_card = {
            #         "name": "Ace",
            #         "suit": suit,
            #         "value": 1
            #     }
            #     new_cards.append(new_card)
            new_cards = new_cards + [
                {
                    "name": "Ace",
                    "suit": "Hearts",
                    "value": 1
                },
                {
                    "name": "Ace",
                    "suit": "Clubs",
                    "value": 1
                },
                {
                    "name": "Ace",
                    "suit": "Diamonds",
                    "value": 1
                },
                {
                    "name": "Ace",
                    "suit": "Spades",
                    "value": 1
                },
            ]
        elif i == 11:
            # for suit in suits:
            #     new_card = {
            #         "name": "Jack",
            #         "suit": suit,
            #         "value": 10
            #     }
            #     new_cards.append(new_card)
            new_cards = new_cards + [
                {
                    "name": "Jack",
                    "suit": "Hearts",
                    "value": 10
                },
                {
                    "name": "Jack",
                    "suit": "Clubs",
                    "value": 10
                },
                {
                    "name": "Jack",
                    "suit": "Diamonds",
                    "value": 10
                },
                {
                    "name": "Jack",
                    "suit": "Spades",
                    "value": 10
                },
            ]
        elif i == 12:
            # for suit in suits:
            #     new_card = {
            #         "name": "Queen",
            #         "suit": suit,
            #         "value": 10
            #     }
            #     new_cards.append(new_card)
            new_cards = new_cards + [
                {
                    "name": "Queen",
                    "suit": "Hearts",
                    "value": 10
                },
                {
                    "name": "Queen",
                    "suit": "Clubs",
                    "value": 10
                },
                {
                    "name": "Queen",
                    "suit": "Diamonds",
                    "value": 10
                },
                {
                    "name": "Queen",
                    "suit": "Spades",
                    "value": 10
                },
            ]
        elif i == 13:
            # for suit in suits:
            #     new_card = {
            #         "name": "King",
            #         "suit": suit,
            #         "value": 10
            #     }
            #     new_cards.append(new_cards)
            new_cards = new_cards + [
                {
                    "name": "King",
                    "suit": "Hearts",
                    "value": 10
                },
                {
                    "name": "King",
                    "suit": "Clubs",
                    "value": 10
                },
                {
                    "name": "King",
                    "suit": "Diamonds",
                    "value": 10
                },
                {
                    "name": "King",
                    "suit": "Spades",
                    "value": 10
                },
            ]
        # For every number, create a card of each suit whose name and value is the number. 
        else:
            # for suit in suits:
            #     new_card = {
            #         "name": str(i),
            #         "suit": suit,
            #         "value": i
            #     }
            #     new_cards.append(new_card)
            new_cards = new_cards + [
                {
                    "name": str(i),
                    "suit": "Hearts",
                    "value": i
                },
                {
                    "name": str(i),
                    "suit": "Clubs",
                    "value": i
                },
                {
                    "name": str(i),
                    "suit": "Diamonds",
                    "value": i
                },
                {
                    "name": str(i),
                    "suit": "Spades",
                    "value": i
                },
            ]
        new_deck = new_deck + new_cards
    new_deck = new_deck * num_decks # How many decks are mixing?
    return new_deck

# Function to return a random card from the deck and remove that card from the deck
def deal_card(deck):
    return deck.pop(random.randrange(len(deck)))

# Display everyone's current hand
def display_score(your_hand, dealer_hand):
    print("Your hand:")
    for i in range(len(your_hand)):
        message = your_hand[i]["name"] + " of " + your_hand[i]["suit"]
        if i == 0: # keep track of which cards are hidden from your opponents
            message += " (visible)"
        else:
            message += " (hidden)"
        print(message)                          
    print("\nDave's hand:")
    print(dealer_hand[0]["name"] + " of " + dealer_hand[0]["suit"] + " and " + str(len(dealer_hand) - 1) + " hidden card(s)\n")

# Function to find the score of a hand
def get_score(hand):
        total = 0
        aces = [card for card in hand if card["name"] == "Ace"]
        for card in hand:
            total += card["value"]
        if len(aces) >= 1 and total + 10 <= 21:
            total += 10
        return total

# Function for the start of the game. The "home screen" if you will
def begin_game():
    new_game = input("""
    'What's up buddy my name is Disembodied Voice Trapped in a Virtual Hell Prison, but you can call me Dave.
    I'll be your dealer today.
    Since I'm a nice guy I'll let you choose how many decks to use' (enter number from 1 to 10):  """)
    while new_game != "q" and not new_game.isnumeric():
        new_game = input("""
        'Very funny
        Just enter a number from 1 to 10 will ya?' """)
    if new_game == "q":
        return False 
    else:
        num_decks = int(new_game)
        return num_decks


win_messages = [
    "'.....................Shut up'\n",
    "'Listen I had a really long night ok? I'm going through some stuff. This doesn't mean you're better than me'\n",
    "'.......Let's pretend that never happened'\n",
    "'I hate this game'\n",
    "'You're definitely cheating'\n"
]
lose_messages = [
    "'Oof that was super embarrassing for you'\n",
    "'YES in your FACE you suck at this'\n",
    "'Wow you must really enjoy losing money'\n",
    "'Aww poor bb let's go again I'm sure you'll win the next one...'\n",
    "'Ya know sometimes being trapped in here and forced to play blackjack with all you losers isn't so bad'\n"
]
draw_messages = [
    "'How did that even happen??'\n",
    "'Honestly I don't even know what to do here...'\n",
    "'That was weird... but hey at least you didn't win right?'\n",
    "'..............................sorry what happened? I wasn't paying attention'\n"
]
# The middle of the game. Will loop until both players stay, or someone busts. Takes the info returned from begin_game()
def mid_game(num_decks):
    game_in_progress = True
    while game_in_progress: 
        deck = generate_deck(num_decks)
        your_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        print("\nStart!\n")
        display_score(your_hand, dealer_hand)
        while True:
            your_score = get_score(your_hand)
            dealer_score = get_score(dealer_hand)
            if your_score > 21 or dealer_score > 21:
                break
            else:
                answer = input("Wanna hit that? (y/n) ")
                print("\n")
                if answer == "y":
                    print("You hit")
                    your_hand.append(deal_card(deck))
                    if dealer_score < 16:
                        print("Dave hits\n")
                        dealer_hand.append(deal_card(deck))
                    else:
                        print("Dave stays\n")
                    display_score(your_hand, dealer_hand)
                if answer == "n":
                    print("You stay")
                    while dealer_score < 16: # If you stay, dealer hits until he decides not to
                        print("Dave hits")
                        dealer_hand.append(deal_card(deck))
                        dealer_score = get_score(dealer_hand)
                        if dealer_score > 21:
                            break
                    print("Dave stays")
                    break 
                if not answer == "y" and not answer == "n":
                    return False
        print("\nFINAL SCORES")
        print("You: " + str(your_score) + " , " + "Dealer: " + str(dealer_score) + "\n")
        if your_score > 21 and dealer_score > 21:
            print("You and Dave both bust!\n")
            print(draw_messages[random.randrange(4)])     
        elif your_score > 21:
            print("You bust!\n")
            print(lose_messages[random.randrange(5)])
        elif dealer_score > 21:
            print("Dave busts!\n")
            print(win_messages[random.randrange(5)])
        elif your_score == dealer_score:
            print("It's a draw!\n")
            print(draw_messages[random.randrange(4)])
        elif your_score > dealer_score:
            print("You win!\n")
            print(win_messages[random.randrange(5)])
        elif dealer_score > your_score:
            print("Dave wins!\n")
            print(lose_messages[random.randrange(5)])
        inp = input("Play again? (y/n) ")
        if inp != "y":
                game_in_progress = False
        else:
                game_in_progress = True   
                    
    return False


# Start game
inp = input("""
'Welcome friend! 
It's 3pm on a Tuesday and you could be at home with your kids but instead you're here so let's get into it.
Press P to play or press Q at any time to get out of my f*cking casino' """)
if inp == "p":
    game_data = begin_game()
    if game_data: # If begin_game() returns False, quit game
        continue_game = mid_game(game_data)




                    

        


