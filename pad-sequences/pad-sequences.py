import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # Your code here

    if not seqs: return np.array([[]])
    maxlen = max((len(s) for s in seqs), default=0)
    L = max_len if max_len is not None else maxlen
    N = len(seqs)
    res = np.full((N, L), pad_value, dtype=np.int32)
    for i, seq in enumerate(seqs):
        trunc = seq[:L]
        res[i, :len(trunc)] = trunc
    return res