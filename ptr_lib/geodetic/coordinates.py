# -*- coding: cp1252 -*-

#
# Copyright (c) 2012-2020 R.Pissardini <rodrigo AT pissardini DOT com>
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


def polar_coordinates (x, y, distance, angle):
    '''
        Calculate polar coordinates from xy, distance and angle (degrees)
    '''
    xf = (distance * cos(radians(angle))) + x
    yf = (distance * sin(radians(angle))) + y
    return (xf,yf)

def lenght_latitude_longitude(value):
    '''
        Lenght of latitude and longitude (degrees)
    '''
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

    return (latlen,longlen)

def quat2euler(qw,qx,qy,qz):
    '''
        Convert quaternions to Euler's angles
    '''
    qw2 = qw * qw
    qx2 = qx * qx
    qy2 = qy * qy
    qz2 = qz * qz
    test= qx * qy + qz * qw

    y = 0.0
    z = 0.0
    x = 0.0

    if (test > 0.499):
        y = 360/pi * atan2(qx,qw)
        z = 90
        x = 0
        return [X,Y,Z]

    if (test < -0.499):
        y = -360/pi*atan2(qx,qw)
        z = -90
        x = 0
        return (X,Y,Z)

    h     = atan2(2 * qy * qw - 2 * qx * qz, 1 - 2 * qy * qy - 2 * qz * qz)
    a     = asin (2 * qx * qy + 2 * qz * qw)
    b     = atan2(2 * qx * qw - 2 * qy * qz, 1 - 2 * qx * qx - 2 * qz * qz)
    y = h * 180/pi
    z = a * 180/pi
    x = b * 180/pi

    return (x, y, z)


def euler2quat(x,y,z):
    '''
        Convert Euler's angles to quaternions
    '''
    h  = y * pi/360
    a  = z * pi/360
    b  = x * pi/360
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
    return (qw, qx, qy, qz)

def rotation_coordinates(x, y, angle):
    '''
        Rotation of coordinates
    '''
    xf =  x * cos(radians(angle))+ y * sin(radians(angle))
    yf = -x * sin(radians(angle))+ y * cos(radians(angle))
    return (xf,yf)  

def geodetic2cartesian(lat,
                       lon,
                       h,
                       a = 6378137,
                       b= 6356752.314140347):
    '''
        Convert from LLH to ECEF
    '''
    e2 = (pow(a,2) -pow(b,2))/pow(a,2)
    n  = a/(pow(1. -e2 * pow(sin(radians(lat)),2), 0.5))
    x  = (n+h) * cos(radians(lat)) * cos(radians(lon))
    y  = (n+h) * cos(radians(lat)) * sin(radians(lon))
    z  = ((1.-e2) * n + h) * sin(radians(lat))
    return (x,y,z)
 
def cartesian2geodetic (x,
                        y,
                        z,
                        a = 6378137,
                        b = 6356752.314140347):
    '''
        Convert from ECEF to LLH
    '''
    h    = 0.0
    v    = 0.0
    e2   = (pow(a,2) -pow(b,2))/pow(a,2)
    p    = pow(pow(x,2)+pow(y,2),0.5)
    lat  = atan2(z, p*(1-e2))
    lat1 = 2 * pi
        
    while fabs(lat1-lat) > 1e-15:
            v = a/pow((1- e2* pow(sin(lat),2)),0.5)
            h = p/cos(lat)- v
            lat1 = lat
            lat = atan2(z + e2 * v * sin(lat),p)
    
    lat = degrees(lat)
    lon = degrees(atan2(radians(y), radians(x)))
    return (lat,lon,h)

def geodetic2enu (lat,
                  lon,
                  h,
                  a = 6378137,
                  b = 6356752.314140347):
    '''
        Convert from LLH to ENU
    '''
    e2           = (pow(a,2) - pow(b,2))/pow(a,2)
    lat          = radians(lat)
    v            = a/pow((1- e2* pow(sin(lat),2)),0.5)
    small_circle = v * cos(lat)
    
    if (lon < 0):
            lon+= 360
            e   = radians(lon) * small_circle

    n = lat * a
    u = h
    return (e,n,u)
    

def helmert_transformation (x,
                            y,
                            z,
                            tx,
                            ty,
                            tz,
                            s,
                            rx,
                            ry,
                            rz,
                            a = 6378137,
                            b = 6356752.314140347):
    '''
        Helmert Transformation
    '''
    xp = tx + ((1 + s) * x) - (rz * y) + (ry * z)
    yp = ty + (rz * x) + ((1 + s) * y) - (rx * z)
    zp = tz - (ry * x) + (rx * y) + ((1 + s) * z)
    
    return (xp,yp,zp)

def sad2sirgas(x,y,z):
    '''
        Convert from SAD69 to SIRGAS 2000
    '''
    xf = x - 67.35
    yf = y + 3.88
    zf = z - 38.22
    return (xf,yf,zf)

def sirgas2sad(x,y,z):
    '''
        Convert from SIRGAS200 to SAD69
    '''
    xf = x + 67.35
    yf = y - 3.88
    zf = z + 38.22
    return (xf,yf,zf)

def corregoalegre2sirgas(x,y,z):
    '''
        Convert from Corrego Alegre to SIRGAS
    '''
    xf = x - 206.048
    yf = y + 168.279
    zf = z - 3.283
    return (xf,yf,zf)

def sirgas2corregoalegre(x,y,z):
    '''
        Convert from SIRGAS to Corrego Alegre
    '''
    xf = x + 206.048
    yf = y - 168.279
    zf = z + 3.283
    return (xf,yf,zf)
