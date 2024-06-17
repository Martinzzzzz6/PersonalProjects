# two_digit_number = input()
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]

# print(int(first_digit) + int(second_digit))



# height = input()
# weight = input()

# print("Your bmi is: " + str(int(weight)/(int(height)**2)))


# year = input()
# if int(year) % 4 == 0 & (int(year) % 100 != 0 | int(year) % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")


size = input("What size of pizza do you want? S, M, L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size.lower() == 's':
    bill = 15
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill += 2
    else:
        bill += 0
    if extra_cheese == 'Y' or extra_cheese == 'y':
        bill += 1
    else:
        bill += 0
elif size.lower() == 'm':
    bill = 20
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill += 3
    else:
        bill += 0
    if extra_cheese == 'Y' or extra_cheese == 'y':
        bill += 1
    else:
        bill += 0
elif size.lower() == 'l':
    bill = 25
    if add_pepperoni == 'Y' or add_pepperoni == 'y':
        bill += 3
    else:
        bill += 0
    if extra_cheese == 'Y' or extra_cheese == 'y':
        bill += 1
    else:
        bill += 0


print(f"Your final bill is: ${bill}")