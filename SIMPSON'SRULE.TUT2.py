                                             TUTORIAL 2.

# QUESTION 2:Plot the error as a function of number of points using Simpson's rule and stundard sum, using log scale.

# ANSWER:

import numpy as km 
from matplotlib import pyplot as plt 
N = (1.0,1.0,1.0,1.0,1.0)
n = (10,30,100,300,1000)
#area for simpson's rule
Bbm = (1.05236326978,1.01745333429,1.00523598809,1.00174532926,1.00052359878)
#the area for standard sum
Dcm = (1.0764828026941022, 1.025951465275319, 1.0078334198735821, 
1.0026157092462991, 1.0007851925466307)
Esmp = abs(km.subtract(Bbm,N))
Eint = abs(km.subtract(Dcm,N))

plt.figure()
plt.semilogy(n, Esmp,
             color = 'blue',
             linewidth = 2)
plt.semilogy(n, Eint,
             color = 'red',
             linewidth = 2)
plt.title('semilog y-axis')
plt.grid(True)
