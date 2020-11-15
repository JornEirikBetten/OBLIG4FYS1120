import numpy as np
import matplotlib.pyplot as plt

def bfieldlist(r, rlist, dlist): 
	B = np.array([0,0,0])
	for i in range(len(rlist)): 
		ri = rlist[i]
		dli = dlist[i]
		R = r-ri
		Rnorm = np.linalg.norm(R)
		dB = np.cross(dli,R)/Rnorm**3 #Biot-Savarts B = IxR/R^3 (konstant er utelatt)
		B = B +dB  
	return B

#Sette opp listene

N = 100
a = 1.0
dl = 2*np.pi*a/N
rlist1 = []
dlist = []
rlist2 = []

for i in range(N): 
	thetai = i/N*2*np.pi
	ri = np.array([a*np.cos(thetai), a*np.sin(thetai), a/2])
	ri2 = np.array([a*np.cos(thetai), a*np.sin(thetai), -a/2])
	rlist1.append(ri)
	rlist2.append(ri2)
	dli = np.array([-dl*np.sin(thetai), dl*np.cos(thetai), 0])
	dlist.append(dli)
	
plt.figure(figsize=(6,6)) # Plott av den ene ringen. 
for i in range(N): 
	ri = rlist1[i]
	plt.plot(ri[0], ri[1], 'ob')
plt.xlabel('x/a')
plt.ylabel('y/a')
plt.show()


L = 5
NL = 20
x = np.linspace(-L, L, NL)
y = np.linspace(-L, L, NL)
z = np.linspace(-L, L, NL)
rx, rz = np.meshgrid(x,z)
rx, ry = np.meshgrid(x, y)
ry, rz = np.meshgrid(y, z) 

Bx1 = rx.copy()
Bx2 = rx.copy()
Bz1 = rz.copy()
Bz2 = rz.copy()
Bx = rx.copy()
Bz = rz.copy()
By1 = ry.copy()
By2 = ry.copy()
By = ry.copy()
# Finner magnetfeltet i x- og z-retningene generert av de to ringene. 

for i in range(len(rx.flat)): 
	r = np.array([rx.flat[i], 0.0, rz.flat[i]])
	Bx1.flat[i], By1, Bz1.flat[i] = bfieldlist(r, rlist1, dlist) #Magnetfeltet fra ringen med senter i (0,0,a/2)
	Bx2.flat[i], By2, Bz2.flat[i] = -bfieldlist(r, rlist2, dlist) # Magnetfeltet fra ringen med senter i (0,0,-a/2)
	Bx.flat[i] = Bx1.flat[i]+Bx2.flat[i] # Det totale magnetfeltet i x-retning
	By = By1 + By2
	Bz.flat[i] = Bz1.flat[i]+Bz2.flat[i] # Det totale magnetfeltet i z-retning
"""	
for i in range(len(rx.flat)): 
	r = np.array([rx.flat[i], ry.flat[i], 0.0])
	Bx1.flat[i], By1.flat[i], Bz1 = bfieldlist(r, rlist1, dlist) #Magnetfeltet fra ringen med senter i (0,0,a/2)
	Bx2.flat[i], By2.flat[i], Bz2 = -bfieldlist(r, rlist2, dlist) # Magnetfeltet fra ringen med senter i (0,0,-a/2)
	Bx.flat[i] = Bx1.flat[i]+Bx2.flat[i] # Det totale magnetfeltet i x-retning
	By.flat[i] = By1.flat[i]+By2.flat[i] # Det totale magnetfeltet i y-retning
"""
plt.figure(figsize=(7,7))
plt.streamplot(x,z,Bx, Bz) # Streamplot av magnetfeltet
plt.xlabel('x/a')
plt.ylabel('z/a')
plt.show()

Bmag = np.sqrt(Bx*Bx+Bz*Bz)
uBx =Bx/Bmag
uBz = Bz/Bmag
Bcolor = np.log10(Bmag)
fig = plt.figure(figsize=(8,8))
Q = plt.quiver(rx, rz, uBx, uBz, Bcolor, cmap='jet') # Quiverplott av magnetfeltet
fig.colorbar(Q, extend='max')
plt.xlabel(r'$\frac{x}{a}$')
plt.ylabel(r'$\frac{z}{a}$')
plt.show()

