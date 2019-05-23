import numpy as np
import matplotlib.pylab as plt

x=np.loadtxt("datos.dat", usecols=1)
y=np.loadtxt("datos.dat", usecols=2)

plt.figure()
plt.plot(x,y,color='green',label='Simulation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig('CordobaCarlos_final_15.pdf')