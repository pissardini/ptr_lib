# -*- coding: cp1252 -*-

#
# Copyright (c) 2014-2020 R.Pissardini <rodrigo AT pissardini DOT com>
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
from ptr_lib.constants import RADIUS_EARTH
import datetime

#Computation of distance
 
def cartesian_distance (x,
                        y,
                        xf,
                        yf):
    ''' Cartesian distance between two points

        Keyword arguments:
	        x, y     -- x,y of first position
                xf, xy   -- x,y of second position
        Output:        
	        distance -- in units

    '''
    distance = pow(pow(xf-x,2)+pow(yf-y,2),0.5)
    return distance

def spheric_cosines(lat1,lon1,lat2,lon2,earth_radius=RADIUS_EARTH):
    delta_lat = lat2 - lat1;
    delta_lon = lon2 - lon1;
    distance = acos(sin(radians(lat1))\
         * sin(radians(lat2)) +cos(radians(lat1))*\
          cos(radians(lat2)) * cos(radians(delta_lon)))* earth_radius
    return distance

def harvesine (lat1,
               lon1,
               lat2,
               lon2,
               earth_radius=RADIUS_EARTH):
    ''' Harvesine - return distance between two points in meters

        Keyword arguments:
	        lat1, lon1   -- lat,lon of first position
                lat2, lon2   -- lat,lon of second position
                earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        distance   -- distance in meters

    '''

    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    
    alpha = delta_lat * 0.5
    beta = delta_lon * 0.5
    
    a = pow(sin(alpha),2) + pow(sin(beta),2)* cos(lat1)* cos(lat2)
    c = 2 * atan2((a)*0.5, (1-a)*0.5)
    distance = earth_radius * c
    
    return distance

def equirec_approximation (lat1, lon1, lat2,lon2, earth_radius=RADIUS_EARTH): # Equirectangular approximation
    x = (lon2-lon1) * cos(lat1+lat2)/2
    y = lat2 - lat1
    d = pow(x * x + y * y, 0.5) * earth_radius
    return d


def great_circle_vec(lat1, lon1, lat2, lon2, earth_radius=RADIUS_EARTH):
    
    d_phi =radians(lat2) - radians(lat1)
    d_theta = radians(log2) - radians(log1)

    h = np.sin(d_phi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(d_theta / 2) ** 2
    h = np.minimum(1.0, h)  # protect against floating point errors

    arc = 2 * np.arcsin(np.sqrt(h))

    # return distance in units of earth_radius
    distance = arc * earth_radius
    return distance

