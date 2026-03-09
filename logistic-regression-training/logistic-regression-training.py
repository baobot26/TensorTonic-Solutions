import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    # Write code here
    pass
    w = np.zeros(X.shape[1])
    b = 0
    for step in range(steps):
        loss = np.sum(-y * np.log(_sigmoid(np.dot(X, w) + b)) - (1 - y) * np.log(_sigmoid(1 - np.dot(X, w) + b))) / len(y)
        dj_dw = np.dot(X.T, (_sigmoid(np.dot(X, w) + b) - y)) / len(y)
        dj_db = np.sum(_sigmoid(np.dot(X, w) + b) - y) / len(y)
        w = w - lr * dj_dw
        b = b - lr * dj_db
    return (w, b)