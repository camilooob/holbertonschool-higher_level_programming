
def matrix_divided(matrix, div):
    matrix1 = []
    matrix2 = []
    matrix10 = [matrix1, matrix2]
    z = 1
    for i in matrix:
        for j in i:
            if z <= 3:
                matrix1.append(float("{0:.2f}".format((j / div))))
            else:
                matrix2.append(float("{0:.2f}".format((j / div))))
            z += 1
    return matrix10

def main():
    matrix = [[1, 2, 3],[4, 5, 6]]
    print(matrix_divided(matrix, 3))
    print(matrix)

main()
