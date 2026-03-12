import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    """
    # Write code here
    pass
    x = np.asarray(x, dtype=np.float64)
    return np.percentile(x, q)
    
    