import math


def SearchClosestPoints(x, y):
    dmin = float("inf")
    (imin, jmin) = (None, None)
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            d = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
            if d < dmin:
                dmin = d
                imin = i
                jmin = j
    return (imin, jmin)


def strcmp(s, p):
    n = len(s)
    m = len(p)
    for i in range(n - m):
        j = 0
        while j < m and s[i + j] == p[j]:
            j = j + 1
        if j == m:
            return i
    return None


def sum(a):
    sum = 0
    for i in range(len(a)):
        sum = sum + a[i]
    return sum


def sum_r(a, l, r):
    if l == r:
        return a[l]
    m = (r + l) / 2
    return sum_r(a, l, m - 1) + sum_r(a, m, r)


def sum_list(a):
    return sum_r(a, 0, len(a) - 1)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(strcmp('hello world', 'lo w'))
    print(SearchClosestPoints((3, 4, 5), (3, 4, 6)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
