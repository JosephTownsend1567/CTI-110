# Joseph Townsend
# 9/23/2024
# P4HW1
# Use a loop to add vaild grades to a list

# Track of user scores [list], input, int
# Loop (for) that goes through the the code (range(userinput))
# Ensure that the score is between 0-100, if not then show invalid

# Create an empty list
grade_list = []

# Get the number of scores that user wants to input
num_scores = int(input("How many scores do you want to enter? "))

# For loop to get the values of the scores
for score in range(num_scores):
    num_grade = int(input(f"Enter score #{score+1}: "))
    # If the grade is INVALID. go into while loop
    while num_grade < 0 or num_grade > 100:
        print("INVALID Grade entered!!!\n")
        print("Score should be beteeen 0 and 100\n")
        num_grade = int(input(f"Enter score #{score+1} again:"))
    # While loop breaks, grade is valid, added to the list
    grade_list.append(num_grade)

# All loops are broken
print(f"The valid grades are: {grade_list}")

# Lowest grade
print(f"The Lowest grade is: {min(grade_list)}")

# Remove lowest grade from the list
grade_list.remove(min(grade_list))
print(f"The final grades are: {grade_list}")

