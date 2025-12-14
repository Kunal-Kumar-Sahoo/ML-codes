# Write a Python function that computes the dot product of a matrix and a vector. 
# The function should return a list representing the resulting vector if the operation is valid, 
# or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be 
# dotted with a vector (a list) only if the number of columns in the matrix equals the length of 
# the vector. For example, an n x m matrix requires a vector of length m.
# https://www.deep-ml.com/problems/1?from=Machine%20Learning


Scalar = int | float
Vector = list[Scalar]
Matrix = list[Vector]


def dot_product(vec1: Vector, vec2: Vector) -> Scalar:
    if len(vec1) != len(vec2):
        raise ValueError('Vector dimensions do not match. Cannot perform dot product.')
    answer: Scalar = 0
    for item_1, item_2 in zip(vec1, vec2):
        answer += item_1 * item_2
    return answer

def matrix_vector_dot_product(matrix: Matrix, vector: Vector) -> Vector | int:
    if len(vector) != len(matrix[0]):
        return -1
    answer: Vector = []
    temp_result: Scalar
    for row in matrix:
        temp_result = dot_product(row, vector)
        answer.append(temp_result)
    return answer

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    matrix: Matrix
    vector: Vector
    result: Vector | int

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data = in_file.readlines()
        matrix = literal_eval(data[0])
        vector = literal_eval(data[1])
 
    result = matrix_vector_dot_product(matrix, vector)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(result))


if __name__ == '__main__':
    main()
