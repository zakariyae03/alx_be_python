# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Function to display the current date and time in the format: YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()  # Get the current date and time
    # Format the current date and time as a string
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Function to calculate and display the future date after adding a user-specified number of days.
    """
    # Get the number of days to add from the user
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    current_date = datetime.now()  # Get the current date and time
    future_date = current_date + timedelta(days=days_to_add)  # Add the number of days to the current date
    # Format the future date as a string
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

# Main function to execute both tasks
def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
