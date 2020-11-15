import numpy as np
import matplotlib.pyplot as plt


# finner det magnetiske feltet langs z-aksen for en sløyfe med en radius rad. (Strømmen I, og konstanten mu0/4pi er utelatt. 
def z_mag(rad, z): 
	return 2*np.pi*rad**2/(np.sqrt(rad**2+z**2))**3

a = 1.0 # radiusen til ringene
L = 5
NL = 101
z = np.linspace(-L, L, NL)
# magnetfelt fra øvre ring og nedre ring
B_ring1 = []
B_ring2 = []
#Totalt magnetfelt (superposisjonsprinsippet) 
Bz = []
for i in range(len(z)): 
	B_ring1.append(z_mag(a, z[i]-a/2))
	B_ring2.append(-z_mag(a, z[i]+a/2))
	Bz.append(B_ring1[i]+B_ring2[i])

plt.plot(z, Bz) 
plt.xlabel('z/a') 
plt.ylabel(r'$B_z\frac{4\pi}{I\mu_0}$')
plt.show()

	

