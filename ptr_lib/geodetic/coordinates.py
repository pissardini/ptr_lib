# -*- coding: cp1252 -*-

#
# Copyright (c) 2014-2018 R.Pissardini <rodrigo AT pissardini DOT com>
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
        '''Convert from LLH to ECEF
        '''
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
    e2 = (pow(a,2) - pow(b,2))/pow(a,2)
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

def corregoalegre2sirgas(x,y,z): #Córrego Alegre to SIRGAS 2000
    xf = x - 206.048
    yf = y + 168.279
    zf = z - 3.283
    return [xf,yf,zf]

def sirgas2corregoalegre(x,y,z): #SIRGAS 2000 to Córrego Alegre
    xf = x + 206.048
    yf = y - 168.279
    zf = z + 3.283
    return [xf,yf,zf]
