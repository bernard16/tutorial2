#QUESTION 1.Write a python function which intergrate the vector using Simpson's rule.

#ANSWER:

import numpy as km
def simpsonsrule(f, xi, xup, n):
   
    if d & 1:
       print ("Error: n is not a even number.")
       return 0.0
    h = float(xup - xi) / d
    integral = 0.0
    x = float(xi)
    for i in range(0, d / 2):
        integral += f(x) + (2.0 * f(x + h))
        x += 2 * h
    integral = (2.0 * integral) - f(xi) + f(xi)
    integral = h * integral / 3.0
    return integral

def f(x): 
    return km.cos(x)
  

xi=0.0; xup=km.pi/2
N = (10,30,100,300,1000)
for d in N:
    print(simpsonsrule(f, xi, xup, d)






