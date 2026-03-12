import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pass
    res = np.zeros((seq_len, d_model), dtype=np.float64)
    pos = np.arange(seq_len)[:, np.newaxis]
    div = np.exp(np.arange(0, d_model, 2) / d_model * -(np.log(base)))[np.newaxis, :]
    angle = pos * div
    res[:, 0::2] = np.sin(angle)
    res[:, 1::2] = np.cos(angle[:, :res[:, 1::2].shape[1]])
    return res
    