# Write a Python function to calculate the covariance matrix for a given set of vectors. The function 
# should take a list of lists, where each inner list represents a feature with its observations, and 
# return a covariance matrix as a list of lists. Additionally, provide test cases to verify the 
# correctness of your implementation.

Scalar = int | float
Vector = list[Scalar]
Matrix = list[Vector]

def compute_mean(vector: Vector) -> Scalar:
    sum: Scalar = 0
    for item in vector:
        sum += item
    return sum / len(vector)

def compute_covariance(vec1: Vector, vec2: Vector) -> Scalar:
    if len(vec1) != len(vec2):
        raise ValueError('Incompatible vectors')
    
    length: int = len(vec1)
    mean1 = compute_mean(vec1)
    mean2 = compute_mean(vec2)
    vec1_centered = [item - mean1 for item in vec1]
    vec2_centered = [item - mean2 for item in vec2]

    sum: float = 0.0
    for item1, item2 in zip(vec1_centered, vec2_centered):
        sum += item1 * item2
    
    return sum / (length - 1)


def covariance_matrix(vectors: Matrix) -> Matrix:
    num_vectors: int = len(vectors)
    cov_matrix: Matrix = [[] for _ in range(num_vectors)]

    for i in range(num_vectors):
        for j in range(num_vectors):
            cov: Scalar = compute_covariance(vectors[i], vectors[j])
            cov_matrix[i].append(cov)

    return cov_matrix

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        vectors: Matrix = literal_eval(in_file.read())

    cov: Matrix = covariance_matrix(vectors)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(cov))


if __name__ == '__main__':
    main()
    