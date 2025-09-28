# Ask user for their name
name = input("Enter your name: ")

# Ask user for their age
age = int(input("Enter your age: "))

# Calculate the year they will turn 100
current_year = 2025
year_turn_100 = current_year + (100 - age)

# Print the result
print(f"Hello {name}! You will turn 100 years old in the year {year_turn_100}.")
