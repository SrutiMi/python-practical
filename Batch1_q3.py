''' Write a Python program to perform matrix addition, matrix subtraction, and matrix multiplication by 
simulating matrix as a list of lists. You may use separate functions for each operation. 
'''

def matrix_addition(A,B):
  if len(A) != len(B) or len(A[0])!= len(B[0]):
    print("The matrices have the same dimensions for addition")
    return None
  
  result = []
  for i in range(len(A)):
    row=[]
    for j in range(len(A[0])):
      row.append(A[i][j]+B[i][j])
    result.append(row)

  return result

def matrix_subtraction(A,B):
  if len(A)!=len(B) or len(A[0])!=len(B[0]):
    print("The matrices have the same dimensions for subtraction")
    return None
  
  result=[]
  for i in range(len(A)):
    row=[]
    for j in range(len(A[0])):
      row.append(A[i][j]-B[i][j])
    result.append(row)
  return result

def matrix_multiplication(A,B):
  if len(A[0])!= len(B):
    print("No of columns in matrix A must be equal to the no of rows in matrix B")
    return None
  
  result=[]
  for i in range(len(A)):
    row=[]
    for j in range(len(B[0])):
      sum = 0
      for k in range(len(B)):
        sum+=A[i][k] * B[k][j]
      row.append(sum)
    result.append(row)
  return result

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print("Matrix Addition:")
result_add = matrix_addition(matrix1, matrix2)
if result_add :
  for row in result_add :
    print(row)

print("Matrix Subtraction:")
result_sub = matrix_subtraction(matrix1, matrix2)
if result_sub:
  for row in result_sub:
    print(row)

print("Matrix Multiplication:")
result_mul = matrix_multiplication(matrix1, matrix2)
if result_mul:
  for row in result_mul:
    print(row)