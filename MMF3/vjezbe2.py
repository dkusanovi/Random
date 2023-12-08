import numpy as np
import math
import matplotlib.pyplot as plt



def f(x):
    return np.exp(x)


def second_derivative(x, h):
    second = (f(x+h)-2*f(x)+f(x-h))/h**2
    return second


hlist = [10**(-6), 10**(-5), 10**(-4), 10**(-3), 10**(-2), 10**(-1)]




for i in range(0, 11): # broj ikseva
    f(i)
    for ii in range(0,5): # broj hova

        second_derivative(i, hlist[ii])





with open('vjezba2_table.txt', 'w') as g:
    g.writelines("%20s %20s %20s %20s %20s %20s %20s %20s %20s %20s %20s %20s %20s" %("x", "10^(-6)", "10^(-5)", "10^(-4)", "10^(-3)", "10^(-2)", "10^(-1)", "error 10^(-6)", "error 10^(-5)", "error 10^(-4)", "error 10^(-3)", "error 10^(-2)", "error 10^(-1)"))

    g.write('\n')

    for i in range(0, 11):
        e0 = abs(second_derivative(i, hlist[0]) - math.exp(i))
        e1 = abs(second_derivative(i, hlist[1]) - math.exp(i))
        e2 = abs(second_derivative(i, hlist[2]) - math.exp(i))
        e3 = abs(second_derivative(i, hlist[3]) - math.exp(i))
        e4 = abs(second_derivative(i, hlist[3]) - math.exp(i))
        e5 = abs(second_derivative(i, hlist[5]) - math.exp(i))

        error0 = e0/math.exp(i)
        error1 = e1/math.exp(i)
        error2 = e2/math.exp(i)
        error3 = e3/math.exp(i)
        error4 = e4/math.exp(i)
        error5 = e5/math.exp(i)

        g.writelines("\n%+20d %+20d %+20.6e %+20.6e %+20.6e %+20.6e %+20.6e %+20.6e %+20.6e %+20.6e %+20.6e %+20.6e %+20.6e" %(i, second_derivative(i, hlist[0]), second_derivative(i, hlist[1]), second_derivative(i, hlist[2]),second_derivative(i, hlist[3]),second_derivative(i, hlist[4]),second_derivative(i, hlist[5]), error0, error1, error2, error3, error4, error5))


    g.close()

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].set_xscale("log")
axes[1].set_xscale("log")
axes[2].set_xscale("log")

axes[0].set_yscale("log")
axes[1].set_yscale("log")
axes[2].set_yscale("log")


errorx1, errorx5, errorx10 = [], [], []

for k in range(0, 6):
    errorx1.append(abs(second_derivative(1, hlist[k]) - math.exp(1))/math.exp(1))
    errorx5.append(abs(second_derivative(5, hlist[k]) - math.exp(5))/math.exp(5))
    errorx10.append(abs(second_derivative(10, hlist[k]) - math.exp(10))/math.exp(10))

axes[0].plot(hlist, errorx1, color="indigo")
axes[1].plot(hlist, errorx5, color="orange")
axes[2].plot(hlist, errorx10)

axes[0].set_title('x = 1')
axes[1].set_title('x = 5')
axes[2].set_title('x = 10')

axes[0].set(xlabel='h', ylabel='relative error')
axes[1].set(xlabel='h', ylabel='relative error')
axes[2].set(xlabel='h', ylabel='relative error')

axes[0].grid()
axes[1].grid()
axes[2].grid()

plt.show()