# diddy_party = ["Meek Mill", "Usher", "Chris Brown", "Epstein"]

# for diddy in diddy_party:
#     print(diddy)

# list_of_grades = [90, 78, 65, 45, 80, 100, 95, 85, 70, 60, 55, 40, 30, 20, 10]
# find_max_number = 0
# for grade in list_of_grades:
#     if grade > find_max_number:
#         find_max_number = grade

# print(find_max_number)

sum = 0
for number in range(1, 101):
    sum += number
print(sum)

sum_even = 0
for even in range(1,101):
    if even % 2 == 0:
        sum_even += even
print(sum_even)

sumEven = 0
for even in range(2, 101, 2):
    sumEven += even
print(sumEven)


for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print ("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)