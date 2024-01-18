def prvi():
    a = [0, 1, 2, 3, 4]
    b = [1, 1, 1, 1, 1]
    c = [4, 3, 2, 1, 0]
    # d = [2, 4, 6, 8, 10]
    d = []

    n = len(a) - 1

    def f(xs):
        return xs**2+5
    
    h = 10**(-3)

    def derivacija(xs, h):
        der = (f(xs+h)-f(xs-h))/(2*h)
        return der

    for i in range(1, 6): # broj ikseva
        f(i)
        d.append(derivacija(i, h))
        print(derivacija(i, h))

    ccc = [c[0]/b[0]]
    dcc = [d[0]/b[0]]
    

    for i in range (1, n):
        ccc.append((c[i])/(b[i]-a[i]*ccc[i-1]))
        dcc.append((d[i]-a[i]*dcc[i-1])/(b[i]-a[i]*ccc[i-1]))

    dcc.append((d[n]-a[n]*dcc[n-1])/(b[n]-a[n]*ccc[n-1]))

    x = [dcc[n]]
    x15 = []

    for j in range(1, n+1):
        k = n - j
        x.append(dcc[k]-ccc[k]*x[j-1])
    x.reverse()

    print(x)

    for l in range(0, len(x)):
        x15.append(round(15*x[l]))

    print(x15)

prvi()