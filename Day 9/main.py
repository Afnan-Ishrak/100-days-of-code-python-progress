import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
import art
print(art.logo)
print("                 WELCOME TO THE BLIND AUCTION!!!!!")
print("*"*30)
bid_info = []
def bid_game():
    def new_bidder(name, bid_price):
        new_bid = {
            "name": name,
            "bid": bid_price,
            }
        bid_info.append(new_bid)
        
    bidder_name = input("What is your name?\n-")
    bid_amount = input("How much are you willing to bid?\n$")

    new_bidder(name=bidder_name, bid_price=bid_amount)
bid_game()


zero = 0
while zero==0:
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no:\n").lower()
    if repeat == "yes":
        cls()
        bid_game()
    else:
        cls()
        lst = []
        for x in bid_info: 
            bid_numbers = int(x["bid"])
            lst.append(bid_numbers)
        largest_number = max(lst)
        ln_index = lst.index(largest_number)
        name_index = bid_info[ln_index]
        highest_bidder_name = name_index["name"]
        print(f"The Highest bidder is {highest_bidder_name} with ${largest_number}.Congrats on your win!!")
        zero += 1
        