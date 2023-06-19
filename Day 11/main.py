############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
import art
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def blackjack():
    print(art.logo)

    suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    computer_cardhand = []
    computer_suithand = []
    player_cards_draw = []   
    player_suits_draw = []

    def draw_cards(number, card, suit):
        card = []
        suit = []
        for x in range(number):
            suit_drawn = random.choice(suits)
            card_drawn = random.choice(ranks)
            card.append(card_drawn)
            suit.append(suit_drawn)
        return card, suit

    player_cards_drawn, player_suit_drawn = draw_cards(2, player_cards_draw, player_suits_draw)

    computer_cards_drawn, computer_suit_drawn = draw_cards(1, computer_cardhand, computer_suithand)

    def value_calc(value_card):
        values_drawn_1 = [value[ranks.index(card)] for card in value_card]
        sum = 0
        for val in values_drawn_1:
            sum += val
        ace = 'Ace' in value_card
        while sum > 21 and ace:
            sum -= 10
            ace = False
        return sum

    def hit(card_draw, suit_draw, card_drawn, suit_drawn, player_cards_draw):
        hits = draw_cards(1, card_draw, suit_draw)
        new_card, new_suit = hits
        if player_cards_draw is not None:
            print(f"\nYour new card is {new_card[0]} of {new_suit[0]}")
        card_drawn.append(new_card[0]), suit_drawn.append(new_suit[0])
        return card_drawn, suit_drawn

    def card_review(player_score, comp_score):
        print("\nYour cards are:\n")
        for x in player_cards_drawn:
            suit_index = player_cards_drawn.index(x)
            print(f"{x} of {player_suit_drawn[suit_index]}")
        print(f"Player Score : '{player_score}'")
        print("*"*40)
        print("Computer's cards are:\n")
        for x in computer_cards_drawn:
            suit_index = computer_cards_drawn.index(x)
            print(f"{x} of {computer_suit_drawn[suit_index]}")
        print(f"Computer Score : '{comp_score}'")

    player_hand_value = value_calc(player_cards_drawn)
    comp_hand_value = value_calc(computer_cards_drawn)
    card_review(player_hand_value, comp_hand_value)
    bj = False
    if player_hand_value == 21:
        bj = True
        print("You hit BLACKJACK!!!. You win! 🤑🎉")
    hs_input = ""
    while player_hand_value < 21 and hs_input != "s":
        hs_input = input("Do you want to Hit(h) or Stand(s)?\n").lower()
        if hs_input == "h":
            hit(player_cards_draw, player_suits_draw, player_cards_drawn, player_suit_drawn, 0)

        elif hs_input == "s":
            while comp_hand_value < 17:
                var = None
                hit(computer_cardhand, computer_suithand, computer_cards_drawn, computer_suit_drawn, var)
                comp_hand_value = value_calc(computer_cards_drawn)
                
        player_hand_value = value_calc(player_cards_drawn)
        comp_hand_value = value_calc(computer_cards_drawn)
        card_review(player_hand_value, comp_hand_value)
        
    if player_hand_value > 21:
        print("Yikes. you busted! 😬")

    if comp_hand_value < 21 and player_hand_value > comp_hand_value and player_hand_value <= 21 and bj == False:
        print("Congratulations! You Win. 😤")

    if comp_hand_value > 21:
        print("Congratulations! Dealer busted. You Win. 😎")

    if comp_hand_value == player_hand_value:
        print("You tied! 😲")

    if comp_hand_value > player_hand_value and comp_hand_value <= 21:
        print("Sorry. You lost. 😰")

blackjack()
stop_game = False
while stop_game == False:
    replay = input("Do you want to play another game of blackjack?\n").lower()
    cls()
    blackjack()
    if replay == "no" or replay == "n":
        print("Thank you for playing with us! 😉")
        stop_game = True
