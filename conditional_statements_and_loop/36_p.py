'''
36. Write a Python program to check if a triangle is equilateral, isosceles or scalene.
    Note :
    An equilateral triangle is a triangle in which all three sides are equal.
    A scalene triangle is a triangle that has three unequal sides.
    An isosceles triangle is a triangle with (at least) two equal sides.'''

def triangle_type(a,b,c):
    if a==b==c:
        return "Equilateral Triangle"
    elif a==b or b==c or c==a:
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"

a = float(input('Enter the value of first side: '))
b = float(input('Enter the value of second side: '))
c = float(input('Enter the value of third side: '))

result = triangle_type(a,b,c)
print(f'The triangle is {result}.')