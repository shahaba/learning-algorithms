# Counting Sort


def counting_sort(A, M):
    counts = [0] * M
    for v in A:
        counts[v] += 1

    pos = 0
    v = 0
    while pos < len(A):
        for idx in range(counts[v]):
            A[pos + idx] = v
        pos += counts[v]
        v += 1

    print(counts)


def counting_sort_updated(A, M):
    counts = [0] * M
    for v in A:
        counts[v] += 1

    pos = 0
    v = 0
    while pos < len(A):
        A[pos : pos + v] = [v] * counts[v]
        pos += counts[v]
        v += 1

    print(counts)


if __name__ == "__main__":
    counting_sort([1, 2, 3, 4], 5)
    counting_sort_updated([1, 2, 3, 4], 5)
