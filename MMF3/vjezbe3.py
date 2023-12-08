import math


def f(t):
    y01 = 5
    y02 = 0.325
    AA = 1
    BB = 3
    C = 2
    D = 0.5
    y1 = y01 + AA*math.cos(BB*t)
    y2 = y02 + C*math.exp(D*t)
    y = y1 - y2
    return y

def derivative(t):
    AA = 1
    BB = 3
    C = 2
    D = 0.5
    y1_der = -AA*(math.sin(BB*t))*BB
    y2_der = C*math.exp(D*t)*D
    y_der = y1_der - y2_der
    return y_der

epsilon = 10**(-6)

def bisekcija(a, b):

    while abs(b-a) >= epsilon:
        c = (a+b)/2
        f_a = f(a)
        f_c = f(c)
        if (f_a*f_c) < 0:
            a = a
            b = c
        elif (f_a*f_c) > 0:
            b = b
            a = c
    print(c)


def newton_raphson(x, n):
    while (abs(f(x)/(derivative(x)))) >= epsilon:
        n = n + 1
        x = x - f(x)/derivative(x)
        if derivative(x) == 0:
            break
    print(x)


newton_raphson(3, 1)
bisekcija(0, 10)


# def metoda_sekante(f, x, epsilon):
#     # Metode sekante za trazenje nul-tocke funkcije u okolini tocke x uz nepoznatu derivaciju funkcije, uz ogranicenje epsilon.
#     def derivative(f, x, epsilon):
#         return (f(x+epsilon) - f(x-epsilon))/(2*epsilon)
#     k = 1
#     while abs(f(x)/derivative(f, x, epsilon)) > epsilon and k <= 500:
#         x = x - f(x)/derivative(f, x, epsilon)
#         k = k + 1
#     return x, k