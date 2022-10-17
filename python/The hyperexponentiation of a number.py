import sys

sys.setrecursionlimit(1857)


def exponantiate(n, k):
    if k == 1:
        return n
    else:
        return pow(n, exponantiate(n, k - 1), 10 ** 8)


n, k = 1777, 1855
print(exponantiate(n, k) % 10 ** 8)
