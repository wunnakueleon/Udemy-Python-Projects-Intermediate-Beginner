import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def blackjack():
    def randomization():

        cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q']

        cards_random = cards[random.randint(0, len(cards) - 1)]
        return cards_random

    play_blackjack = input('Do you wanna play Blackjack?\nIf yes, type "y"; if no, type "n":').lower()
    player_cards = []
    computer_cards = []
    if play_blackjack == 'y':
        for x in range(2):
            player_cards.append(randomization())
        for x in range(2):
            computer_cards.append(randomization())

        print(f"Your cards: {player_cards}")
        print(f"Computer cards: [{computer_cards[0]}, __]")

        player_points = 0
        for x in player_cards:
            if isinstance(x, (int, float)):
                player_points += x
            elif x in ['J', 'K', 'Q']:
                player_points += 10
            elif x == 'A':
                player_points += 11

        computer_points = 0
        for x in computer_cards:
            if isinstance(x, (int, float)):
                computer_points += x
            elif x in ['J', 'K', 'Q']:
                computer_points += 10
            elif x == 'A':
                computer_points += 11

        limit = True
        while limit:
            if player_points < 21 and computer_points < 21:
                draw_cards = True
                while draw_cards:
                    draw_cards = input('Would you like to Hit or Stand?\nType "hit" or "stand"').lower()
                    if draw_cards == 'hit':
                        player_cards.append(randomization())
                        player_points = 0
                        for x in player_cards:
                            if isinstance(x, (int, float)):
                                player_points += x
                            elif x in ['J', 'K', 'Q']:
                                player_points += 10
                            elif x == 'A':
                                player_points += 11
                        print(player_cards)
                    if player_points > 21 or player_cards == 21:
                        draw_cards = False

                    else:
                        if player_points < computer_points:
                            print('The Computer has won!')
                        elif player_points > computer_points:
                            print('You have won!')
                        print(f'Computer cards: {computer_cards}')
                        draw_cards = False
            else:
                if player_points < computer_points:
                    print('The Computer has won!')
                elif player_points > computer_points:
                    print('You have won!')
                elif player_points > 21:
                    print('You have lost. Your cards exceed 21.')
                elif player_points == 21:
                    print('You have won')
                elif player_points == computer_points:
                    print('A Draw!!')
                elif computer_points > 21:
                    print('The Computer has lost. The cards exceed 21.')
                elif computer_points == 21:
                    print('The Computer has won!')
                limit = False

        print(f'Computer cards: {computer_cards}')
        blackjack()


blackjack()
