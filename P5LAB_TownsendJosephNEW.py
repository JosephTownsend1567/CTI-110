#Joseph Townsend
#9/30/2024
#P5LAB
#Using random float values to display coins

# Generate random float -> amount owed
# Prompt the user to give amount cash paid
# Input validation
# Calculate change owed (variable)
# Get coins to make change owned

# Import random
import random

# Define disperse_change function (Name)
def disperse_change(change):
    
    # Convert the float value into an integer
    change = int(change * 100)


    if change == 0:
        print("No change due")

    # Calculate the amount of each coin needed
    # Integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels *5)

    num_pennies = change // 1

    # Display coins owed

    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickels > 0:
        print(num_nickels,  end=" ")
        if num_nickels == 1:
            print("Nickel")
        else:
            print("Nickels")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")
        
# Create the main function
def main():
    # Generate random float
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"The total for purchase is ${total_owed:.2f}")

    # Prompt user to give amount paid
    amount_paid = float(input("Enter amount to pay: $"))

    # Calculate changed owed
    change_owed = amount_paid - total_owed
    print(f"Change owed to customer: ${change_owed:.2f}")
    print()
    
    # Call the disperse_change function
    disperse_change(change_owed)
    
    
# Calling the main function
if __name__ == "__main__":
    main()
    
