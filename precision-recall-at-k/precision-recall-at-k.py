def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    precision = len(set(recommended[:k]).intersection(relevant)) / k
    recall = len(set(recommended[:k]).intersection(relevant)) / len(relevant)
    return [precision, recall]