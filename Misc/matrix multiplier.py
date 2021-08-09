def multiplymatrices(transformation, matrix):
    if len(transformation[0]) != len(matrix):
        return None

    if len(matrix) == 1:
        multiply = matrix.copy()
    else:
        multiply = list(zip(*matrix))

    output = [[0 for i in range(len(matrix[0]))] for i in range(len(transformation))]

    for rowi, row in enumerate(transformation):
        for columni, column in enumerate(multiply):
            if all([str(x).isdigit() for x in row]) and all([str(y).isdigit() for y in column]):
                values = [(int(row[i]) * int(column[i])) for i in range(len(row))]
                output[rowi][columni] = sum(values)
            else:
                output[rowi][columni] = "-"

    return output


transformationA = [[2, 0, 0],
                   [0, 2, 0],
                   [0, 0, 2]]

matrixA = [[1, 2, 3, 4],
           [4, 5, 6, 7],
           [7, 8, 9, 10]]
