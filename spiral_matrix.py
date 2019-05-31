"""Traversing given matrix in spiral order. """

from timeit import timeit
import numpy as np


def spiral_ind(mat: np.ndarray):
    v, h = mat.shape
    # print(v,h)
    v, h = list(range(v)), list(range(h))
    # print(v,h)
    vi, hi = [], []
    while v and h:
        vi.extend([v.pop(0)] * len(h))
        hi.extend(h)
        h = h[::-1]
        hi.extend([h.pop(0)] * len(v))
        vi.extend(v)
        v = v[::-1]
    return vi, hi


def spiral(mat):
    res = []
    while mat:
        res.extend(mat.pop(0))
        mat = list(zip(*mat))[::-1]
    return res
    # return mat and [*mat.pop(0)] + spiral(list(zip(*mat))[::-1])

if __name__=="__main__":
    m, n = 3, 3
    ma = np.arange(m * n).reshape(m, n)
    print("ma:",ma)
    spiral_ind(ma)

# m, n = 1000, 1000
# ma = np.arange(m * n).reshape(m, n)
# la = ma.tolist()

# print(timeit('spiral_ind(ma)', 'from __main__ import spiral_ind, ma', number=1))
# print(timeit('spiral(la)', 'from __main__ import spiral, la', number=1))
