UNDERWEIGHT_MAX = 18.5
NORMAL_MAX = 24.9

def bmi_calculator(weight, height):
    """
    Calculate the Body Mass Index (BMI) given weight and height.

    Parameters:
    weight (float): The weight of the participant in kilograms.
    height (float): The height of the participant in meters.

    Returns:
    float: The calculated BMI.
    """
    return weight / (height ** 2)

def results(weight, height):
    """
    Determines and prints the BMI category for a given weight and height.

    Parameters:
    weight (float): The weight of the participant in kilograms.
    height (float): The height of the participant in meters.
    """
    bmi = bmi_calculator(weight, height)  # Call the BMI calculator function
    if bmi <= UNDERWEIGHT_MAX:
        print("You are underweight")
    elif bmi > UNDERWEIGHT_MAX and bmi <= NORMAL_MAX:
        print("You are normal weight")
    else:
        print("You are overweight")