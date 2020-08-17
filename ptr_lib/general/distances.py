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
from ptr_lib.general.constants import RADIUS_EARTH
import datetime


def cartesian_distance (lat1,
                        lon1,
                        lat2,
                        lon2,
                        earth_radius=RADIUS_EARTH):
    
    """ Cartesian distance between two coordinates
        Keyword arguments:
                lat1, lon1   -- lat,lon of first position
                lat2, lon2   -- lat,lon of second position
                earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        distance -- in meters
    """
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    
    return sqrt(pow(lat2-lat1,2)+ pow(lon2-lon1,2))* earth_radius

def cartesian_xy(x1,
                 y1,
                 x2,
                 y2):
    """ Cartesian distance between two points

        Keyword arguments:
	        x1, y1     -- x,y of first position
                x2, y2     -- x,y of second position
        Output:        
	        distance -- in units
    """
    return sqrt(pow(x2-x1,2)+ pow(y2-y1,2))

def spherical_cosines(lat1,
                      lon1,
                      lat2,
                      lon2,
                      earth_radius=RADIUS_EARTH):
    
    """ Spherical Cosines - return distance between two points in meters

        Keyword arguments:
	        lat1, lon1   -- lat,lon of first position
                lat2, lon2   -- lat,lon of second position
                earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        distance   -- distance in meters

    """
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    
    return acos(sin(lat1)* sin(lat2) + cos(lat1)* cos(lat2) * cos(lon2 - lon1)) * earth_radius

def haversine (lat1,
               lon1,
               lat2,
               lon2,
               earth_radius=RADIUS_EARTH):
    
    """ Harvesine - return distance between two points in meters

        Keyword arguments:
	        lat1, lon1   -- lat,lon of first position
                lat2, lon2   -- lat,lon of second position
                earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        distance   -- distance in meters

    """

    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    
    a = pow(sin(delta_lat/2),2) + cos(lat1) * cos(lat2) * pow(sin(delta_lon/2),2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
                  
    return earth_radius * c

def equirec_approximation (lat1,
                           lon1,
                           lat2,
                           lon2,
                           earth_radius=RADIUS_EARTH):
    
    """ Equirectangular approximation - return distance between two points in meters
        using Pythagorean theorem. In this case, accuracy is less important.

        Keyword arguments:
	        lat1, lon1   -- lat,lon of first position
                lat2, lon2   -- lat,lon of second position
                earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        distance   -- distance in meters

    """
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    
    x = (lon2 - lon1) * cos((lat1 + lat2)/2)
    y = lat2 - lat1

    return sqrt(x * x + y * y) * earth_radius
