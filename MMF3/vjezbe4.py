def jedan():
    a = [0, 1, 2, 3, 4, 5, 6]
    b = [2, 4, 6, 8, 6, 4, 2]
    c = [6, 5, 4, 3, 2, 1, 0]
    d = [0, 1, 2, 3, 2, 1, 0]

    n = len(d) - 1

    ccc = [c[0]/b[0]]
    dcc = [d[0]/b[0]]
    

    for i in range (1, n):
        ccc.append((c[i])/(b[i]-a[i]*ccc[i-1]))
        dcc.append((d[i]-a[i]*dcc[i-1])/(b[i]-a[i]*ccc[i-1]))

    dcc.append((d[n]-a[n]*dcc[n-1])/(b[n]-a[n]*ccc[n-1]))

    x = [dcc[n]]
    x14 = []


    for j in range(1, n+1):
        k = n - j
        x.append(dcc[k]-ccc[k]*x[j-1])

    print(x)


    for l in range(0, len(x)):
        x14.append(round(14*x[l]))

    print(x14)




def dva():
    a = [0, -2, -2, -2]
    b = [4, 6, 6, 8]
    c = [-2, -2, -2, 0]
    d = [5, 0, 0, 0]


    n = len(d) - 1

    ccc = [c[0]/b[0]]
    dcc = [d[0]/b[0]]
    

    for i in range (1, n):
        ccc.append((c[i])/(b[i]-a[i]*ccc[i-1]))
        dcc.append((d[i]-a[i]*dcc[i-1])/(b[i]-a[i]*ccc[i-1]))

    dcc.append((d[n]-a[n]*dcc[n-1])/(b[n]-a[n]*ccc[n-1]))

    x = [dcc[n]]
    x94 = []

    for j in range(1, n+1):
        k = n - j
        x.append(dcc[k]-ccc[k]*x[j-1])
    x.reverse()

    print(x)


    for l in range(0, len(x)):
        x94.append(round(94*x[l]))

    print(x94)



jedan()
dva()