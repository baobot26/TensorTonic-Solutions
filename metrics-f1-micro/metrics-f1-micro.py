def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    TP = 0
    mismatch = 0
    for i in range(len(y_true)):
        if (y_true[i] == y_pred[i]):
            TP += 1
        else: mismatch += 1
    return 2 * TP / (2 * TP + 2 * mismatch)