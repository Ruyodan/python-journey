# Program functions to check the salary of part-time or full-time employees
def hourly(time):
    rate = 25  # Set the hourly rate
    salary = time * rate  # Calculate the salary based on hours worked 
    return salary  # Return the calculated salary

def full_time(experience):
    annual_salary = 25000  # Set the annual salary for full-time employees
    if experience >= 2 and experience < 4:  # Check if the experience is between 2 and 4 years
        extra_salary = 1.5 # Set extra salary for this experience range
        bonus = 500 # Set a bonus for this experience range
    elif experience >= 4 and experience < 10:  # Check if the experience is between 4 and 10 years 
        extra_salary = 2.0  # Set extra salary for this experience range
        bonus = 1000  # Set a bonus for this experience range  
    elif experience >= 10:  # Check if the experience is 10 years or more
        extra_salary = 3.0  # Set extra salary for this experience range
        bonus = 1500  # Set a bonus for this experience range
    else:
        extra_salary = 1.0
        bonus = 200  # Set default values if experience is less than 2 years  
    annual_salary = annual_salary * extra_salary + bonus  # Calculate the annual salary with extra salary and bonus        
    return annual_salary  # Return the calculated annual salary

account = int(input("1 - run or 2 - quit:"))  # Ask the user to choose an option
while account != 2:
    employee = input("Enter your name: ")  # Get the employee's name
    employee_type = input("Enter your employee type (part-time or full-time): ").strip().lower()  # Get the employee type
    if employee_type == 'part-time':  # If the employee is part-time
        time = int(input("Enter the number of hours worked: "))  # Get the number of hours worked
        pay = hourly(time)  # Calculate the pay for hourly employees
    elif employee_type == 'full-time':  # If the employee is full-time
        experience = int(input("Enter your years of experience: "))  # Get the years of experience
        pay = full_time(experience)  # Calculate the pay for full-time employees
    else:
        print("Invalid employee type. Please enter 'part-time' or 'full-time'.")
        pay = None
    if pay is not None:
        print(employee, "your salary is:", pay)  # Print the employee's name and calculated salary
    
    