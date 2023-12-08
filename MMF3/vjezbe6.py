import math
import numpy as np
import matplotlib.pyplot as plt


m = 3.37*10**(-26)
T = 300
k = 1.38064852*10**(-23)

v1 = 559.4 - 50
v2 = 559.4 + 50



def f(v):
    y = (m/(2*math.pi*k*T))**(3/2)*4*math.pi*v**2*math.exp(-(m*v**2)/(2*k*T))
    return y



def trapez(lower, upper, m):
    h = (upper-lower)/m
    br = 0.5 * (f(lower) + f(upper))*h

    for i in range(1, m):
        br = br + h*f(lower+i*h)
    return br

print('trapez 10 tocaka:', trapez(v1, v2, 10))
print('trapez 50 tocaka:', trapez(v1, v2, 50))
print('trapez 100 tocaka:', trapez(v1, v2, 100))




def simpson(lower, upper, m):
    h = (upper-lower)/m
    br = (f(lower) + f(upper))*h*1/3

    for i in range(1, m):
        if (i % 2) == 0:
            br = br + 2*f(lower+i*h)*h/3
        else:
            br = br + 4*f(lower+i*h)*h/3

    return br

print('simpson 10 tocaka:', simpson(v1, v2, 10))
print('simpson 50 tocaka:', simpson(v1, v2, 50))
print('simpson 100 tocaka:', simpson(v1, v2, 100))




#include <stdio.h> 
#include <math.h>
#include <malloc.h>
#include <stdlib.h>

# void gauleg(float x1, float x2, float x[], float w[], int n)
# //Given the lower and upper limits of integration x1 and x2, and given n, this routine returns arrays x[1..n] and w[1..n] of length n, containing the abscissas and weights of the Gauss-Legendre n-point quadrature formula. 
# // **********
# {
#         double EPS=0.000001;	
# 	int m,j,i;
# 	double z1,z,xm,xl,pp,p3,p2,p1;       # definiramo varijable

# // ************************
# 	m=(n+1)/2;                            # m je brojač
# // ************************
#        xm=0.5*(x2+x1);                  # xm je sredina intervala
# // ************************
#        xl=0.5*(x2-x1);                  # xl je pola intervala

# // ************************
#   	for (i=1;i<=m;i++)                 # for petlja za određivanje nultočaka
#       {
# // ************************
# 	z=cos(3.141592654*(i-0.25)/(n+0.5));    # za svaku nultočku odabiremo početnu vrijednost 

#   do {                                     # while petlja
# //************************
# 	p1=1.0;                               
# 	p2=0.0;
# // ************************
# 	for (j=1;j<=n;j++) {
#         p3=p2;                            # for petlja
# 	p2=p1;
# // ************************
# 	p1=((2.0*j-1.0)*z*p2-(j-1.0)*p3)/j;     # rekurzivna formula za računanje Legendrovih polinoma
# 	}    
# // ************************

# 	pp=n*(z*p1-p2)/(z*z-1.0);               # rekurzivna formula za računanje derivacija Legendrovog polinoma
# // ************************
# 	z1=z;
# 	z=z1-p1/pp;

#    } while (fabs(z-z1) > EPS);        # uvjeti za while petlju
# //************************
# //  ************************
# 	x[i]=xm-xl*z;                       # for petlja nađe jednu nultočku z pa u x upisujemo nultočke
# 	x[n+1-i]=xm+xl*z;
# // ************************
# 	w[i]=2.0*xl/((1.0-z*z)*pp*pp);      # računanje težine
# 	w[n+1-i]=w[i];

#        } // ************************
  
# }



def gauge(x1, x2, n):
    x = []
    w = []
    EPS = 0.000001
    
    for k in range(0, n+1):
        x.append(k)
        w.append(k)

    m = int((n+1)/2)
    xm = 0.5*(x2 + x1)
    xl = 0.5*(x2 - x1)

    for i in range(1, m+1):
        z=math.cos(math.pi*(i - 0.25)/(n + 0.5))

        while True:
            p1 = 1
            p2 = 0

            for j in range(1, n+1):
                p3 = p2
                p2 = p1
                p1 = ((2*j - 1)*z*p2-(j - 1)*p3)/j

            pp = n*(z*p1 - p2)/(z*z - 1)
            z1 = z
            z = z1 - p1/pp

            if (abs(z-z1) < EPS):      # do while ima obrnuto značenje od if
                break

        x[i] = xm - xl*z
        x[n+1-i] = xm + xl*z

        w[i] = 2*xl/((1-z*z)*pp*pp)
        w[n+1-i] = w[i]

        I = 0

        for i in range(1, len(x)):
            I = I + f(x[i])*w[i]

    return I, n


print('GauLeg za',  gauge(v1, v2, 10)[1], 'tocaka:', gauge(v1, v2, 10)[0])
print('GauLeg za',  gauge(v1, v2, 50)[1], 'tocaka:', gauge(v1, v2, 50)[0])
print('GauLeg za',  gauge(v1, v2, 100)[1], 'tocaka:', gauge(v1, v2, 100)[0])