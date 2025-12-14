# In this task, you need to implement a function cosine_similarity(v1, v2) that calculates the 
# cosine similarity between two vectors. Cosine similarity measures the cosine of the angle 
# between two vectors, indicating their directional similarity.
# https://www.deep-ml.com/problems/76?from=Machine%20Learning


Scalar = int | float
Vector = list[Scalar]


def dot_product(vec1: Vector, vec2: Vector) -> Scalar:
    if len(vec1) != len(vec2):
        raise ValueError('Vector dimensions do not match. Cannot perform dot product.')
    result: Scalar = 0
    for item_1, item_2 in zip(vec1, vec2):
        result += item_1 * item_2
    return result

def norm(vector: Vector) -> Scalar:
    from math import sqrt

    magnitude_squared: Scalar = dot_product(vector, vector)
    return sqrt(magnitude_squared)

def cosine_similarity(vec1: Vector, vec2: Vector) -> Scalar:
    return dot_product(vec1, vec2) / (norm(vec1) * norm(vec2))

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    vector1: Vector
    vector2: Vector
    similarity: Scalar

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data = in_file.readlines()
        vector1 = literal_eval(data[0])
        vector2 = literal_eval(data[1])
    
    similarity = cosine_similarity(vector1, vector2)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(similarity))


if __name__ == '__main__':
    main()