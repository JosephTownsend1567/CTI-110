# Joseph Townsend
# 9/25/2024
# P4LAB2
# Using a while loop with a for loop

# Get integer from user (only non negative, 1 to 12)
# tell the user it cannot accept negaitve values
# prompt user to run the program again (while loop***)
# type "yes" it runs again, "no" it ends

# Create a loop that runs until the user enters
run_again = ""

while run_again != "no":
    
    usr_num = int(input("Enter an integer: "))
    print()
    if usr_num < 0:
        print("This program doesn't handle negative numbers")
    else:
        for num in range(12):
            print(f"usr_num * {num+1} = {usr_num * (num+1)}")
            
    run_again = input("Would you like to run the program again?\n")

# loop ends
print("\nGoodbye\n")
