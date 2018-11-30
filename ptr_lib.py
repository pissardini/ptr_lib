#
# Copyright (c) 2014 R.Pissardini <rodrigo AT pissardini DOT com> 
# Copyright (c) 2018 R.Pissardini <rodrigo AT pissardini DOT com> and Alex Boava Meza 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from math import *
import datetime

#Computation of distance

def diff_simple(ai,af):
    return sqrt(pow(af-ai,2))
 
def cartesian_distance (x, y, xf,yf): 
	distance =  sqrt(((xf-x)**2)+ ((yf-y)**2))
	return distance

def spheric_cosines(lat1,lon1,lat2,lon2,earth_radius):
	delta_lat = lat2 - lat1;
	delta_lon = lon2 - lon1;
	distance = acos(sin(radians(lat1))\
		 * sin(radians(lat2)) +cos(radians(lat1))*\
		  cos(radians(lat2)) * cos(radians(delta_lon)))* earth_radius
	return distance

def harvesine (lat1, lon1, lat2,lon2, earth_radius):
	delta_lat = lat2 - lat1
	delta_lon = lon2 - lon1
	alpha = delta_lat * 0.5;
	beta = delta_lon * 0.5;
	a = sin(radians(alpha))* sin(radians(alpha))+\
		   cos(radians(lat1))*cos(radians(lat2)) *\
		   sin(radians(beta)) * sin(radians(beta));
	c = 2 * atan2((a)*0.5, (1-a)*0.5)	
	distance = earth_radius * c
	return distance
	
def equirec_approximation (lat1, lon1, lat2,lon2, earth_radius): # Equirectangular approximation
	x = (lon2-lon1) * cos(lat1+lat2)/2
	y = lat2 - lat1
	d = sqrt(x * x + y * y) * earth_radius
	return d
  
#Computation of angles

def angle_between_coordinates (xi, yi, xf, yf):
        angle = atan2(yf -yi, xf -xi)
        return angle

def bearing (lat1,lon1,lat2,lon2):
    y = sin(lon2-lon1) * cos(lat2)
    x = cos(lat1)*sin(lat2)-\
        sin(lat1)*cos(lat2)*\
        cos(lon2-lon1)
    b = atan2(y,x) #radians
    return b
    
#Computation of new coordinates

def polar_coordinates (x, y, distance, angle): #angle in degrees
        xf = (distance * cos(radians(angle))) + x
        yf = (distance * sin(radians(angle))) + y
        return [xf,yf]

##Lenght of latitude and longitude 

def lenght_latitude_longitude(value): #value in degrees (0.0)
	lat = radians(value)
	m1 = 111132.92
	m2 = -559.82
	m3 = 1.175
	m4 = -0.0023
	p1 = 111412.84
	p2 = -93.5
	p3 = 0.118
	latlen = m1 + (m2 * cos(2 * lat)) + (m3 * cos(4 * lat)) +\
			(m4 * cos(6 * lat))
	longlen = (p1 * cos(lat)) + (p2 * cos(3 * lat)) +\
			(p3 * cos(5 * lat))
	return [latlen,longlen]

#Computation of date and time 

def day_of_year(year,month,day):
	doy = datetime.datetime(year, month, day).timetuple().tm_yday
	return doy

def julian_date(year,month,day,hour,minute,second): 
        MJD0 = 2400000.5
        b = 0
        
        if (month <= 2):
                month +=12
                year -= 1

        if ((10000*year+100*month+day) <= 15821004):
                b = -2 + get_intpart (year+4716) - 1179
                
        else:
                b = get_intpart(year* 0.0025)- get_intpart(year* 0.01)+\
                    get_intpart(year *0.25)

        mjdmidnight = 365 *year - 679004 + b + (30.6001*(month+1)) + day
        fracofday = ((hour+ (minute/60)+ (second/3600)))/24
        return MJD0 + mjdmidnight + fracofday

#Transformations

##Transformations between quaternions and Euler's angles

def quat2euler(qw,qx,qy,qz):
    
    qw2 = qw * qw
    qx2 = qx * qx
    qy2 = qy * qy
    qz2 = qz * qz
    test= qx * qy + qz * qw

    Y = 0.0
    Z = 0.0
    X = 0.0

    if (test > 0.499):
        Y = 360/pi * atan2(qx,qw)
        Z = 90
        X = 0
        return [X,Y,Z]

    if (test < -0.499):
        Y = -360/pi*atan2(qx,qw)
        Z = -90
        X = 0
        return [X,Y,Z]

    h     = atan2(2 * qy * qw - 2 * qx * qz, 1 - 2 * qy * qy - 2 * qz * qz)
    a     = asin (2 * qx * qy + 2 * qz * qw)
    b     = atan2(2 * qx * qw - 2 * qy * qz, 1 - 2 * qx * qx - 2 * qz * qz)
    Y = h * 180/pi
    Z = a * 180/pi
    X = b * 180/pi

    return [X, Y, Z]


def euler2quat(X,Y,Z):
    
    h  = Y * pi/360
    a  = Z * pi/360
    b  = X * pi/360
    c1 = cos(h)
    c2 = cos(a)
    c3 = cos(b)
    s1 = sin(h)
    s2 = sin(a)
    s3 = sin(b)
    qw = ((c1 * c2 * c3 - s1 * s2 * s3)* 100000)/100000
    qx = ((s1 * s2 * c3 + c1 * c2 * s3)* 100000)/100000
    qy = ((s1 * c2 * c3 + c1 * s2 * s3)* 100000)/100000
    qz = ((c1 * s2 * c3 - s1 * c2 * s3)* 100000)/100000
    return [qw, qx, qy, qz]

##rotation of coordinates 

