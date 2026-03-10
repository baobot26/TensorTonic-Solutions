import numpy as np
def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    unique_a = np.unique(set_a)
    unique_b = np.unique(set_b)
    a_and_b = np.intersect1d(unique_a, unique_b)
    a_or_b = np.union1d(unique_a, unique_b)
    if a_or_b.size == 0: return 0.0
    return a_and_b.size / a_or_b.size