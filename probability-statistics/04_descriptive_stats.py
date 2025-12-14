# Write a Python function to calculate various descriptive statistics metrics for a given dataset. 
# The function should take a list or NumPy array of numerical values and return a dictionary containing 
# mean, median, mode, variance, standard deviation, percentiles (25th, 50th, 75th), and interquartile range (IQR).
# https://www.deep-ml.com/problems/78?from=Machine%20Learning

import math

def calculate_mean(data: list[int|float]) -> float:
    sum: int|float = 0
    size: int = len(data)
    for item in data:
        sum += item
    return sum / size

def calculate_mode(data: list[int|float]) -> set[int|float]:
    frequency = dict()
    for item in data:
        if item in frequency.keys():
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    mode_items = {}
    mode_freq = 0

    print('DEBUG:', frequency)

    for item, freq in frequency.items():
        if mode_freq < freq:
            mode_items = {item}
            mode_freq = freq
        elif mode_freq == freq:
            mode_items.add(item)

    return mode_items

def calculate_median(data: list[int|float]) -> int|float:
    sorted_data: list[int|float] = sorted(data)
    length: int = len(sorted_data)
    if length % 2:
        return sorted_data[length // 2]
    return (sorted_data[length // 2] + sorted_data[length // 2 + 1]) / 2

def calculate_variance(data: list[int|float], mode: str = 'population') -> float:
    mean: float = calculate_mean(data)
    squared_sum: float = 0.0
    length: int = len(data)
    for item in data:
        squared_sum += (item - mean) ** 2
    
    if mode == 'population':
        return squared_sum / length
    elif mode == 'sample':
        return squared_sum / (length - 1)
    else:
        raise ValueError('Invalid mode.')
    
def kth_percentile(data: list[int|float], k: float) -> float:
    if k < 0 or k > 100: 
        raise ValueError('Invalid percentile query.')
    sorted_data: list[int|float] = sorted(data)
    length: int = len(sorted_data)

    if length == 1:
        return sorted_data[0]
    
    position: float = (k / 100) * (length - 1)
    lower_index: int = int(position)
    upper_index: int = lower_index + 1

    fraction: float = position - lower_index
    lower_value: int|float = sorted_data[lower_index]
    upper_value: int|float = sorted_data[upper_index]

    return lower_value + fraction * (upper_value - lower_value)

def descriptive_statistics(data: list[int|float]) -> dict[str, int|float]:
    mean = calculate_mean(data)
    mode = calculate_mode(data)
    median = calculate_median(data)
    variance = calculate_variance(data)
    std_dev = math.sqrt(variance)
    percentiles = [kth_percentile(data, k) for k in (25, 50, 75)]
    iqr = percentiles[-1] - percentiles[0]

    stats_dict = {
        'mean': mean,
        'median': median,
        'mode': mode,
        'variance': round(variance, 4),
        'standard_deviation': round(std_dev, 4),
        '25th_percentile': percentiles[0],
        '50th_percentile': percentiles[1],
        '75th_percentile': percentiles[2],
        'interquartile_range': iqr,
    }

    return stats_dict

def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data: list[int|float] = literal_eval(in_file.read())
    
    statistics: dict[str, int|float] = descriptive_statistics(data)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.write(str(statistics))


if __name__ == '__main__':
    main()
