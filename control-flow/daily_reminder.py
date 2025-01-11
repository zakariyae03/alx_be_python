# daily_reminder.py

# Prompt for task description
task = input("Enter your task: ")

# Prompt for task priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time sensitivity
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Validate priority input
valid_priorities = {"high", "medium", "low"}
if priority not in valid_priorities:
    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
    exit()

# Validate time-bound input
if time_bound not in {"yes", "no"}:
    print("Invalid input for time sensitivity. Please enter 'yes' or 'no'.")
    exit()

# Process and generate the reminder
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."

if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print the final reminder
print(f"\nReminder: {reminder}")
