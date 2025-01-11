# daily_reminder.py

# Get user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case statement for task priority
match priority:
    case "high":
        priority_message = f"'{task}' is a high priority task"
    case "medium":
        priority_message = f"'{task}' is a medium priority task"
    case "low":
        priority_message = f"'{task}' is a low priority task"
    case _:
        priority_message = "Invalid priority level!"

# Check if the task is time-bound
if time_bound == "yes":
    reminder_message = f"{priority_message} that requires immediate attention today!"
else:
    reminder_message = f"{priority_message}. Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder_message)

