import time
time.sleep(0.5)
print("This program will give you up to 5 previous numbers \nAnd up to 20 next numbers\n")

#examples
Fibonacci_examples1=0
Fibonacci_examples2=1
Fibonacci_examples_ammount = 0
Fibonacci_examples0 = []
while Fibonacci_examples_ammount != 10:
    Fibonacci_examples = Fibonacci_examples1 + Fibonacci_examples2
    Fibonacci_examples0.append(Fibonacci_examples)
    Fibonacci_examples1 = Fibonacci_examples2
    Fibonacci_examples2 = Fibonacci_examples
    Fibonacci_examples_ammount += 1

time.sleep(3)
print("Type random number of *fibonacci*")
time.sleep(1)
print("examples of *fibonacci* numbers:")
print(Fibonacci_examples0)
print()
time.sleep(4)

while True:
    try:
        fibonacci_start_number = int(input("Your *start* number: "))
        break
    except ValueError:
        time.sleep(0.1)
        print()
        print("Please enter a valid number.\n")

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
    time.sleep(0.5)
    print("Please enter a valid *fibonacci* number from examples:\n")
    time.sleep(0.5)
    print("Examples of Fibonacci numbers: \n")
    print(Fibonacci_examples0)
    print()
    time.sleep(0.5)
    while True:
        try:
            fibonacci_start_number = int(input("Your number: "))
            #fibonacic checker v2
            fibonacic_checker = looking_for_piervus(fibonacci_start_number)
            fibonacic_checker2 = looking_for_piervus(fibonacic_checker)
            if fibonacci_start_number == fibonacic_checker + fibonacic_checker2:
                break
            time.sleep(0.5)
            print("Please enter a valid *fibonacci* number from examples:\n")
            time.sleep(0.5)
            print("Examples of Fibonacci: \n")
            print(Fibonacci_examples0)
        except ValueError:
            print("Please enter a valid number.\n")
            time.sleep(0.5)

while True:
    try:
        time.sleep(0.5)
        print()
        ammount_piervus = int(input("how many of *previous* numbers u want?: "))
        if ammount_piervus > 5 or ammount_piervus < 1:
            print("have mercy pick something between 1-5")
            continue
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        time.sleep(0.5)
        ammount_next = int(input("how many *next* numbers u want?: "))
        time.sleep(0.5)
        if ammount_next > 20 or ammount_next < 0:
            print("Pick something between 0-20\n")
            continue
        else:
            break
    except ValueError:
        time.sleep(0.5)
        print("Please enter a valid number.\n")

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

#at this point this are still int's
if piervus <=1:
    Checker = True
    Checker1 = False
    Checker2 = False
    Checker3 = False
    Checker4 = False
elif piervus1 <=1:
    Checker = False
    Checker1 = True
    Checker2 = False
    Checker3 = False
    Checker4 = False
elif piervus2 <=1:
    Checker = False
    Checker1 = False
    Checker2 = True
    Checker3 = False
    Checker4 = False
elif piervus3 <=1:
    Checker = False
    Checker1 = False
    Checker2 = False
    Checker3 = True
    Checker4 = False
elif piervus3 <=1:
    Checker = False
    Checker1 = False
    Checker2 = False
    Checker3 = False
    Checker4 = True

#at this point this are still int's (last warning)
if Checker == True:
    User_and_piervus = []
    User_and_piervus.append(piervus)
    User_and_piervus.append(fibonacci_start_number)

elif Checker1 == True:
    User_and_piervus = []
    User_and_piervus.append(piervus1)
    User_and_piervus.append(piervus)
    User_and_piervus.append(fibonacci_start_number)

elif Checker2 == True:
    User_and_piervus = []
    User_and_piervus.append(piervus2)
    User_and_piervus.append(piervus1)
    User_and_piervus.append(piervus)
    User_and_piervus.append(fibonacci_start_number)

elif Checker3 == True:
    User_and_piervus = []
    User_and_piervus.append(piervus3)
    User_and_piervus.append(piervus2)
    User_and_piervus.append(piervus1)
    User_and_piervus.append(piervus)
    User_and_piervus.append(fibonacci_start_number)

elif Checker4 == True:
    User_and_piervus = []
    User_and_piervus.append(piervus4)
    User_and_piervus.append(piervus3)
    User_and_piervus.append(piervus2)
    User_and_piervus.append(piervus1)
    User_and_piervus.append(piervus)
    User_and_piervus.append(fibonacci_start_number)

ammount_next_Backup = ammount_next
User_and_next = []
while True:
    next_fibonacci = piervus + fibonacci_start_number
    if ammount_next <= 0:
        break
    User_and_next.append(next_fibonacci)
    fibonacci_start_number = next_fibonacci
    piervus = fibonacci_start_number
    ammount_next -= 1
time.sleep(0.5)
print("This is your *fibonacci** numbers:")
time.sleep(0.2)
print(User_and_piervus + User_and_next)
print()
time.sleep(1)
input("press any button to exit")