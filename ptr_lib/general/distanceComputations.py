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

#Computation of distance

def diff_simple(ai,af):
    return pow(pow(af-ai,2), 0.5)
 
def cartesian_distance (x, y, xf,yf): 
	distance = pow(pow(xf-x,2)+pow(yf-y,2),0.5)
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
	d = pow(x * x + y * y, 0.5) * earth_radius
	return d
