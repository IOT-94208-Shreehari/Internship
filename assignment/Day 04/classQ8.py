# Input tuple of tuples
data = ((10, 10, 10, 12), 
        (30, 45, 56, 45), 
        (81, 80, 39, 32), 
        (1, 2, 3, 4))

# Number of rows and columns
rows = len(data)
cols = len(data[0])

# List to store averages
averages = []

# Loop through each column
for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += data[i][j]
    averages.append(col_sum / rows)

# Print result
print(averages)
