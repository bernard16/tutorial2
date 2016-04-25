## The difference of the two Area can be seen by integrating the function in to two parts, 
## like in this case the integration from -pi to pi is 1st part from -pi to 1 and 2nd part 
## 1 to pi, Therefore, 1st integral is the sum of the two parts and the 2nd interation is
## just the 1st only 
import numpy
import scipy.integrate as quad
def mygauss(x,cent=0,sig=0.1):
    return numpy.exp(-0.5*(x-cent)**2/sig**2)

I,err=quad.quad(mygauss,-numpy.pi-,numpy.pi) 
print I
I1,err=quad.quad(mygauss,-numpy.pi,1)
print I1
I2,err=quad.quad(mygauss, 1,numpy.pi)
print I2
