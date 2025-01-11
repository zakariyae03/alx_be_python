# pattern_drawing.py

# Prompt the user for the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a positive integer.")
    exit()

# Draw the pattern using a while loop and nested for loop
row = 0
while row < size:
    # Use a for loop to draw the stars in each row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after completing the row
    row += 1
