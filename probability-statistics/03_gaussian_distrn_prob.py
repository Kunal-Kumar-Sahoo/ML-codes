# Write a Python function to calculate the probability density function (PDF) of the normal distribution 
# for a given value, mean, and standard deviation. The function should use the mathematical formula of 
# the normal distribution to return the PDF value rounded to 5 decimal places.
# https://www.deep-ml.com/problems/80?from=Machine%20Learning

import math

def gaussian_distribution(x: float, mean: float, std_dev: float) -> float:
    prob = 1 / math.sqrt(2 * math.pi * std_dev ** 2) * math.exp(-0.5 * ((x - mean) / std_dev) ** 2)
    return round(prob, 5)

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data: str = in_file.readlines()
        x: int = literal_eval(data[0])
        mean: int = literal_eval(data[1])
        std_dev: float = literal_eval(data[2])
    
    prob: float = gaussian_distribution(x, mean, std_dev)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(prob))


if __name__ == '__main__':
    main()