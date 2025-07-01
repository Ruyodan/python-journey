# from function_bmi import results  # Import the results function from the bmi module

# participation = int(input("Enter the number of participants: "))  # Get the number of participants
# for i in range(participation):
#     weight = float(input("Enter your weight in kg: "))
#     height = float(input("Enter your height in meters: "))  # Get the height in meters
#     results(weight, height)
    

from functions import * # Import all functions from the import_mudule_python module

questions = input("Do you want to check your flight? (yes or quit): ").strip().lower()  # Ask the user if they want to check their flight type
while questions != 'quit':  # Continue asking until the user types 'quit'
    if questions == 'yes':  # If the user wants to check their flight
        flight_check()  # Call the flight check function
    else:  # If the user does not want to check their flight
        print("Thank you for using the flight check program. Goodbye!")
    questions = input("Do you want to check your flight? (yes or quit): ").strip().lower()