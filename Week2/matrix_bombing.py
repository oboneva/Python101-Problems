def matrix_bombing_plan(matrix):
    sum_of_all = 0
    rows = len(matrix)
    cows = len(matrix[0])

    for i in range(rows):
        for j in range(cows):
            sum_of_all += matrix[i][j]

    result = {}

    for i in range(rows):
        for j in range(cows):
            bombed_sum = 0

            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if x >= 0 and y >= 0 and x < rows and y < cows:
                        bombed_sum += min(matrix[i][j], matrix[x][y])

            result.update({(i, j): sum_of_all - bombed_sum + matrix[i][j]})

    return result
