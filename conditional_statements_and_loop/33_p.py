'''
33. Write a Python program to convert a month name to a number of days.'''

print("List of months: January, February, March, April, May, June, July, August, September, October, November, December")

month_name = input('Enter the name of the month: ')

if month_name == 'february':
    print('No. of days: 28/29 days.')
elif month_name in ("April", "June", "September", "November"):
    print('No of days: 30 days.')
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print('No of days: 31 days.')
else:
    print('Wrong month name.')