def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    a = set(set_a)
    b = set(set_b)
    if len(a.union(b)) == 0: return 0.0
    return len(a.intersection(b)) / len(a.union(b))