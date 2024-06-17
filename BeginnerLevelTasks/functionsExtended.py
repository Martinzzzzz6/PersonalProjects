# def greet_with_name(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# input_name = input("Enter your name: ")
# input_location = input("Enter your location: ")
# greet_with_name(input_name, input_location)

# import math

# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil(((height * width) / cover))
#     print(f"You'll need {number_of_cans} cans of paint")

# paint_calc(height = 3, width = 9, cover = 5)


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
        return True
    