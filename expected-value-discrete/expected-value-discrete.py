import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    pass
    x = np.asarray(x, dtype=np.float64)
    p = np.asarray(p, dtype=np.float64)
    if x.shape != p.shape:
        raise ValueError("")
    if not np.all(p>=0): raise ValueError("")
    if not np.allclose(np.sum(p), 1.0, atol=1e-6): raise ValueError("")
    return x @ p
