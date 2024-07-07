
bids={}
bidding_finished=False
highest_bid=0
winner=""
def find_highest_bidder(bidding_record):
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner =bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name=input("What is your name? ")
    price=int(input("What is your bid? $"))
    bids[name]=price
    should_continue= input("Are there any othher bidders? type 'Yes' or 'No'")
    if should_continue=="No":
        bidding_finished = True
