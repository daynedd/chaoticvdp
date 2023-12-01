from pylab import *

theta = arange(0.0, 2*pi, 0.01)

# choose a few values of the eccentricity
#   see http://en.wikipedia.org/wiki/Orbital_eccentricity

ec0 = 0.0       # circle for comparison 
ec1 = 0.0167    # the eccentricity of the Earth's orbit: close to zero
ec2 = 0.248     # 0.248    Pluto is 0.248 biggest in solar system 

r0= 1/(1-ec0*cos(theta))  # the general equation for a conic
r1= 1/(1-ec1*cos(theta))  # these are cooked so they all have the same
r2= 1/(1-ec2*cos(theta))  # semi latus rectum = 1

# sort out the points that exceed rlimit

rlimit = 4.0

r0p = []            # arrays for plots
r1p = []
r2p = []

r0pp = []           
r1pp = []
r2pp = []

theta0p = []
theta1p = []
theta2p = []

for ii in range(0,len(theta)):
    if r0[ii] < rlimit and r0[ii] > 0.0:
        r0p.append(r0[ii])
        r0pp.append((1+ec0)*r0[ii])         # rescale so they have the same periapsis
        theta0p.append(theta[ii])           # for the second plot
    if r1[ii] < rlimit and r1[ii] > 0.0:
        r1p.append(r1[ii])
        r1pp.append((1+ec1)*r1[ii])
        theta1p.append(theta[ii])
    if r2[ii] < rlimit and r2[ii] > 0.0:
        r2p.append(r2[ii])
        r2pp.append((1+ec2)*r2[ii])
        theta2p.append(theta[ii])
    
        
fig1 = figure(1)
ax1 = fig1.add_subplot(111,projection='polar')
ax1.plot([0],[0],'r.')
ax1.plot(theta0p,r0p, theta1p,r1p, theta2p,r2p)
grid('off')
ax1.spines['polar'].set_visible(False)
ax1.set_xticks([])
ax1.set_yticks([])
title("Orbits with same latus rectum for different planets")
legend(('sun',"circle="+str(ec0),"earth="+str(ec1),"pluto="+str(ec2)),loc="lower left", bbox_to_anchor=(-0.2, 0.0))

fig2 = figure(2)
ax2 = fig2.add_subplot(111,projection='polar')
ax2.plot([0],[0],'r.')
ax2.plot(theta0p,r0pp, theta1p,r1pp, theta2p,r2pp)
grid('off')
ax2.spines['polar'].set_visible(False)
ax2.set_xticks([])
ax2.set_yticks([])
title("Orbits with same periapsis for different planets")
legend(('sun',"circle="+str(ec0),"earth="+str(ec1),"pluto="+str(ec2)),loc="lower left",bbox_to_anchor=(-0.2, 0.0))

show()
