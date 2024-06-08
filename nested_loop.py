# 3x3 matrix - get each component by indexing of each individual component
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    # print(matrix[1][1])

for rows in matrix:
    for item in rows:
        if item == rows[1]:
            print(item, end=" ")
        # code below helps print as matrix structure in terminal
    print()

