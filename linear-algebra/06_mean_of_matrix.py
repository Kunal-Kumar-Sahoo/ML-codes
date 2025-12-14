# Write a Python function that calculates the mean of a matrix either by row or by column, based on a 
# given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input 
# and return a list of means according to the specified mode.
# https://www.deep-ml.com/problems/4?from=Machine%20Learning


Scalar = int | float
Vector = list[Scalar]
Matrix = list[Vector]


def calculate_vector_mean(vector: Vector) -> Scalar:
    sum: Scalar = 0.0
    for item in vector:
        sum += item
    mean: Scalar = sum / len(vector)
    return mean


def calculate_matrix_mean(matrix: Matrix, mode: str = 'row') -> Vector:
    num_rows: int = len(matrix)
    num_cols: int = len(matrix[0])
    mean: Vector = []

    if mode == 'row':
        for row_id in range(num_rows):
            mean.append(calculate_vector_mean(matrix[row_id]))

    elif mode == 'col':
        for col_id in range(num_cols):
            col_entries: Vector = [matrix[row_id][col_id]
                            for row_id in range(num_rows)]
            mean.append(calculate_vector_mean(col_entries))

    else:
        raise ValueError('Invalide mode')
    
    return mean

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    matrix: Matrix
    mean: Vector
    mode: str

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data = in_file.readlines()
        matrix = literal_eval(data[0])
        mode = data[1]

    mean = calculate_matrix_mean(matrix, mode)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(mean))


if __name__ == '__main__':
    main()