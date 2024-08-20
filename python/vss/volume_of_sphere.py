#find the volume of the sphere
import math
r=int(input('enter the radius of the sphere'))
v=4/3*math.pi*r*r*r
#if you want to print only 3 values after the point in case of format method then we use {:.3f}
print("volume of the sphere of the radius {} is : {:.3f}".format(r,v))
print("volume of the sphere of the radius %d is : %0.3f"%(r,v))