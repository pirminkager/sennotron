#import scipy
from scipy.integrate import odeint

def vectorfield(T, t, k):
  """
    Defines the differential equations for the Sennkessel.

    Arguments:
        T :  vector of the state variables:
                  w = [x1,y1,x2,y2]
		  T = [T1,T2]
        t :  time
        k :  vector of the parameters:
                  p = [m1,m2,k1,k2,L1,L2,b1,b2]
  """

  k1, k2, k3, T_HW, T_ENV = k
  T1, T2, T3 = T

  f = [(k1*(T_HW-T1))-(k3*(T2-T_ENV)),
      k2*(T1-T2),
      k3*(T2-T_ENV)]

  return f

# Parameter values
k1 = 1000
k2 = 10000000
k3 = 100
T_HW = 70
T_ENV = 20

#Initial conditions
T1 = 10
T2 = T1
T3 = T2

#ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 250

# Create the time samples for the output of the ODE solver.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

# Pack up the parameters and initial conditions:
T0 = [T1,T2,T3]
k = [k1,k2,k3,T_HW,T_ENV]

# Call the ODE solver.
wsol = odeint(vectorfield, T0, t, args=(k,), atol=abserr, rtol=relerr)

with open('output.dat', 'w') as f:
    # Print & save the solution.
    for t1, T1 in zip(t, wsol):
       print >> f, t1, T1[0], T1[1]


if __name__ == "__main__":
  import matplotlib
  matplotlib.use('GTK')
  import matplotlib.pyplot as plt
  print 'hello'
##
