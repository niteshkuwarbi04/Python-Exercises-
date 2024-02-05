'''
11. Write a Python program that takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
      Note :
      i = 0,1.., m-1
      j = 0,1, n-1.

      Test Data : Rows = 3, Columns = 4
      Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
'''

def generate_2d_array(rows, columns):
   array_2d = [[i*j for j in range(columns)] for i in range (rows)]
   return array_2d 

rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))

result_array = generate_2d_array(rows, columns)

print('Generated 2D Array: ')
for row in result_array:
   print(row) 