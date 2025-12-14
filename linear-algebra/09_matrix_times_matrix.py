# Multiply two matrices together (return -1 if shapes of matrix don't align), i.e. C = A ⋅ B
# https://www.deep-ml.com/problems/9?from=Machine%20Learning

Scalar = int | float
Vector = list[Scalar]
Matrix = list[Vector]

def vector_vector_dot_product(vec1: Vector, vec2: Vector) -> Scalar:
    if len(vec1) != len(vec2):
        raise ValueError('Vector dimensions do not match. Cannot perform dot product.')
    result: Scalar = 0
    for item_1, item_2 in zip(vec1, vec2):
        result += item_1 * item_2
    return result

def vector_matrix_dot_product(vector: Vector, matrix: Matrix) -> Vector:
    if len(vector) != len(matrix):
        raise ValueError('Vector and matrix are incompatible for dot product.')
    result: Vector = []
    for col_id in range(len(matrix[0])):
        col_vector: Vector = [matrix[row_id][col_id]
                              for row_id in range(len(matrix))]
        result.append(vector_vector_dot_product(vector, col_vector))
    return result

def matrix_multiplication(mat1: Matrix, mat2: Matrix) -> Matrix:
    if len(mat1[0]) != len(mat2):
        raise ValueError('Matrices are incompatible for multiplication.')
    result: Matrix = [[] for _ in range(len(mat1))]
    for row_id in range(len(mat1)):
        result[row_id] = vector_matrix_dot_product(mat1[row_id], mat2)
    return result

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    mat1: Matrix
    mat2: Matrix
    result: Matrix

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data = in_file.readlines()
        mat1 = literal_eval(data[0])
        mat2 = literal_eval(data[1])

    result = matrix_multiplication(mat1, mat2)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(result))


if __name__ == '__main__':
    main()