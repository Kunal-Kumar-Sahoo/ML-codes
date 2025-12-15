# Write a Python function that performs linear regression using gradient descent. The function should take 
# NumPy arrays X (features with a column of ones for the intercept) and y (target) as input, along with 
# learning rate alpha and the number of iterations, and return the coefficients of the linear regression model 
# as a NumPy array. Round your answer to four decimal places. -0.0 is a valid result for rounding a very small number.
# https://www.deep-ml.com/problems/15?from=Machine%20Learning

import numpy as np
import matplotlib.pyplot as plt

def augment(X: np.ndarray) -> np.ndarray:
    num_records: int
    num_records, _ = X.shape
    ones: np.ndarray = np.ones(shape=(num_records, 1))
    return np.hstack([ones, X])

def loss_fn(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return 0.5 * (1 / len(y_true)) * np.linalg.norm(y_true - y_pred)

def grad_loss_fn(X: np.ndarray, y: np.ndarray, theta: np.ndarray) -> np.ndarray:
    return (1 / len(y)) * X.T @ (X @ theta - y)

def gradient_descent(X: np.ndarray, y: np.ndarray, theta: np.ndarray, alpha: float) -> np.ndarray:
    grad_loss: np.ndarray = grad_loss_fn(X, y, theta)
    return theta - alpha * grad_loss

def predict(X: np.ndarray, theta: np.ndarray) -> np.ndarray:
    return X @ theta

def linear_regression(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> dict[str, np.ndarray]:
    num_features: int
    _, num_features = X.shape

    X_augmented: np.ndarray = augment(X)
    theta: np.ndarray = np.random.randn(num_features + 1)

    losses: list[float] = []

    for iter in range(iterations):
        # Prediction & Loss Compute
        y_pred: np.ndarray = predict(X_augmented, theta)
        loss: float = loss_fn(y, y_pred)
        losses.append(loss)

        # Parameter update
        theta_old: np.ndarray = theta.copy()
        theta = gradient_descent(X_augmented, y, theta, alpha)

        # Check for convergence
        if (theta_old == theta).all():
            break
    
    return {'weights': theta, 'losses': np.array(losses)}

def plot_loss(losses: np.ndarray, filename: str = 'loss.png') -> None:
    plt.plot(losses)
    plt.xlabel('Epochs')
    plt.ylabel('Mean Squared Error')
    plt.grid(True)
    plt.title('Loss Curve for Linear Regression')
    plt.tight_layout()
    plt.savefig(filename)

def compute_r2(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    mean: float = y_true.mean()
    return 1 - ((y_true - y_pred) ** 2).sum() / ((y_true - mean) ** 2).sum()


def main(input_file: str = 'input.txt', output_file: str = 'output.txt') -> None:
    from ast import literal_eval

    with open(input_file, mode='r', encoding='utf-8') as in_file:
        data = in_file.readlines()
        X: np.ndarray = np.array(literal_eval(data[0]))
        y: np.ndarray = np.array(literal_eval(data[1]))
        alpha: float = literal_eval(data[2])
        iterations: int = literal_eval(data[3])

    regression: dict[str, np.ndarray] = linear_regression(X, y, alpha, iterations)
    theta: np.ndarray = regression['weights']
    losses: list[float] = regression['losses']
    r2_score = compute_r2(y, predict(augment(X), theta))

    plot_loss(losses)

    with open(output_file, mode='w', encoding='utf-8') as out_file:
        out_file.writelines([f'Weights: {np.round(theta, 4)}\n',
                             f'R2 Score: {r2_score:.4f}\n'])
        

if __name__ == '__main__':
    main()