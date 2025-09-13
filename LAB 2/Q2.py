matrix1 = [[1,2,3],
           [4,5,6],
           [7,8,9]
           ]
matrix2 = [[2,4,6],
           [4,5,6],
           [7,8,9]
           ]
addMatrix =[[0,0,0],
            [0,0,0],
            [0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        addMatrix[i][j] = matrix1[i][j] +  matrix2[i][j]

row1, cols1 = len(matrix1), len(matrix1[0])
row2, cols2 = len(matrix2), len(matrix2[0])

mulMatrix =[[0,0,0],
            [0,0,0],
            [0,0,0]]

for i in range(row1):
    for j in range(cols2):
        for k in range(cols1):  
            mulMatrix[i][j] += matrix1[i][k] * matrix2[k][j]


print("\nMatrix 1:")
for row in matrix1:
    print(row)
print("\nMatrix 2:")
for row in matrix2:
    print(row)
print("\nAddition result:")
for row in addMatrix:
    print(row)

print("\nMultiplication result:")
for row in mulMatrix:
    print(row)

