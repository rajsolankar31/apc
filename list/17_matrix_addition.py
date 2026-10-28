# Program 17: Matrix Addition
# Create two 3x3 matrices using nested lists and perform addition

print("Enter elements for Matrix 1 (3x3):")
matrix1 = []
for i in range(3):
    row = []
    for j in range(3):
        val = int(input(f"Enter element [{i}][{j}]: "))
        row.append(val)
    matrix1.append(row)
print("\nEnter elements for Matrix 2 (3x3):")
matrix2 = []
for i in range(3):
    row = []
    for j in range(3):
        val = int(input(f"Enter element [{i}][{j}]: "))
        row.append(val)
    matrix2.append(row)
result = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)
print("\nMatrix 1:")
for row in matrix1:
    print(row)
print("\nMatrix 2:")
for row in matrix2:
    print(row)
print("\nResultant Matrix (Addition):")
for row in result:
    print(row)
