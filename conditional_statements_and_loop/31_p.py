'''
31. Write a Python program to calculate a dog's age in dog years.
    Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.'''

def calculate_dog_years(human_years):
    if human_years <= 2:
        dog_years = human_years * 10.5
    else:
        dog_years = 2*10.5 + (human_years-2) * 4

    return dog_years

human_years = float(input("Input a dog's age in human years: "))

dog_years = calculate_dog_years(human_years)

print(f"The dog's age in dog's years is {dog_years}")