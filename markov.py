import numpy


def power_of(m, n):
    last = m
    for i in range(n):
        last = numpy.matmul(last, m)
    return last


m = numpy.array([[0.6, 0.2, 0.2], [0.1, 0.8, 0.1], [0.6, 0, 0.4]])
print(power_of(m, 100))
print(power_of(m, 1000))
print(power_of(m, 10000))
