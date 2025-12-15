# You need to implement a single function that can perform three variants of gradient descent 
# Stochastic Gradient Descent (SGD), Batch Gradient Descent, and Mini Batch Gradient Descent using 
# Mean Squared Error (MSE) as the loss function. The function will take an additional parameter to 
# specify which variant to use. Note: Do not shuffle the data
# https://www.deep-ml.com/problems/47?from=Machine%20Learning

import random
import numpy as np

def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return 0.5 * np.mean((y_true - y_pred) ** 2)

def grad_error(X: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    size: int = len(X)
    return (1 / size) * X.T @ (X @ theta - y)

def update_weights(X: np.ndarray, y: np.ndarray, theta: np.ndarray, alpha: float) -> np.ndarray:
    return theta - alpha * grad_error(X, y, theta)

def batch_gradient_descent(X: np.ndarray, y: np.ndarray, weights: np.ndarray, 
                           learning_rate: np.ndarray, n_iterations: int) -> np.ndarray:
    for _ in range(n_iterations):
        old_weights: np.ndarray = weights.copy()
        weights = update_weights(X, y, weights, learning_rate)
        if (old_weights == weights).all():
            break
    return weights

def stochastic_gradient_descent(X: np.ndarray, y: np.ndarray, weights: np.ndarray, 
                                learning_rate: np.ndarray, n_iterations: int) -> np.ndarray:
    for _ in range(n_iterations):
        sample_idx: int = int(random.uniform(0, len(X)))
        sample_data: np.ndarray = X[sample_idx].reshape((1, -1))
        sample_label: np.ndarray = y[sample_idx].reshape((1, -1))
        old_weights: np.ndarray = weights.copy()
        weights = update_weights(sample_data, sample_label, weights, learning_rate)
        if (old_weights == weights).all():
            break
    return weights

def minibatch_gradient_descent(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, 
                               n_iterations: int, batch_size: int = 1) -> np.ndarray:
    for iter in range(n_iterations):
        start_idx: int = iter * batch_size
        end_idx: int = start_idx + batch_size
        sample_data: np.ndarray = X[start_idx:end_idx].reshape((batch_size, -1))
        sample_labels: np.ndarray = y[start_idx:end_idx].reshape((batch_size, -1))
        old_weights: np.ndarray = weights.copy()
        weights = update_weights(sample_data, sample_labels, weights, learning_rate)
        if (old_weights == weights).all():
            break
    return weights

def gradient_descent(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iterations: int, 
                     batch_size: int = 1, method: str = 'batch') -> np.ndarray:
    
    if method == 'batch':
        return batch_gradient_descent(X, y, weights, learning_rate, n_iterations)

    elif method == 'stochastic':
        return stochastic_gradient_descent(X, y, weights, learning_rate, n_iterations)

    elif method == 'minibatch':
        return minibatch_gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size)

    else:
        raise ValueError('Invalid mode.')
