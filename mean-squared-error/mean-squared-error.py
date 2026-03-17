import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    pass
    y_pred = np.asarray(y_pred)
    y_true = np.asarray(y_true)
    return np.sum(np.square(y_pred-y_true)) / y_pred.size