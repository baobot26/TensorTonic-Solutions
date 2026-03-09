import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.asarray(x, dtype=float) #Cast the input into NumPy Array to use np.exp()
    return 1 / (1 + np.exp(-x)) #Sigmoid function: g(z) = 1 / (1 + e^-z)
