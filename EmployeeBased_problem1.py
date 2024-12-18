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


# check_status("Nazim")
daily_wage("Nazim",20,8)