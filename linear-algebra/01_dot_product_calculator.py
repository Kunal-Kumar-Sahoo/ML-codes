# Write a Python function to calculate the dot product of two vectors. 
# The function should take two 1D arrays as input and return the dot product as a single number.
# https://www.deep-ml.com/problems/83?from=Machine%20Learning


Scalar = int | float
Vector = list[Scalar]

def dot_product(vec1: Vector, vec2: Vector) -> Scalar:
    if len(vec1) != len(vec2):
        raise ValueError('Vector dimensions do not match. Cannot perform dot product.')
    answer: Scalar = 0
    for item_1, item_2 in zip(vec1, vec2):
        answer += item_1 * item_2
    return answer

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    vector1: Vector
    vector2: Vector
    answer: Scalar

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        vectors = in_file.readlines()
        vector1 = literal_eval(vectors[0])
        vector2 = literal_eval(vectors[1])

    answer = dot_product(vector1, vector2)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(answer))
        

if __name__ == '__main__':
    main()