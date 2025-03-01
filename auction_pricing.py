logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

continue_auction = True
participants = {}
bid = 0

while continue_auction:
    bidder_name = str(input("What's the bidder's name?: "))
    bidder_price = int(input('Insert the amount: $ '))
    participants[bidder_name] = bidder_price

    end_auction = input("Do you want to end the auction? Yes or No?\n").lower()
    if end_auction == 'no':
        continue
    else:
        for highest_bidder in participants:
            if participants[highest_bidder] > bid:
                winner = highest_bidder
                bid = participants[highest_bidder]
        print(f'The winner is {winner} with ${bid}.')
        continue_auction = False
