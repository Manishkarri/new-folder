import pandas as pd
import matplotlib.pyplot as plt


def track_weight():
    # Initialize an empty list to store weight data
    weight_entries = []

    # Loop to input weight data
    while True:
        date = input("Enter date (YYYY-MM-DD) or 'done' to finish: ")
        if date.lower() == 'done':
            break
        weight = float(input("Enter weight (in kg): "))
        weight_entries.append({'Date': date, 'Weight': weight})

    # Convert the list of dictionaries to a DataFrame
    weight_data = pd.DataFrame(weight_entries)

    # Convert the 'Date' column to datetime format
    weight_data['Date'] = pd.to_datetime(weight_data['Date'])

    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(weight_data['Date'], weight_data['Weight'], marker='o', linestyle='-')
    plt.title('Weight Tracking')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    track_weight()


