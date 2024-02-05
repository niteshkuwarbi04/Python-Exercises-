'''
12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines 
    as output (all characters in lower case).
'''

lines = []
while True:
    l = input("Enter a line (blank line to terminate): ")
    if not l:
        break
    else:
        lines.append(l.upper())

for l in lines:
    print(l)
