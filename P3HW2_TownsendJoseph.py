# Joseph Townsend
# 9/18/202
# P3HW2
# Calculate payrate using if/else statements

#get_name - string
#hours_worked - int
#pay_rate - float
# Each one needs a variable
# OT - anything over 40 hours (if (hours_worked)>40: //has OT)
# Else: //no OT
# OT payrate - rat * 15
# 2 payrates (regular pay and overtime pay)
# overtime pay - regular pay = total (overtime)
# overtime hours - hours(40) * pay rate =
# OT_payrate = 1.5 * pay_rate

name = input("Enter employee's name: ")
hours = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#Display name (\n can be used to seperate lines)
print("------------------------------\nEmployee name: ", name)

#Determine employee pay

if hours > 40:
    #They have some overtime
    reg_pay_amt = 40 * pay_rate
    ot_pay_rate = 1.5 * pay_rate
    ot_hours = hours - 40
    ot_pay_amt = (ot_hours) * ot_pay_rate
    
else:
    #No overtime
    reg_pay_amt = hours * pay_rate
    ot_hours = 0
    ot_pay_amt = 0

# Calculate the gross pay
gross_pay = reg_pay_amt + ot_pay_amt

print()

# Display headings (F strings dont use commas, curly braces seprate them)
print(f"{'Hours Worked':<16}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print("-" * 100)
# Formats the result)
print(f"{hours:<16.1f}${pay_rate:<12.2f}{ot_hours:<10.1f}${ot_pay_amt:<14.2f}${reg_pay_amt:<14.2f}${gross_pay:<15.2f}")

