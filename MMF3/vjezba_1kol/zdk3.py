def treci():
    a = [0, -1, -1, -1, -1]
    b = [1, 2, 3, 4, 5]
    c = [-3, -3, -3, -3, 0]
    d = [5, 4, 3, 2, 1]

    n = len(d) - 1

    ccc = [c[0]/b[0]]
    dcc = [d[0]/b[0]]
    

    for i in range (1, n):
        ccc.append((c[i])/(b[i]-a[i]*ccc[i-1]))
        dcc.append((d[i]-a[i]*dcc[i-1])/(b[i]-a[i]*ccc[i-1]))

    dcc.append((d[n]-a[n]*dcc[n-1])/(b[n]-a[n]*ccc[n-1]))

    x = [dcc[n]]
    x29 = []


    for j in range(1, n+1):
        k = n - j
        x.append(dcc[k]-ccc[k]*x[j-1])

    print(x)


    for l in range(0, len(x)):
        x29.append(round(29*x[l]))

    print(x29)

treci()