# Write a Python function that computes the transpose of a given matrix.
# https://www.deep-ml.com/problems/2?from=Machine%20Learning


Matrix = list[list[int | float]]


def transpose(matrix: Matrix) -> Matrix:
    num_rows: int = len(matrix)
    num_cols: int = len(matrix[0])
    transposed: Matrix = [[] for _ in range(num_cols)]

    for j in range(num_cols):
        for i in range(num_rows):
            transposed[j].append(matrix[i][j])

    return transposed

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    matrix: Matrix
    transposed: Matrix

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data = in_file.read()
        matrix = literal_eval(data)

    transposed = transpose(matrix)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(transposed))
    


if __name__ == '__main__':
    main()