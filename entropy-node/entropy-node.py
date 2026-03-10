import numpy as np

def _log2(y):
    if y.any == 0: return 0.0
    return np.log2(y)
def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    pass
    inp = np.unique_counts(y)
    freq = inp.counts / len(y)
    return -np.sum(freq*_log2(freq))