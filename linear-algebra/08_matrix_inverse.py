# Write a Python function that calculates the inverse of a 2x2 matrix. 
# Return 'None' if the matrix is not invertible.
# https://www.deep-ml.com/problems/8?from=Machine%20Learning

Scalar = int | float
Matrix = list[list[Scalar]]

def calculate_determinant(matrix: Matrix) -> Scalar:
    a_d = matrix[0][0] * matrix[1][1]
    b_c = matrix[0][1] * matrix[1][0]
    return a_d - b_c

def calculate_adjoint(matrix: Matrix) -> Matrix:
    adjoint: Matrix = matrix.copy()
    adjoint[0][0] = matrix[1][1]
    adjoint[1][1] = matrix[0][0]
    adjoint[0][1] *= -1
    adjoint[1][0] *= -1
    return adjoint

def scalar_product(matrix: Matrix, scalar: Scalar) -> Matrix:
    scaled_matrix: Matrix = matrix.copy()
    for row_id in range(len(scaled_matrix)):
        for col_id in range(len(scaled_matrix[0])):
            scaled_matrix[row_id][col_id] *= scalar
    return scaled_matrix 

def calculate_inverse(matrix: Matrix) -> Matrix:
    determinant = calculate_determinant(matrix)
    if determinant == 0:
        raise ValueError('Inverse of a singular matrix does not exist')
    adjoint: Matrix = calculate_adjoint(matrix)
    inverse: Matrix = scalar_product(adjoint, 1 / determinant)
    return inverse

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    matrix: Matrix
    inverse: Matrix

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data = in_file.read()
        matrix = literal_eval(data)

    inverse = calculate_inverse(matrix)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(inverse))


if __name__ == '__main__':
    main()
