'''
37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.'''

def get_season(month, day):
    if (month == 3 and day >= 20) or (month > 3 and month < 6) or (month == 6 and day < 21):
        return "Spring"
    elif (month == 6 and day >= 21) or (month > 6 and month < 9) or (month == 9 and day < 23):
        return "Summer"
    elif (month == 9 and day >= 23) or (month > 9 and month < 12) or (month == 12 and day < 21):
        return "Autumn"
    else:
        return "Winter"

# Get input from the user
month = int(input("Enter the month (as a number, e.g., 1 for January): "))
day = int(input("Enter the day: "))

# Check and print the season
season = get_season(month, day)
print(f"The season for {month}/{day} is {season}.")
