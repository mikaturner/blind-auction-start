from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.") 

name = input("What is your name? ") 
bid = input("What's your bid? ")
bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

auction_dic = {}

def secret_auction(name, bid, bidders):
  best_bid = 0  
  if bidders == "yes":
    auction_open = True
  else:
    auction_open = False
  
  while auction_open:
    auction_dic[name] = float(bid.replace("$",""))
    print(auction_dic)
    
    name = input("What is your name? ") 
    bid = input("What's your bid? ")
    bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
    clear()
    secret_auction(name, bid, bidders)
  
  for bidder in auction_dic:
      if auction_dic[bidder] > best_bid:
        best_bid = auction_dic[bidder]
  print(f"The winner is {bidder} with a bid of {best_bid}.")
secret_auction(name, bid, bidders)