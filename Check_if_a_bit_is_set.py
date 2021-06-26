def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return 1
    else:
        return 0