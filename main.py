from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.") 

auction_dic = {}
auction_open = True
   
while auction_open:
  name = input("What is your name? ") 
  bid = input("What's your bid? ")
  bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  auction_dic[name] = float(bid.replace("$",""))
  if bidders == "yes":
    auction_open = True
    clear()
  else:
    auction_open = False
    best_bid = 0 
    for bidder in auction_dic:
      if auction_dic[bidder] > best_bid:
        best_bid = auction_dic[bidder]
    print(f"The winner is {bidder} with a bid of ${best_bid}0.")