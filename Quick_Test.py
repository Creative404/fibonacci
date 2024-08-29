a = 1
b = 1
c = 1

while a != b + c:
    try:
        a = int(input("Your number: "))
        if a == b + c:
            break
        print("Please enter a valid number.")
    except ValueError:
        print("Please enter a valid number.")

print("works")