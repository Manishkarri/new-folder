def calculate_speed(distance, time):
    """
    Calculate the speed of a car.

    Parameters:
    distance (float): The distance traveled by the car (in kilometers or miles).
    time (float): The time taken to travel the distance (in hours).

    Returns:
    float: The speed of the car (in kilometers per hour or miles per hour).
    """
    if time <= 0:
        raise ValueError("Time must be greater than zero to calculate speed.")

    speed = distance / time
    return speed


# Example usage:
try:
    distance = float(input("Enter the distance traveled by the car (in kilometers or miles): "))
    time = float(input("Enter the time taken to travel the distance (in hours): "))
    speed = calculate_speed(distance, time)
    print(f"The speed of the car is {speed:.2f} km/h or mph")
except ValueError as e:
    print(f"Error: {e}")
