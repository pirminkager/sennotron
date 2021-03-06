#import scipy
from scipy.integrate import odeint

def vectorfield(T, t, k):
  """
    Defines the differential equations for the Sennkessel.

    Arguments:
        T :  vector of the state variables:
                  w = [x1,x2]
		  T = [T1,T2]
        t :  time
        k :  vector of the parameters:
                  p = [m1,m2,k1,k2,L1,L2,b1,b2]
  """

  k1, k2, k3, T_HW, T_ENV = k
  T1, T2 = T
  if t > 0.5:
    T_HW = T1
  f = [(k1*(T_HW-T1))-(k3*(T2-T_ENV)),
      k2*(T1-T2)]

  return f

# Parameter values
k1 = 1
k2 = 80
k3 = 0.01
T_HW = 70
T_ENV = 20

#Initial conditions
T1 = 10
T2 = T1

#ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 1.0
numpoints = 250

# Create the time samples for the output of the ODE solver.
t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

# Pack up the parameters and initial conditions:
T0 = [T1,T2]
k = [k1,k2,k3,T_HW,T_ENV]

# Call the ODE solver.
wsol = odeint(vectorfield, T0, t, args=(k,), atol=abserr, rtol=relerr)

with open('output.dat', 'w') as f:
    # Print & save the solution.
    for t1, T1 in zip(t, wsol):
       print >> f, t1, T1[0], T1[1]


if __name__ == "__main__":
  import matplotlib
#  matplotlib.use('GTK')
  import matplotlib.pyplot as plt
  from numpy import loadtxt
  from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig
  from matplotlib.font_manager import FontProperties

  t, x1, x2 = loadtxt('output.dat', unpack=True)

  figure(1, figsize=(6, 4.5))

  xlabel('t')
  grid(True)
  hold(True)
  lw = 1

  plot(t, x1, 'b', linewidth=lw)
  plot(t, x2, 'g', linewidth=lw)

  legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
  title('Titel')
  plt.show()
#  savefig('plot.png', dpi=100)

