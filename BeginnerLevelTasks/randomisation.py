import random 

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is: {love_score}")


# Challenge:
# Write a program that will randomly select a person from a list of names.
# The person selected will have to pay for everyone's meal.
# Example Input:
# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
# Output:
# Michael is going to buy the meal today!
names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")

# Flip a coin
choices = ["Heads", "Tails"]
random_choice = random.choice(choices)
print(random_choice)

random_number_choice = random.randint(1,2)
print(random_number_choice)
if random_number_choice == 1:
    print("Heads")
else:
    print("Tails")