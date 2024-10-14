
# Joseph Townsend
# 9/9/2024
# P1HW2
# Using IDLE to create and test a program
print("This program calculates and displays travel expenses")
print()
budget = int(input("Enter budget: "))
print()
travel = input("Enter your travel destination: ")
print()
gas = int(input("How much do you think you will spend on gas? "))
print()
hotel = int(input("How much will you need for accomodation/hotel? "))
print()
food = int(input("Last, how much do you need for food? "))
print()
print("------------Travel Expenses------------")
print("Location:", travel)
print("Initial Budget:", f"${budget: .2f}")
print("Fuel:", f"${gas: .2f}")
print("Accomodation:", f"${hotel: .2f}")
print("Food:",f"${food: .2f}")
print()
print("Remaining Balance:", f"${budget - gas - hotel - food: .2f}")

