import random
import numpy as np

def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return 0.5 * np.mean((y_true - y_pred) ** 2)

def grad_error(X: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    size = len(X)
    return (1 / size) * X.T @ (X @ theta - y)

def update_weights(X: np.ndarray, y: np.ndarray, theta: np.ndarray, alpha: float) -> np.ndarray:
    return theta - alpha * grad_error(X, y, theta)

def batch_gradient_descent(X, y, weights, learning_rate, n_iterations):
    for _ in range(n_iterations):
        old_weights = weights.copy()
        weights = update_weights(X, y, weights, learning_rate)
        if np.linalg.norm(old_weights - weights) < 1e-8:
            break
    return weights

def stochastic_gradient_descent(X, y, weights, learning_rate, n_iterations):
    n = len(X)
    for _ in range(n_iterations):
        idx = random.randrange(n)
        sample_X = X[idx:idx+1]
        sample_y = y[idx:idx+1]
        old_weights = weights.copy()
        weights = update_weights(sample_X, sample_y, weights, learning_rate)
        if np.linalg.norm(old_weights - weights) < 1e-8:
            break
    return weights

def minibatch_gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size):
    n = len(X)
    for i in range(n_iterations):
        start = (i * batch_size) % n
        end = min(start + batch_size, n)
        batch_X = X[start:end]
        batch_y = y[start:end]
        old_weights = weights.copy()
        weights = update_weights(batch_X, batch_y, weights, learning_rate)
        if np.linalg.norm(old_weights - weights) < 1e-8:
            break
    return weights

def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method='batch'):
    if method == 'batch':
        return batch_gradient_descent(X, y, weights, learning_rate, n_iterations)
    elif method == 'stochastic':
        return stochastic_gradient_descent(X, y, weights, learning_rate, n_iterations)
    elif method == 'mini_batch':
        return minibatch_gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size)
    else:
        raise ValueError('Invalid method')

def main(input_file='input.txt', output_file='output.txt'):
    from ast import literal_eval

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        X = np.array(literal_eval(lines[0]))
        y = np.array(literal_eval(lines[1]))
        lr = literal_eval(lines[2])
        n_iters = literal_eval(lines[3])
        batch_size = literal_eval(lines[4])
        method = lines[5].strip()

    weights = np.zeros(X.shape[1])
    weights = gradient_descent(X, y, weights, lr, n_iters, batch_size, method)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(str(weights))

if __name__ == '__main__':
    main()
