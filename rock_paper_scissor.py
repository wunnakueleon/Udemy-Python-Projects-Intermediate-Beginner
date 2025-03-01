import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# user choice

user_choice = input('Rock, Paper, Scissors. Choose one: ').lower()
user_index = ['rock', 'paper', 'scissors'].index(user_choice)
if user_choice == 'rock':
    print(f'You chose {rock}')
elif user_choice == 'paper':
    print(f'You chose {paper}')
else:
    print(f'You chose {scissors}')

# computer_choice

choices = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

print(f'The computer chose {choices[computer_choice]}')

wins_and_losses = [['Tie', 'You lose', 'You win'], ['You win', 'Tie', 'You lose'], ['You lose', 'You win', 'Tie']]

print(f'{wins_and_losses[user_index][computer_choice]}')
