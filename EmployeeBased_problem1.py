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
    else:
        print(f"You don't get your todays wage!!!")
    return amount

# UC-3
def Add_partTime_wage(name,amount,wage_per_hour,partTime_hour):
    # Calculating part time wage
    partTime_wage = wage_per_hour * partTime_hour

    # Checking if employee is present in part time 
    status = check_status(name)
    if(status == 'Present'):
        new_amount = amount + partTime_wage
        print(f"Your part time amount is also added : ${new_amount}")
    else:
        print(f"Your amount is :",amount)



print("Enter 1 for checking status")
print("Enter 2 for checking the wage")
print("Enter 3 for checking the dailyWage + partTimeWage")
Choice = int(input("Enter your choice :"))

match Choice:
    case 1:
        check_status("Nazim")
    
    case 2:
        daily_wage("Nazim",20,8)
    
    case 3:
        Add_partTime_wage("Nazim",160,20,8)
    
    case _:
        print("Invalid choice!!!")
