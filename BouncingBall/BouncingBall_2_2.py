from math import sqrt
import matplotlib.pyplot as plt

h0 = 5         # m/s
v = 0          # m/s, current velocity
g = 10         # m/s/s
t = 0          # starting time
dt = 0.001     # time step
rho = 0.75     # coefficient of restitution
tau = 0.10     # contact time for bounce
hmax = h0      # keep track of the maximum height
h = h0
hstop = 0.01   # stop when bounce is less than 1 cm
freefall = True # state: freefall or in contact
t_last = -sqrt(2*h0/g) # time we would have launched to get to h0 at t=0
vmax = sqrt(2 * hmax * g)
H = []
T = []

def FreeFall():
  global h, v, t_last, t, hmax, freefall
  hnew = h + v * dt - 0.5 * g * dt * dt
  if (hnew < 0):
    t = t_last + 2 * sqrt(2 * hmax / g)
    freefall = False
    t_last = t + tau
    h = 0
  else:
    t = t + dt
    v = v - g * dt
    h = hnew
  hmax = 0.5*vmax*vmax/g
  print(h)
  H.append(h)
  T.append(t)
  return

def Bouncing():
  global vmax, h, v, t_last, t, hmax, freefall
  t = t + tau
  vmax = vmax * rho
  v = vmax
  freefall = True
  h = 0
  hmax = 0.5*vmax*vmax/g
  print(h)
  H.append(h)
  T.append(t)
  return

def Stop():
  return hmax < hstop

def isFreeFall():
  return freefall

def isBouncing():
  return not(freefall)

'''
while(hmax > hstop):
  if(freefall):
    FreeFall()
  else:
    Bouncing()

print("stopped bouncing at t=%.3f\n"%(t))

plt.figure()
plt.plot(T, H)
plt.xlabel('time')
plt.ylabel('height')
plt.title('bouncing ball')
plt.show()
'''