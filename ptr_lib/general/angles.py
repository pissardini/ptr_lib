# -*- coding: cp1252 -*-

#
# Copyright (c) 2012-2021 R.Pissardini <rodrigo AT pissardini DOT com>
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

from math import acos, asin, atan2, cos, degrees, pi, radians, sin, sqrt

def angle_xy (a,
              b):
    """return angle between two points.
        Keyword arguments:
	        a  -- (x,y)   x,y of first position
            b  -- (x,y)   x,y of second position
        Output:        
	        angle -- in radians
    """
    xi = a[0]
    yi = a[1]
    xf = b[0]
    yf = b[1]

    angle = atan2(yf - yi, xf - xi)
    return angle

def bearing (a,b):
    """return bearing between two points in radians. This formula is
       for the initial bearing.
        Keyword arguments:
	        a  -- (lat1, lon1)   lat,lon of first position
            b  -- (lat2, lon2)   lat,lon of second position
        Output:        
	        bearing - in radians
        """
    lat1 = radians(a[0])
    lon1 = radians(a[1])
    lat2 = radians(b[0])
    lon2 = radians(b[1])

    y = sin(lon2-lon1) * cos(lat2)
    x = cos(lat1) * sin(lat2) -\
        sin(lat1) * cos(lat2) *\
        cos(lon2-lon1)
    b = atan2(y,x)
    
    return b


def bearing2azimuth(value):
    """convert bearing value to azimuth .
    """
    if value <0:
        value = (180 + value) + 180
    return value

def arcsecs2radians (seconds):
    """convert arcseconds to radians.
    """
    radians = seconds * 0.000004848
    return radians

def radians2arcsecs (radians):
    """convert radians to arcseconds.
    """
    seconds = radians * 206264.806247096
    return seconds

def dms2decimal (degrees, minutes, seconds, direction='S'):
    """Convert degree-minute-second to degree in decimal format.
    """    
    if direction in ['S','W']:
        signal = -1
    elif direction in ['N','E']:
        signal = 1
    else:
        print('[Error] Insert a correct direction [ N, S, W or E]\n')
        return
    
    decimal = signal * (int(degrees) + float(minutes) / 60 + float(seconds) / 3600)
    
    return decimal
    
def decimal2dms (decimal, direction = 'N'):
    """Convert degree in decimal formar to degree in degree-minute-second format.
    """
    degrees = int(decimal)
    minutes = int (abs((decimal - int(decimal)) * 60))
    seconds = abs((abs((decimal - int(decimal)) * 60)-minutes)*60)
                  
    if direction =='N':
        if decimal <0 :
            direction ='S'
    elif direction =='E':
        if decimal <0:
            direction ='W'
    else:
        print('[Error] Insert a correct direction [N or E]\n')
        return
    return (degrees,minutes,seconds,direction)

def degrees2radians(value):
    """Convert degrees to radians.
    """
    return radians(value)

def radians2degrees(value):
    """Convert radians to degrees.
    """
    return degrees(value)

def degrees2gradians(value):
    """Convert degrees to gradians.
    """
    return value * 200/180

def gradians2degrees(value):
    """Convert gradians to degree.
    """
    return value * 180/200


def radians2gradians(value):
    """Convert radians to gradians.
    """
    return value * 200/pi


def gradians2radians(value):
    """Convert gradians to radians.
    """
    return value * pi/200
