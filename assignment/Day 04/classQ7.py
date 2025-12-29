# 3x4 matrix as list of lists
matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# 3x4 matrix as tuple of tuples
matrix_tuple = (
    (2, 0, 1, 3),
    (4, 5, 6, 7),
    (8, 9, 10, 11)
)

# Function to add and subtract matrices
def matrix_ops(mat1, mat2):
    add = []
    sub = []
    for i in range(3):
        add_row = []
        sub_row = []
        for j in range(4):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])
        add.append(add_row)
        sub.append(sub_row)
    return add, sub

# Main
add_result, sub_result = matrix_ops(matrix_list, matrix_tuple)

print("Addition:")
for row in add_result:
    print(row)

print("\nSubtraction:")
for row in sub_result:
    print(row)
