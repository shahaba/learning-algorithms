# Linear Time Median
from typing import List
import random


def partition(A, lo, hi, idx):
    """Partition using A[idx] as value."""
    if lo == hi:
        return lo

    A[idx], A[lo] = A[lo], A[idx]  # swap into position
    i = lo
    j = hi + 1
    while True:
        while True:
            i += 1
            if i == hi:
                break
            if A[lo] < A[i]:
                break

        while True:
            j -= 1
            if j == lo:
                break
            if A[j] < A[lo]:
                break

        if i >= j:
            break
        A[i], A[j] = A[j], A[i]

    A[lo], A[j] = A[j], A[lo]
    return j


def linear_median(A):
    """
    Efficient implementation that returns median value in arbitrary list,
    assuming A has an odd number of values. Note this algorithm will
    rearrange values in A.
    """
    lo = 0
    hi = len(A) - 1
    mid = hi // 2
    while lo < hi:
        idx = random.randint(lo, hi)  # select valid index randomly
        j = partition(A, lo, hi, idx)

        if j == mid:
            return A[j]
        if j < mid:
            lo = j + 1
        else:
            hi = j - 1
    return A[lo]


def median(array: List) -> int:
    array.sort()  # sort the given list
    n = len(array)

    return array[n // 2]


if __name__ == "__main__":
    mlist = [1, 2, 3, 4, 5]

    print(median((mlist)))
