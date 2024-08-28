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

piervus_list = []

def looking_for_piervus(fibonacci_start_number):

    fibonacci_piervus_number1 = 0
    fibonacci_piervus_number2 = 1

    while True:
        fibonacci_piervus_number = fibonacci_piervus_number1 + fibonacci_piervus_number2

        if fibonacci_start_number <= fibonacci_piervus_number:
            return fibonacci_piervus_number2


        fibonacci_piervus_number1 = fibonacci_piervus_number2
        fibonacci_piervus_number2 =  fibonacci_piervus_number
        #print(fibonacci_piervus_number)
    #idk what im doing



#massife sitty if's
piervus =  looking_for_piervus(fibonacci_start_number)
if piervus >= 0 and ammount_piervus >= 1:
    piervus_list.append(piervus) #this cant be bigger than this
    print(piervus_list)
    ammount_piervus -=1

piervus1 =  looking_for_piervus(piervus)
if piervus1 >= 0 and ammount_piervus >= 1:
    piervus_list.append(piervus1)
    print(piervus_list)
    ammount_piervus -=1

piervus2 =  looking_for_piervus(piervus1)
if piervus1 >= 0 and ammount_piervus >= 1:
    piervus_list.append(piervus2)
    print(piervus_list)
    ammount_piervus -=1

piervus3 =  looking_for_piervus(piervus2)
if piervus1 >= 0 and ammount_piervus >= 1:
    piervus_list.append(piervus3)
    print(piervus_list)
    ammount_piervus -=1

piervus4 =  looking_for_piervus(piervus3)
if piervus1 >= 0 and ammount_piervus >= 1:
    piervus_list.append(piervus4)
    print(piervus_list)
    ammount_piervus -=1

#remeber add pop ad put it in order and in if's
#pop remove last - (its for me dot read this shi-)





