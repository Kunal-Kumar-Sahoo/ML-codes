# Write a Python function that multiplies a matrix by a scalar and returns the result.
# https://www.deep-ml.com/problems/5?from=Machine%20Learning


Scalar = int | float
Matrix = list[list[Scalar]]


def scalar_multiply(matrix: Matrix, scalar: Scalar) -> Matrix:
    num_rows: int = len(matrix)
    num_cols: int = len(matrix[0])
    scaled_matrix: Matrix = [[] for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            scaled_matrix[i].append(scalar * matrix[i][j])

    return scaled_matrix

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval
   
    scalar: Scalar
    matrix: Matrix
    scaled_matrix: Matrix

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data = in_file.readlines()
        matrix = literal_eval(data[0])
        scalar = literal_eval(data[1])

    scaled_matrix = scalar_multiply(matrix, scalar)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(scaled_matrix))

   
if __name__ == '__main__':
    main()
