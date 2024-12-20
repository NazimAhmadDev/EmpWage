import random

print("Welcome to Employee Wage Computation Program on Master Branch")



# UC-1
def check_status(name):
    status = random.choice(['Present','Absent'])
    print(f"{name} is {status}")
    return status


# UC-2
def daily_wage(name,wage_per_hour,full_day_hour):
    # Checking status of employee is present or absent
    status = check_status(name)

    if(status == 'Present'):
        amount = wage_per_hour * full_day_hour
        print(f"Your wage is ${amount}")
        return amount
    else:
        print(f"You don't get your todays wage!!!")
    return 0

# UC-3
def Add_partTime_wage(name,amount,wage_per_hour,partTime_hour):
    # Calculating part time wage
    partTime_wage = wage_per_hour * partTime_hour

    # Checking if employee is present in part time 
    status = check_status(name)
    if(status == 'Present'):
        new_amount = amount + partTime_wage
        print(f"Your part time amount is also added : ${new_amount}")
        return new_amount
    else:
        print(f"Your amount is :",amount)
    return 0


# Uc-5
def calculate_monthly_wage(name,wage_per_hour,full_day_hour,partTime_hour):
    monthly_wage = 0
    working_days = 20
    partTime_days = 10

    for day in range(1, working_days + 1):
        print(f"\nDay {day}:")
        # Check daily status
        amount = daily_wage(name, wage_per_hour, full_day_hour)
        
        # Add part-time wage if he is present
        if day <= partTime_days:  
            amount = Add_partTime_wage(name, amount, wage_per_hour, partTime_hour)
        
        monthly_wage += amount

    print(f"\n{name}'s total monthly wage is: ${monthly_wage}")
    return monthly_wage

# UC-6
def working_hour_reached(name,wage_per_hour,your_total_working_hour):
    monthly_hour = 100

    if(your_total_working_hour <= monthly_hour) :
        your_total_working_hour_wage = wage_per_hour * your_total_working_hour
        print(f"{name} your total monthly working hour wage is: ${your_total_working_hour_wage}")
        return your_total_working_hour_wage
    else:
        return 0

        




print("Enter 1 for checking status")
print("Enter 2 for checking the wage")
print("Enter 3 for checking the dailyWage + partTimeWage")
print("Enter 4 for checking the monthlyWage")
print("Enter 5 for checking the total working hours wage")

Choice = int(input("Enter your choice :"))

match Choice:
    case 1:
        check_status("Nazim")
    
    case 2:
        daily_wage("Nazim",20,8)
    
    case 3:
        Add_partTime_wage("Nazim",160,20,8)

    case 4:
        calculate_monthly_wage("Nazim",20,8,4)

    case 5:
        working_hour_reached("Nazim",20,100)
    
    case _:
        print("Invalid choice!!!")
