import math
from numpy import arange
import matplotlib.pyplot as plt

N_1 = 10
N_2 = 20
N_3 = 30
segment = [0, 1]
a = 0
b = 1
h_1 = 1 / N_1
h_2 = 1 / N_2
h_3 = 1 / N_3
y_0 = 1
x_0 = 0


def y(x):
    return 2 * math.pow(math.e, -2 * (x ** 2)) - 1


def function(x, y):
    return -4 * x * (y+1)


def get_precise_values(n):
    x_values = [a]
    y_values = [y_0]
    h = (b - a) / n
    for i in range(1, n + 1):
        x = a + h * i
        x_values.append(x)
        y_values.append(y(x))
    plt.plot(x_values, y_values, label=f"y(x) {n}")


def method_eiler(h, a, b):
    values = []
    for i in arange(a + h, b + h, h):
        values.append(i)
    y_previous = y_0
    y_values = [y_previous]
    for x in values:
        y_current = y_previous + function(x, y_previous) * h
        y_values.append(y_current)
        y_previous = y_current
    values.insert(0, x_0)
    plt.plot(values, y_values, label=f'h={h}, eiler')


def method_koshi(h, a, b):
    values = []
    for i in arange(a + h, b + h, h):
        values.append(i)
    y_previous = y_0
    y_values = [y_previous]
    for x in values:
        y_k_and_half = y_previous + (h / 2) * function(x, y_previous)
        x_k_and_half = x + h / 2
        y_current = y_previous + function(x_k_and_half, y_k_and_half) * h
        y_values.append(y_current)
        y_previous = y_current
    values.insert(0, x_0)
    plt.plot(values, y_values, label=f'h={h}, koshi')


def runges_method(h, x, y):
    k1 = h * function(x, y)
    k2 = h * function(x + h / 2, y + k1 / 2)
    k3 = h * function(x + h / 2, y + k2 / 2)
    k4 = h * function(x + h, y + k3)
    return y + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


def adams_multon_method(h, a, b):
    y_1 = runges_method(h, x_0, y_0)
    values = []
    y_values = []
    for i in arange(a + h, b + h, h):
        values.append(i)
    y_pre_previous = y_0
    y_previous = y_1
    x_pre_previous = values[0]
    x_previous = values[1]
    y_values.append(y_0)
    y_values.append(y_1)
    for x in values:
        y_current_razgon = runges_method(h, x_previous, y_previous)
        y_current = y_previous + (h / 12) * (
                5 * function(x, y_current_razgon) +
                8 * function(x_previous, y_previous)
                - function(x_pre_previous, y_pre_previous))
        y_pre_previous = y_previous
        y_previous = y_current
        x_pre_previous = x_previous
        x_previous = x
        y_values.append(y_current)
    values.insert(0, x_0)
    values.insert(1, x_0 + h)
    plt.plot(values, y_values, label=f'h={h}, adams-multon')


if __name__ == '__main__':
    get_precise_values(500)
    method_eiler(h_1, a, b)
    method_eiler(h_2, a, b)
    method_eiler(h_3, a, b)
    method_koshi(h_1, a, b)
    method_koshi(h_2, a, b)
    method_koshi(h_3, a, b)
    adams_multon_method(h_1, a, b)
    adams_multon_method(h_2, a, b)
    adams_multon_method(h_3, a, b)
    plt.legend()
    plt.show()
