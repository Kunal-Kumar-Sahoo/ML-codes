# Write a Python function to calculate the probability of achieving exactly k successes in n independent
# Bernoulli trials, each with probability p of success, using the Binomial distribution formula.
# https://www.deep-ml.com/problems/79?from=Machine%20Learning

import math

def bernoulli_distribution(n: int, k: int, p: float) -> float:
    prob = math.comb(n, k) * p ** k * (1-p) ** (n-k)
    return round(prob, 5)

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data: str = in_file.readlines()
        n: int = literal_eval(data[0])
        k: int = literal_eval(data[1])
        p: float = literal_eval(data[2])
    
    prob: float = bernoulli_distribution(n, k, p)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(prob))


if __name__ == '__main__':
    main()