#import scipy
from scipy.integrate import odeint,solve_ivp
import numpy as np
from scipy import stats
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import scipy.optimize as optimize

#%%
def model(t, T, k):
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
  k1, k2, k3, T_HW, T_ENV, m, rho, cp, t_stop = k
  T1 = T[0]
  T2 = T[1]
  if t > t_stop:
    T_HW = T1
#  f = [(k1*(T_HW-T1))-(k3*(T2-T_ENV)),k2*(T1-T2)]
#  f = [k2*(T1-T2),(k1*(T_HW-T1))-(k3*(T2-T_ENV))]
  dT1dt = (k1*(T_HW-T1))-k2*(T1-T2)
  dT2dt = k2*(T1-T2)-(k3*(T2-T_ENV))
  dTdt = [dT1dt,dT2dt]
  # convert to np.array
  dTdt = np.array(dTdt)
  m = np.array(m)
  rho = np.array(rho)
  cp = np.array(cp)
  dTdt = dTdt/(m*rho*cp)
  return dTdt
#%%
# Parameter values
k1 = 2000
k2 = 100000
k3 = 190
T_HW = 70
T_ENV = 20
m1 = 1000
m2 = 1000
rho1 = 1.033731
rho2 = 1.033731
cp1 = 3.85
cp2 = 3.85
t_stop = 11

#Initial conditions
T1 = 10
T2 = 10

#ODE solver parameters
abserr = 1.0e-8
relerr = 1.0e-6
starttime= 0
stoptime = 11
step = 0.001

# Create the time samples for the output of the ODE solver.
t = np.arange(starttime,stoptime+step,step)

# Pack up the parameters and initial conditions:
T0 = [T1,T2]
k = [k1,k2,k3,T_HW,T_ENV,[m1,m2],[rho1,rho2],[cp1,cp2],t_stop]

# Call the ODE solver.
#wsol = odeint(vectorfield, T0, t, args=(k,), atol=abserr, rtol=relerr)

#def upward_cannon(t, y): return [y[1], -0.5]
#def hit_ground(t, y): return y[1]
#def stopevent(t, T):
#    out=1
#    if sol.y[1][-2] > sol.y[1][-1]:
#        out = -0.1
#    return out
#stopevent.terminal = True
#stopevent.direction = -1
#sol = solve_ivp(vectorfield, [0, 100], [0, 10], events=hit_ground)
fun=lambda t, T: model(t,T,k)
#sol = solve_ivp(upward_cannon,[0,10],T0,events=event)
sol = solve_ivp(fun,[0,stoptime+step],T0,t_eval=t)#,events=stopevent)

print(sol.t_events)
print(sol.t)
print(sol.y)
plt.plot(sol.t,sol.y[0])
plt.plot(sol.t,sol.y[1])
plt.show

t_max = sol.t[np.where(sol.y[1]==np.amax(sol.y[1]))]
T_stop = sol.y[1][np.where(sol.t==t_stop)]
T_max = np.amax(sol.y[1])

print t_max[0]*60
print T_stop[0]

out = []
for i in range(len(t)):
    out = out+[abs(sol.y[1][i-1]-sol.y[1][i])]
   
#%%
# The critical Temperature has a linear dependency
T_crit=[]
T_crit_all=[]
T_stats=[]
T_start=50
T_end=70
T_step=5
for i in range(T_start,T_end+T_step,T_step):
    try:
        slope, intercept, r_value, p_value, std_err = stats.linregress(T_crit.transpose()[2],T_crit.transpose()[0])
        plt.plot(T_crit.transpose()[2],T_crit.transpose()[0])
        try:
            T_stats = np.concatenate([T_stats,np.array([[slope, intercept, r_value, p_value, std_err]])])
        except:
            T_stats = np.array([[slope, intercept, r_value, p_value, std_err]])
            
        try:
            T_crit_all = np.concatenate([T_crit_all,T_crit])
            T_crit = []
        except:
            T_crit_all = T_crit
            T_crit = []
    except:
        print 'exception'
    for j in t:
        T_HW = i
        t_stop = j
        k = [k1,k2,k3,T_HW,T_ENV,[m1,m2],[rho1,rho2],[cp1,cp2],t_stop]
        fun=lambda t, T: model(t,T,k)
        sol = solve_ivp(fun,[starttime,stoptime+step],T0,t_eval=t)
        #t_max = sol.t[np.where(sol.y[1]==np.amax(sol.y[1]))]
        T_stop = sol.y[1][np.where(sol.t==t_stop)]
        T_max = np.amax(sol.y[1])
        newdata = np.array([[(T_max - T_stop)[0],T_stop[0],T_max,i,j]])
        if T_max == sol.y[1][-1]:
            continue
        else:
            try:
                T_crit = np.concatenate([T_crit,newdata])
            except:
                T_crit = newdata
plt.show()
plt.plot(range(T_start,T_end,T_step),T_stats.transpose()[1])
plt.show()
T_stats2 = np.asarray(stats.linregress(range(T_start,T_end,T_step),T_stats.transpose()[1]))
#%%
def costfunction(t):
    fun=lambda t, T: model(t,T,k)
    sol = solve_ivp(fun,[0,stoptime+step],T0,t_eval=t,events=stopevent)
    sol.t[np.where(sol.y[1]==max(sol.y[1]))]

#%%

# function that returns dz/dt
def model(z,t,u):
    x = z[0]
    y = z[1]
    dxdt = (-x + u)/5.0
    dydt = (-y + x)/5.0
    dzdt = [dxdt,dydt]
#    dzdt = [(-y + x)/5.0,(-x + u)/2.0]
    return dzdt

# initial condition
z0 = [0,0]

# number of time points
n = 401

# time points
t = np.linspace(0,40,n)

# step input
u = np.zeros(n)
# change to 2.0 at time = 5.0
u[102:] = 2.0

# store solution
x = np.empty_like(t)
y = np.empty_like(t)
# record initial conditions
x[0] = z0[0]
y[0] = z0[1]

# solve ODE
for i in range(1,n):
    # span for next time step
    tspan = [t[i-1],t[i]]
    # solve for next step
    z = odeint(model,z0,tspan,args=(u[i],))
    # store solution for plotting
    x[i] = z[1][0]
    y[i] = z[1][1]
    # next initial condition
    z0 = z[1]

# plot results
plt.plot(t,u,'g:',label='u(t)')
plt.plot(t,x,'b-',label='x(t)')
plt.plot(t,y,'r--',label='y(t)')
plt.ylabel('values')
plt.xlabel('time')
plt.legend(loc='best')
plt.show()
#%%

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

