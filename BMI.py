def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI).

    Parameters:
    weight (float): The weight of the person (in kilograms or pounds).
    height (float): The height of the person (in meters or inches).

    Returns:
    float: The BMI of the person.
    """
    bmi = weight / (height ** 2)
    return bmi


# Example usage:
try:
    weight = float(input("Enter your weight (in kg or lbs): "))
    height = float(input("Enter your height (in meters or inches): "))

    # Convert height from inches to meters if necessary
    if height > 3:  # Assuming no one is taller than 3 meters!
        height /= 39.37  # Convert inches to meters

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi:.2f}")
except ValueError:
    print("Please enter valid numeric values for weight and height.")
