import random

print("Welcome to Employee Wage Computation Program on Master Branch")

# UC-1
def check_status(name):
    status = random.choice(['Present','Absent'])
    print(f"{name} is {status}")
    return status


check_status("Nazim")