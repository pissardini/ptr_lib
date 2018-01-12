import math 

def diff_simple(ai,af):
    return math.sqrt(pow(af-ai,2))

def cartesian_distance(xi,yi,zi,xf,yf,zf):
    return math.sqrt(pow(xf-xi,2)+pow(yf-yi,2)+ pow(zf-zi,2))
