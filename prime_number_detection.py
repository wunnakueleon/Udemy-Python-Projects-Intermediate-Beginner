# Prime Number Checker
# def function is applied.

def prime_checker(number):

    if number == 2 or number == 3:
        return True

    else:
        if number % 2 == 0 or number % 3 == 0:
            return False
        return True


num = int(input('Insert the number here: '))
if prime_checker(num):
    print("It's a prime number.")
else:
    print(f"{num} is not a prime number.")
