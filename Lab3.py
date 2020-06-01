# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 22:17:27 2019

@author: joshu
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:35:53 2019

@author: joshu
"""
from astropy.io import ascii
import numpy as np
from numpy import arctan,arccos
from numpy.polynomial.polynomial import polyfit
import matplotlib.pyplot as plt
from math import sin,cos

l1blue = ascii.read('halpha_blue.dat')
l1cyan= ascii.read('halpha_cyan.dat')
l1green = ascii.read('halpha_green.dat')
l1purple = ascii.read('halpha_purple.dat')
l1red = ascii.read('halpha_red.dat')

l2blue = ascii.read('O3_blue.dat')
l2cyan= ascii.read('O3_cyan.dat')
l2green = ascii.read('O3_green.dat')
l2purple = ascii.read('O3_purple.dat')
l2red = ascii.read('O3_red.dat')

l3blue = ascii.read('S3_blue.dat')
l3cyan= ascii.read('S3_cyan.dat')
l3green = ascii.read('S3_green.dat')
l3purple = ascii.read('S3_purple.dat')
l3red = ascii.read('S3_red.dat')


###H Alpha
'''
fig = plt.figure()
plt.scatter(l1blue['col1'],l1blue['col2'],color='blue')
plt.scatter(l1red['col1'],l1red['col2'],color='red')
plt.scatter(l1purple['col1'],l1purple['col2'],color='purple')
plt.scatter(l1cyan['col1'],l1cyan['col2'],color='cyan')
plt.scatter(l1green['col1'],l1green['col2'],color='limegreen')
#plt.ylim(-1,1)
plt.title("H Alpha Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
#fig.savefig('halphaa.png')
plt.show()
'''

fig = plt.figure()
plt.plot(l1blue['col1'],l1blue['col2'],color='blue')
plt.plot(l1red['col1'],l1red['col2'],color='red')
plt.plot(l1purple['col1'],l1purple['col2'],color='purple')
plt.plot(l1cyan['col1'],l1cyan['col2'],color='cyan')
plt.plot(l1green['col1'],l1green['col2'],color='limegreen')
plt.title("H Alpha Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
fig.savefig('halphab.png')
plt.show()

fig = plt.figure()
plt.plot(l1blue['col1'],l1blue['col2'],color='blue')
plt.plot(l1green['col1'],l1green['col2'],color='limegreen')
plt.title("H Alpha Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
fig.savefig('halphac.png')
plt.show()


###OIII
'''
fig = plt.figure()
plt.scatter(l2blue['col1'],l2blue['col2'],color='blue')
plt.scatter(l2red['col1'],l2red['col2'],color='red')
plt.scatter(l2purple['col1'],l2purple['col2'],color='purple')
plt.scatter(l2cyan['col1'],l2cyan['col2'],color='cyan')
plt.scatter(l2green['col1'],l2green['col2'],color='limegreen')
#plt.ylim(-1,1)
plt.title("OIII Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
#fig.savefig('OIIIa.png')
plt.show()
'''
fig = plt.figure()
plt.plot(l2blue['col1'],l2blue['col2'],color='blue')
plt.plot(l2red['col1'],l2red['col2'],color='red')
plt.plot(l2purple['col1'],l2purple['col2'],color='purple',)
plt.plot(l2cyan['col1'],l2cyan['col2'],color='cyan')
plt.plot(l2green['col1'],l2green['col2'],color='limegreen')
#plt.ylim(-1,1)
plt.title("OIII Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
fig.savefig('OIIIb.png')
plt.show()

fig = plt.figure()
plt.plot(l2blue['col1'],l2blue['col2'],color='blue')
plt.plot(l2green['col1'],l2green['col2'],color='limegreen')
#plt.ylim(-1,1)
plt.title("OIII Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
fig.savefig('OIIIc.png')
plt.show()


fig = plt.figure()
#plt.plot(l2blue['col1'],l2blue['col2'],color='blue')
#plt.plot(l2red['col1'],l2red['col2'],color='red')
plt.plot(l2purple['col1'],l2purple['col2'],color='purple',)
plt.plot(l2cyan['col1'],l2cyan['col2'],color='cyan')
#plt.plot(l2green['col1'],l2green['col2'],color='limegreen')
#plt.ylim(-1,1)
plt.title("OIII Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
fig.savefig('OIIId.png')
plt.show()
###SII
'''
fig = plt.figure()
plt.scatter(l3blue['col1'],l3blue['col2'],color='blue')
plt.scatter(l3red['col1'],l3red['col2'],color='red')
plt.scatter(l3purple['col1'],l3purple['col2'],color='purple')
plt.scatter(l3cyan['col1'],l3cyan['col2'],color='cyan')
plt.scatter(l3green['col1'],l3green['col2'],color='limegreen')
#plt.ylim(-1,1)
plt.title("SII Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
#fig.savefig('SIIa.png')
plt.show()
'''
fig = plt.figure()
plt.plot(l3blue['col1'],l3blue['col2'],color='blue')
plt.plot(l3red['col1'],l3red['col2'],color='red')
plt.plot(l3purple['col1'],l3purple['col2'],color='purple')
plt.plot(l3cyan['col1'],l3cyan['col2'],color='cyan')
plt.plot(l3green['col1'],l3green['col2'],color='limegreen')
#plt.ylim(-1,1)
plt.title("SII Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
fig.savefig('SIIb.png')
plt.show()

fig = plt.figure()
plt.plot(l3purple['col1'],l3purple['col2'],color='purple')
plt.plot(l3cyan['col1'],l3cyan['col2'],color='cyan')
#plt.ylim(-1,1)
plt.title("SII Distribution: Brightness vs Position of Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
fig.savefig('SIIc.png')
plt.show()


###Blue line
fig = plt.figure()
plt.plot(l1blue['col1'],l1blue['col2'],color='orangered',label="H alpha")
plt.plot(l2blue['col1'],l2blue['col2'],color='lawngreen',label="OIII")
plt.plot(l3blue['col1'],l3blue['col2'],color='dodgerblue',label="SII")
#plt.ylim(-1,1)
plt.title("Three Emission line comparison: Brightness vs Position of Blue Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
plt.legend()
fig.savefig('bluea.png')
plt.show()

###Cyan line
fig = plt.figure()
plt.plot(l1cyan['col1'],l1cyan['col2'],color='orangered',label="H alpha")
plt.plot(l2cyan['col1'],l2cyan['col2'],color='lawngreen',label="OIII")
plt.plot(l3cyan['col1'],l3cyan['col2'],color='dodgerblue',label="SII")
#plt.ylim(-1,1)
plt.title("Three Emission line comparison: Brightness vs Position of Cyan Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
plt.legend()
fig.savefig('cyana.png')
plt.show()

###Purple line
fig = plt.figure()
plt.plot(l1purple['col1'],l1purple['col2'],color='orangered',label="H alpha")
plt.plot(l2purple['col1'],l2purple['col2'],color='lawngreen',label="OIII")
plt.plot(l3purple['col1'],l3purple['col2'],color='dodgerblue',label="SII")
#plt.ylim(-1,1)
plt.title("Three Emission line comparison: Brightness vs Position of Purple Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
plt.legend()
fig.savefig('purplea.png')
plt.show()

###Red line
fig = plt.figure()
plt.plot(l1red['col1'],l1red['col2'],color='orangered',label="H alpha")
plt.plot(l2red['col1'],l2red['col2'],color='lawngreen',label="OIII")
plt.plot(l3red['col1'],l3red['col2'],color='dodgerblue',label="SII")
#plt.ylim(-1,1)
plt.title("Three Emission line comparison: Brightness vs Position of Red Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
plt.legend()
fig.savefig('reda.png')
plt.show()

###Green line
fig = plt.figure()
plt.plot(l1green['col1'],l1green['col2'],color='orangered',label="H alpha")
plt.plot(l2green['col1'],l2green['col2'],color='lawngreen',label="OIII")
plt.plot(l3green['col1'],l3green['col2'],color='dodgerblue',label="SII")
#plt.ylim(-1,1)
plt.title("Three Emission line comparison: Brightness vs Position of Green Line" )
plt.ylabel("Brightness")
plt.xlabel('Position of Line')
plt.grid()
plt.legend()
fig.savefig('greena.png')
plt.show()












def angsep(ra1,ra2,dec1,dec2):
    return arccos(cos(dec2) * cos(dec1) * cos(ra2 - ra1) + sin(dec1) * sin(dec2))

rightasc1 = 4.676389
rightasc2 = 4.677778
decel1 = 50.463056
decel2 = 50.431667

rightas1err = 0.001667
rightas2err = 0.000556
decel1err = 0.033333
decel2err =0.004167

rightasc1up = rightasc1 + rightas1err
rightasc1lo = rightasc1 - rightas1err

rightasc2up = rightasc2 + rightas2err
rightasc2lo = rightasc2 - rightas2err

decel1up = decel1 + decel1err
decel1lo = decel1 - decel1err

decel2up = decel2 + decel2err
decel2lo = decel2 - decel2err

distance = angsep(rightasc1,rightasc2,decel1,decel2)

distanceup= angsep(rightasc1up,rightasc2up,decel1up,decel2up)
distancelo= angsep(rightasc1lo,rightasc2lo,decel1up,decel2lo)


distanceerr = (distanceup - distancelo) / 2.0

print distance,abs(distanceerr)
print distance *3600,abs(distanceerr) * 3600
