# Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return 
# a list containing the eigenvalues, sort values from highest to lowest.
# https://www.deep-ml.com/problems/6?from=Machine%20Learning


Scalar = int | float
Vector = list[Scalar]
Matrix = list[Vector]

def calculate_trace(matrix: Matrix) -> Scalar:
    sum: Scalar = 0.0
    for i in range(len(matrix)):
        sum += matrix[i][i]
    return sum

def calculate_determinant(matrix: Matrix) -> Scalar:
    a_d = matrix[0][0] * matrix[1][1]
    b_c = matrix[0][1] * matrix[1][0]
    return a_d - b_c

def solve_quadratic(a: Scalar, b: Scalar, c: Scalar) -> Vector:
    from math import sqrt

    sol1: Scalar = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    sol2: Scalar = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return [sol1, sol2]

def calculate_eigenvectors(matrix: Matrix) -> Vector:
    # \lambda^2 - trace(A) \lambda + determinant(A) = 0
    trace: Scalar = calculate_trace(matrix)
    determinant: Scalar = calculate_determinant(matrix)
    return solve_quadratic(1, -trace, determinant)

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    matrix: Matrix
    eigenvalues: Vector

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data = in_file.read()
        matrix = literal_eval(data)

    eigenvalues = calculate_eigenvectors(matrix)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(eigenvalues))


if __name__ == '__main__':
    main()  