# This project will determine which year is a leap year.
# 'if/else' statement is applied.

year = int(input('Enter the year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Leap Year')
        else:
            print('Not Leap Year')
    else:
        print('Leap Year')
else:
    print('Not Leap Year')

