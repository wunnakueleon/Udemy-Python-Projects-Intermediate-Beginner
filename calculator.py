# This program is a calculator program using functions and recursion

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
    return n1+n2


def subtract(n1,n2):
    return n1-n2


def multiply(n1,n2):
    return n1*n2


def divide(n1,n2):
    return n1/n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)
    first_num = float(input('What is your first number: '))

    calculation = True
    while calculation:
        signs = input('Input operation; ')
        second_num = float(input('What is another number: '))
        resulted_number = operations[signs](first_num, second_num)
        print(resulted_number)

        yes_no = input("Do you wanna continue? If yes, type 'y'. If not, type 'n'").lower()
        if yes_no == 'y':
            first_num = resulted_number

        else:
            calculation = False
            print('\n' * 5)
            calculator()


calculator()


