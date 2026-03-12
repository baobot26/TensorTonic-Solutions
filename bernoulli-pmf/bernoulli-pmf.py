import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    pass
    mean = p
    var = p * (1 - p)
    pmf = np.zeros(len(x))
    for i in range(len(x)):
        pmf[i] = p if x[i] == 1 else 1 - p
    return (pmf, mean, var)