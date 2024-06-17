print("Love calclulator:")
name1 = input("Enter your name: ")
name2 = input("Enter their name: ")

concatenated_names = name1 + name2
lower_case_names = concatenated_names.lower()
countL = lower_case_names.count('l')
countO = lower_case_names.count('o')
countV = lower_case_names.count('v')
countE = lower_case_names.count('e')
countT = lower_case_names.count('t')
countR = lower_case_names.count('r')
countU = lower_case_names.count('u')

total_love = countL + countO + countV + countE
total_true = countT + countR + countU + countE

print(f"Your love score is: {str(total_true) + str(total_love)}")