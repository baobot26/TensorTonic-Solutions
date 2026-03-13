import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    pass
    s = np.asarray(s)
    g = np.asarray(g)
    w = np.asarray(w)
    s = beta * s + (1 - beta) * np.square(g)
    w = w - lr * g / np.sqrt(s + eps)
    return (w, s)