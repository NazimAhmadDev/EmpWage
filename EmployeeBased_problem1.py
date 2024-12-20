import random

class EmployeeWageComputation:

    def __init__(self,name,wage_per_hour,full_day_hour,partTime_hour):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.full_day_hour = full_day_hour
        self.partTime_hour = partTime_hour
        self.monthly_hour = 100

    # UC-1
    def check_status(self):
        status = random.choice(['Present','Absent'])
        print(f"{self.name} is {status}")
        return status


    # UC-2
    def daily_wage(self):
        # Checking status of employee is present or absent
        status = self.check_status()

        if(status == 'Present'):
            amount = self.wage_per_hour * self.full_day_hour
            print(f"Your wage is ${amount}")
            return amount
        else:
            print(f"You don't get your todays wage!!!")
            return 0

    # UC-3
    def Add_partTime_wage(self,amount):
        # Calculating part time wage
        partTime_wage = self.wage_per_hour * self.partTime_hour

        # Checking if employee is present in part time 
        status = self.check_status()
        if(status == 'Present'):
            new_amount = amount + partTime_wage
            print(f"Your part time amount is also added : ${new_amount}")
            return new_amount
        else:
            print(f"Your amount is :",amount)
            return 0



    # Uc-5
    def calculate_monthly_wage(self):
        monthly_wage = 0
        working_days = 20
        part_time_days = 10

        for day in range(1, working_days + 1):
            print(f"\nDay {day}:")
            daily_amount = self.daily_wage()
            if day <= part_time_days:
                daily_amount = self.Add_partTime_wage(daily_amount)
            monthly_wage += daily_amount
        print(f"\n{self.name}'s total monthly wage is: ${monthly_wage}")
        return monthly_wage


    # UC-6
    def working_hour_reached(self,your_total_working_hour):
        monthly_hour = 100
        if(your_total_working_hour <= self.monthly_hour) :
            your_total_working_hour_wage = self.wage_per_hour * your_total_working_hour
            print(f"{self.name} your total monthly working hour wage is: ${your_total_working_hour_wage}")
            return your_total_working_hour_wage
        else:
            return 0

        


# Main

print("Welcome to Employee Wage Computation Program on Master Branch")

name = input("Enter your name :")
wage_per_hour = int(input("Enter wage per hour :"))
full_day_hour = int(input("Enter full day hours :"))
partTime_hour = int(input("Enter your part time hours :"))

employee = EmployeeWageComputation(name,wage_per_hour,full_day_hour,partTime_hour)

first_execution = True

while True:
        if not first_execution:
            print("************************ Choose Repeat for checking it again ************************")
            print("************************ Press enter to exit ************************")

            Choose = input("Enter your choice : ")

            if(Choose != 'Repeat'):
                break

        first_execution = False

        print("Enter 1 for checking status")
        print("Enter 2 for checking the wage")
        print("Enter 3 for checking the dailyWage + partTimeWage")
        print("Enter 4 for checking the monthlyWage")
        print("Enter 5 for checking the total working hours wage")

        Choice = int(input("Enter your choice :"))


        match Choice:
            case 1:
                employee.check_status()

            case 2:
                employee.daily_wage()

            case 3:
                amount = employee.daily_wage()
                employee.Add_partTime_wage(amount)

            case 4:
                employee.calculate_monthly_wage()

            case 5:
                your_total_working_hour = int(input("Enter your total working hour in a month :"))
                employee.working_hour_reached(your_total_working_hour)

            case _:
                print("Invalid choice!!!")
        
