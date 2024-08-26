import time

print("Give random number of fibonacci code")

time.sleep(0)

print("and this program will give u back 10 numbers before and after")

time.sleep(0)

while True:

    try:
        fibonacci_start_number = int(input("Your number: "))
        break
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        ammount_piervus = int(input("how many of piervus numbers u want?: "))
        break
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        ammount_next = int(input("how many of next numbers u want?: "))
        break
    except ValueError:
        print("Please enter a valid number.")






fibonacci_piervus_number1 = 0
fibonacci_piervus_number2 = 1

while True:
    fibonacci_piervus_number = fibonacci_piervus_number1 + fibonacci_piervus_number2

    if fibonacci_start_number <= fibonacci_piervus_number:
        break


    fibonacci_piervus_number1 = fibonacci_piervus_number2
    fibonacci_piervus_number2 =  fibonacci_piervus_number
