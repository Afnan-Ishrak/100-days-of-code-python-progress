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
    def comp_draw():
        comp_card_drawn = random.choice(ranks)
        comp_suit_drawn = random.choice(suits)
        computer_cardhand.append(comp_card_drawn)
        computer_suithand.append(comp_suit_drawn)
    comp_draw()
        

    def draw_cards(number):
        suits_draw = []
        cards_draw = []
        for x in range(number):
            suit_drawn = random.choice(suits)
            card_drawn = random.choice(ranks)
            cards_draw.append(card_drawn)
            suits_draw.append(suit_drawn)
        return cards_draw, suits_draw

    cards_drawn_1, suit_drawn1 = draw_cards(2)

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


    # print(f"Your hand is \n{cards_drawn_1[0]} of {suit_drawn1[0]} \nand \n{cards_drawn_1[1]} of {suit_drawn1[1]}")

    # print("*"*40, f"\nComputer's Hand is \n{computer_cardhand[0]} of {computer_suithand[0]} \nand \n***** of *****")

    def hit():
        hits = draw_cards(1)
        new_card, new_suit = hits
        print(f"\nYour new card is {new_card[0]} of {new_suit[0]}")
        cards_drawn_1.append(new_card[0]), suit_drawn1.append(new_suit[0])
        return cards_drawn_1, suit_drawn1

    def card_review(player_score, comp_score):
        print("\nYour cards are:\n")
        for x in cards_drawn_1:
            suit_index = cards_drawn_1.index(x)
            print(f"{x} of {suit_drawn1[suit_index]}")
        print(f"Player Score : '{player_score}'")
        print("*"*40)
        print("Computer's cards are:\n")
        for x in computer_cardhand:
            suit_index = computer_cardhand.index(x)
            print(f"{x} of {computer_suithand[suit_index]}")
        print(f"Computer Score : '{comp_score}'")

    def hit_stand():
        hit_stand = input("Do you want to Hit(h) or Stand(s)?\n").lower()
        return hit_stand


    player_hand_value = value_calc(cards_drawn_1)
    comp_hand_value = value_calc(computer_cardhand)
    bust = False

    card_review(player_hand_value, comp_hand_value)

    val_hand = value_calc(cards_drawn_1)
    bj = True
    if val_hand == 21:
        bj = False
        print("You hit BLACKJACK!!!. You win! 🤑🎉")

    hs_input = ""
    while player_hand_value < 21 and hs_input != "s":
        hs_input = hit_stand()
        if hs_input == "h":
            hit()

        if hs_input == "s":
            while comp_hand_value <= 17:
                comp_draw()
                comp_hand_value = value_calc(computer_cardhand)
                
        player_hand_value = value_calc(cards_drawn_1)
        comp_hand_value = value_calc(computer_cardhand)
        card_review(player_hand_value, comp_hand_value)
        
    if player_hand_value > 21:
        print("Yikes. you busted! 😬")
        bust = True

    if comp_hand_value < 21 and player_hand_value > comp_hand_value and bust != True and bj:
        print("Congratulations! You Win. 😤")

    if comp_hand_value > 21:
        print("Congratulations! Dealer busted. You Win. 😎")

    if comp_hand_value == player_hand_value:
        print("You tied! 😲")

    if comp_hand_value > player_hand_value and comp_hand_value <= 21:
        print("Sorry. You lost. 😰")

blackjack()
replay = input("Do you want to play another game of blackjack?\n").lower()
stop_game = False
while stop_game == False and replay == "yes" or replay == "y":
    cls()
    blackjack()
    replay = input("Do you want to play another game of blackjack?\n").lower()
    if replay == "no" or replay == "n":
        print("Thank you for playing with us! 😉")
        stop_game = True