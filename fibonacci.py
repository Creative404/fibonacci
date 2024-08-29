import time

print("Give random number of fibonacci code")

time.sleep(0)

print("and this program will give u back 10 numbers before and after")

time.sleep(0)

#examples
Fibonacci_examples1=0
Fibonacci_examples2=1
Fibonacci_examples_ammount = 0
Fibonacci_examples0 = []

while Fibonacci_examples_ammount != 20:
    Fibonacci_examples = Fibonacci_examples1 + Fibonacci_examples2
    Fibonacci_examples0.append(Fibonacci_examples)
    Fibonacci_examples1 = Fibonacci_examples2
    Fibonacci_examples2 = Fibonacci_examples
    Fibonacci_examples_ammount += 1



while True:

    try:
        fibonacci_start_number = int(input("Your number: "))
        break
    except ValueError:
        print("Please enter a valid number.")



def looking_for_piervus(fibonacci_start_number):

    fibonacci_piervus_number1 = 0
    fibonacci_piervus_number2 = 1

    while True:
        fibonacci_piervus_number = fibonacci_piervus_number1 + fibonacci_piervus_number2

        if fibonacci_start_number <= fibonacci_piervus_number:
            return fibonacci_piervus_number2


        fibonacci_piervus_number1 = fibonacci_piervus_number2
        fibonacci_piervus_number2 =  fibonacci_piervus_number

    #idk what im doing


#fibonacic checker

fibonacic_checker = looking_for_piervus(fibonacci_start_number)
fibonacic_checker2 = looking_for_piervus(fibonacic_checker)

if fibonacci_start_number != fibonacic_checker + fibonacic_checker2:
    print("Please enter a valid fibonacci number.")
    while True:
        try:
            fibonacci_start_number = int(input("Your number: "))

            fibonacic_checker = looking_for_piervus(fibonacci_start_number)
            fibonacic_checker2 = looking_for_piervus(fibonacic_checker)

            if fibonacci_start_number == fibonacic_checker + fibonacic_checker2:
                break
            print("Please enter a valid fibonacci number.")
        except ValueError:
            print("Please enter a valid number.")


while True:
    try:
        ammount_piervus = int(input("how many of piervus numbers u want?: "))
        if ammount_piervus > 5 or ammount_piervus < 1:
            print("have mercy pick something between 1-5")
            continue
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        ammount_next = int(input("how many of next numbers u want?: "))
        if ammount_next > 5 or ammount_next < 1:
            print("have mercy pick something between 1-5")
            continue
        else:
            break
    except ValueError:
        print("Please enter a valid number.")


#massife sitty if's
piervus =  looking_for_piervus(fibonacci_start_number)
if piervus >= 0 and ammount_piervus >= 1:
    Checker = True
    ammount_piervus -=1

piervus1 =  looking_for_piervus(piervus)
if piervus1 >= 0 and ammount_piervus >= 1:
    Checker = False
    Checker1 = True
    ammount_piervus -=1

piervus2 =  looking_for_piervus(piervus1)
if piervus1 >= 0 and ammount_piervus >= 1:
    Checker = False
    Checker1 = False
    Checker2 = True
    ammount_piervus -=1

piervus3 =  looking_for_piervus(piervus2)
if piervus1 >= 0 and ammount_piervus >= 1:
    Checker = False
    Checker1 = False
    Checker2 = False
    Checker3 = True
    ammount_piervus -=1

piervus4 =  looking_for_piervus(piervus3)
if piervus1 >= 0 and ammount_piervus >= 1:
    Checker = False
    Checker1 = False
    Checker2 = False
    Checker3 = False
    Checker4 = True
    ammount_piervus -=1

if Checker == True:
    sum = str(fibonacci_start_number)
    sum1 = str(piervus)
    User_and_piervus = sum + " " + sum1
    print(User_and_piervus)

elif Checker1 == True:
    sum = str(fibonacci_start_number)
    sum1 = str(piervus)
    sum2 = str(piervus1)
    User_and_piervus = sum + " " + sum1 + " " + sum2
    print(User_and_piervus)

elif Checker2 == True:
    sum = str(fibonacci_start_number)
    sum1 = str(piervus)
    sum2 = str(piervus1)
    sum3 = str(piervus2)
    User_and_piervus = sum + " " + sum1 + " " + sum2 + " " + sum3
    print(User_and_piervus)

elif Checker3 == True:
    sum = str(fibonacci_start_number)
    sum1 = str(piervus)
    sum2 = str(piervus1)
    sum3 = str(piervus2)
    sum4 = str(piervus3)
    User_and_piervus = sum + " " + sum1 + " " + sum2 + " " + sum3 + " " + sum4
    print(User_and_piervus)

elif Checker4 == True:
    sum = str(fibonacci_start_number)
    sum1 = str(piervus)
    sum2 = str(piervus1)
    sum3 = str(piervus2)
    sum4 = str(piervus3)
    sum5 = str(piervus4)
    User_and_piervus = sum + " " + sum1 + " " + sum2 + " " + sum3 + " " + sum4 + " " + sum5
    print(User_and_piervus)
