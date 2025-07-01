# # # # # creating a function that accepts score as a parameter :
# # # # def evaluate_score(score): 
# # # #     print("Your score is:", score)  # Print the score provided by the user
# # # #     if score > 0 and score <= 50:
# # # #         print("Below passing, Improve your grade!")
# # # #     elif score > 50 and score <= 70:
# # # #         print("Barely passing the class!")
# # # #     elif score > 70 and score <= 90:
# # # #         print("You have a passing grade!")
# # # #     else:
# # # #         print("You are one of the best in class!")
    
# # # # user_score = int(input("Enter your score: "))  # Get the score from the user
# # # # evaluate_score(user_score)  # Call the function to evaluate the score




# # # # creating a funcion to add on extra flight charges : 
# # # def charges(flight_cost):
    
# # #     upgrade = input("Do you want to upgrade your flight? (yes/no): ").lower()  # Ask if the user wants an upgrade
# # #     if upgrade == "yes":
# # #         flight_cost += 99  # Add $99 if the user wants an upgrade
        
# # #     baggage = input("Do you have baggage? (yes/no): ").lower()  # Ask if the user has baggage      
# # #     if baggage == "yes":
# # #         flight_cost += 35  # Add $35 if the user has baggage
        
# # #     tax = (flight_cost * 0.08) + flight_cost  # Calculate 8% tax on the flight cost
# # #     return tax # Return the total cost including tax

# # # price = int(input("Enter the flight cost: "))  # Get the flight cost from the user
# # # grand_total = charges(price)  # Call the function to calculate total cost
# # # print("The total cost of your flight is: $", grand_total)  # Print the total cost including tax




# # # Creating functions to determine which terminal to go to

def terminal_1():
    print("You are in terminal 1, budget:")
    
def terminal_2():
    print("You are in terminal 2, domestic:")
    
def terminal_3():
    print("You are in terminal 3, international:")
    
def flight_check():
    flight = input("what type of flight do you have ?: ").lower()
    if flight == "budget":
        terminal_1()
    elif flight == "domestic":
        terminal_2()    
    elif flight == "international":
        terminal_3()
    else:
        print("Invalid flight type. Please enter 'budget', 'domestic', or 'international'.") 
        
flight_check()  # Call the function to start the flight check process      
    
    
# # BMI Calculator Program
# # BMI category boundaries as constants for clarity
# UNDERWEIGHT_MAX = 18.5
# NORMAL_MAX = 24.9

# def bmi_calculator(weight, height):
#     """
#     Calculate the Body Mass Index (BMI) given weight and height.

#     Parameters:
#     weight (float): The weight of the participant in kilograms.
#     height (float): The height of the participant in meters.

#     Returns:
#     float: The calculated BMI.
#     """
#     return weight / (height ** 2)

# def results(weight, height):
#     """
#     Determines and prints the BMI category for a given weight and height.

#     Parameters:
#     weight (float): The weight of the participant in kilograms.
#     height (float): The height of the participant in meters.
#     """
#     bmi = bmi_calculator(weight, height)  # Call the BMI calculator function
#     if bmi <= UNDERWEIGHT_MAX:
#         print("You are underweight")
#     elif bmi > UNDERWEIGHT_MAX and bmi <= NORMAL_MAX:
#         print("You are normal weight")
#     else:
#         print("You are overweight")
        
# participation = int(input("Enter the number of participants: "))  # Get the number of participants
# for i in range(participation):
#     weight = float(input("Enter your weight in kg: "))
#     height = float(input("Enter your height in meters: "))  # Get the height in meters
#     results(weight, height)
    