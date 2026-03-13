import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    pass
    x = np.asarray(x)
    if rng is not None:
        mask = rng.random((x.shape))
        mask = mask < (1-p)
        mask = mask / (1 - p)
        x = x * mask
    else:
        mask = np.random.random(x.shape)
        mask = mask < (1-p)
        mask = mask / (1 - p)
        x = x * mask
    return (x, mask)