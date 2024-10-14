# Joseph Townsend
# 9/16/24
# P2HW2
# Understanding of Lists

# Gets input from user
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Creates a list with user input
modulelist = [module1, module2, module3, module4, module5, module6]


print()
print("---------Results---------")

print(f'{"Lowest Grade: ":<20}{min(modulelist):.2f}')
print(f'{"Highest Grade: ":<20}{max(modulelist):.2f}')
print(f'{"Sum of Grades: ":<20}{sum(modulelist):.2f}')
print(f'{"Average: ":<20}{sum(modulelist)/len(modulelist):.2f}')

print("----------------------------------------")


