# Write a Python function to calculate the probability of observing exactly k events in a fixed interval 
# using the Poisson distribution formula. The function should take k (number of events) and lam (mean rate of occurrences) 
# as inputs and return the probability rounded to 5 decimal places.
# https://www.deep-ml.com/problems/81?from=Machine%20Learning

import math

def poisson_distribution(k: int, lam: float) -> float:
    p_k: int|float = (lam ** k * math.exp(-lam)) / math.factorial(k)
    return round(p_k, 5)


def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data: str = in_file.readlines()
        k: int = literal_eval(data[0])
        lam: float = literal_eval(data[1])
    
    prob: float = poisson_distribution(k, lam)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(prob))


if __name__ == '__main__':
    main()