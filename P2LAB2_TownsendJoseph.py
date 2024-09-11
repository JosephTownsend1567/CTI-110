# Joseph Townsend
# 9/11/2024
# P2LAB2 
# Using Dictionares to store user input and output

#Create a dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S": 110, "Sliverado": 26}

#Get All keys
keys = cars.keys()

#Print all keys
print(keys)

#Get user input and assign to a variable
user_car = input("Enter a vehicle to see it's mpg: ")

print("The", user_car, "gets", cars[user_car], "mpg.")

#Get miles to drive
miles_to_drive = int(input("How many miles will you drive the " + user_car + "?"))

#Calculate gallons needed
gallons_needed = miles_to_drive /cars[user_car]
print(round(gallons_needed, 2), "gallon(s) of gas are needed to drive the", user_car, miles_to_drive, "miles.")
