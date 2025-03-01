# The player will have to choose left or right decision.
# His/her choice will determine survival.
# 'if/else' statement is applied.


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()

if choice1 == 'left':
    choice2 = input('Swim or Wait\n').lower()
    if choice2 == 'wait':
        choice3 = input('Red, Blue and Yellow. Which door?\n').lower()
        if choice3 == 'red':
            print('Burned by fire.\nGame Over...')
        elif choice3 == 'yellow':
            print('Fall into deep gold mine.\nGame Over...')
        elif choice3 == 'blue':
            print("You've won! Congratulations...")
        else:
            print("Game Over...")
    else:
        print('Attacked by trout.\nGame Over...')
else:
    print('Fall into a hole.\nGame Over...')