def rotation_coordinates(x, y, angle): #angle in degrees
	xf = x * cos(radians(angle))+ y * sin(radians(angle))
	yf = -x * sin(radians(angle))+ y * cos(radians(angle));
	return [xf,yf]
  
#Transformations between reference systems

def geodetic2cartesian(lat,lon,h, a =6378137, b=6356752.314140347): #SIRGAS
	e2 = (pow(a,2) -pow(b,2))/pow(a,2)
	N = a/(pow(1. -e2 * pow(sin(radians(lat)),2), 0.5))
	X = (N+h) * cos(radians(lat)) * cos(radians(lon))
	Y = (N+h) * cos(radians(lat)) * sin(radians(lon))
	Z = ((1.-e2) * N + h) * sin(radians(lat))
	return [X,Y,Z]
 
def cartesian2geodetic (X, Y, Z, a = 6378137,b = 6356752.314140347): #SIRGAS
        H = 0
        v = 0
        e2 = (pow(a,2) -pow(b,2))/pow(a,2)
        p = pow(pow(X,2)+pow(Y,2),0.5)
        lat = atan2(Z, p*(1-e2))
        lat1 = 2 * pi
        
        while fabs(lat1-lat) > 1e-15:
                v = a/pow((1- e2* pow(sin(lat),2)),0.5)
                H = p/cos(lat)- v
                lat1 = lat
                lat = atan2(Z + e2 * v * sin(lat),p)
        
        lat = degrees(lat) #in degrees
        lon = degrees(atan2(radians(Y), radians(X))) #in degrees
        return [lat,lon,H]


def geodetic2enu (lat, lon, h, a = 6378137, b = 6356752.314140347):
    """ Convert from geodetic to a different ENU local coordinate system.
    East  -- is the longitude multiplied by the radius of the small circle at that latitude
    North -- is the product of the  geodetic latitue by the semi-major axis of the ellipsoid
    Up    -- is the geodetic height
    
    Keyword arguments:
    lat -- latitude in degrees
    lon -- longitude in degrees
    h   -- geodetic height in meters
    a   -- semi-major axis (default SIRGAS)
    b   -- semi-minor axis (default SIRGAS)
    
    """
    	e2 = (pow(a,2) -pow(b,2))/pow(a,2)
    	lat = radians(lat)
    	v = a/pow((1- e2* pow(sin(lat),2)),0.5)
    	small_circle = v * cos(lat)
    	if (lon < 0):
        	lon+=360
    	E = radians(lon) * small_circle
   	N = lat * a
    	U = h
    	return [E, N, U]
    


def helmert_transformation (X,Y,Z,tx,ty,tz,s,rx,ry,rz,a= 6378137,b=6356752.314140347):

	xp = tx + ((1 + s) * X) - (rz * Y) + (ry * Z)
	yp = ty + (rz * X) + ((1 + s) * Y) - (rx * Z)
	zp = tz - (ry * X) + (rx * Y) + ((1 + s) * Z)
	
	return [xp,yp,zp]

def sad2sirgas(x,y,z): #SAD 69 to SIRGAS 2000
        xf = x - 67.35
        yf = y + 3.88
        zf = z - 38.22
        return [xf,yf,zf]

def sirgas2sad(x,y,z): #SIRGAS 2000 to SAD69
        xf = x + 67.35
        yf = y - 3.88
        zf = z + 38.22
        return [xf,yf,zf]

def corregoalegre2sirgas(x,y,z): #CÃ³rrego Alegre to SIRGAS 2000
        xf = x - 206.048
        yf = y + 168.279
        zf = z - 3.283
        return [xf,yf,zf]

def sirgas2corregoalegre(x,y,z): #SIRGAS 2000 to CÃ³rrego Alegre
        xf = x + 206.048
        yf = y - 168.279
        zf = z + 3.283
        return [xf,yf,zf]

#Conversions 

def arcsec2radians (seconds):
    radians = seconds * 0.000004848
    return radians

def radians2arcsec (radians):
    seconds = radians * 206264.806247096
    return seconds

def dms2decimal (degrees, minutes, seconds, direction): #direction - N- S- W- E
    if (direction=='S' or direction=='E'):
        signal = -1
    elif (direction=='N' or direction=='S'):
        signal = 1
    else:
        print('[Error] Insert a correct direction [ N, S, W or E]\n')
        return
    
    decimal = signal * (int(degrees) + float(minutes) / 60 + float(seconds) / 3600)
    
    return decimal
    
def decimal2dms (decimal, direction): #N- E
    degrees = int(decimal)
    minutes = int (abs((decimal - int(decimal)) * 60))
    seconds = abs((abs((decimal - int(decimal)) * 60)-minutes)*60)
                  
    if (direction=='N'):
        if (decimal <0):
            direction ='S'
    elif (direction =='E'):
        if (decimal <0):
            direction ='W'
    else:
        print('[Error] Insert a correct direction [N or E]\n')
        return
    return [degrees,minutes,seconds,direction]

#skyplot and other charts 

import matplotlib.pyplot as plt

def skyplot (prn,e,az): #input lists of prn (or svid), elevation and azimuths 

	ax = plt.subplot(111, projection='polar')
	ax.set_theta_zero_location("N")
	ax.set_theta_direction(-1)
	ax.set_ylim(0,90)
	ax.set_yticks(np.arange(0,91,30))
	ax.set_yticklabels(ax.get_yticks()[::-1])

	for sv, elev, azim in zip(prn, e, az):
	    ax.plot(math.radians(azim), 90-elev,color='green', marker='o', markersize=20)
	    ax.text(math.radians(azim), 90-elev, sv, ha='center', va='center',color='white')

	plt.show()

#General functions 

def get_intpart (value): 
	ipart = modf(value)
	return ipart[1]

def get_fracpart (value):
	fpart = modf(value)
	return fpart[0]

