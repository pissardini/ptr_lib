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

from math import acos, asin, atan2, cos, degrees, radians, sin, sqrt
from ptr_lib.general.constants import RADIUS_EARTH
import datetime


def cartesian_distance (a,b,
                        earth_radius=RADIUS_EARTH):
    
    """ Cartesian distance between two coordinates
        Keyword arguments:
	        a  -- (lat1, lon1)   lat,lon of first position
            b  -- (lat2, lon2)   lat,lon of second position
            earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        distance -- in meters
    """
    lat1 = radians(a[0])
    lon1 = radians(a[1])
    lat2 = radians(b[0])
    lon2 = radians(b[1])

    return sqrt(pow(lat2-lat1,2)+ pow(lon2-lon1,2))* earth_radius

def cartesian_xy(a,
                 b):
    """ Cartesian distance between two points

        Keyword arguments:
	        a           -- (x,y) of first position
            b           -- (x,y) of second position
        Output:        
	        distance -- in units
    """
    return sqrt(pow(b[0]-a[0],2)+ pow(b[1]-a[1],2))

def spherical_cosines(a,b,
                      earth_radius=RADIUS_EARTH):
    
    """ Spherical Cosines - return distance between two points in meters

        Keyword arguments:
	        a  -- (lat1, lon1)   lat,lon of first position
            b  -- (lat2, lon2)   lat,lon of second position
            earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        distance   -- distance in meters

    """
    lat1 = radians(a[0])
    lon1 = radians(a[1])
    lat2 = radians(b[0])
    lon2 = radians(b[1])

    return acos(sin(lat1)* sin(lat2) + cos(lat1)* cos(lat2) * cos(lon2 - lon1)) * earth_radius

def haversine (a,b,
               earth_radius=RADIUS_EARTH):
    
    """ Harvesine - return distance between two points in meters

        Keyword arguments:
	        a  -- (lat1, lon1)   lat,lon of first position
            b  -- (lat2, lon2)   lat,lon of second position
            earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        distance   -- distance in meters

    """

    lat1 = radians(a[0])
    lon1 = radians(a[1])
    lat2 = radians(b[0])
    lon2 = radians(b[1])
    
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    
    a = pow(sin(delta_lat/2),2) + cos(lat1) * cos(lat2) * pow(sin(delta_lon/2),2)
    c = 2 * atan2(sqrt(a), sqrt(1-a))
                  
    return earth_radius * c

def equirec_approximation (a,b,
                           earth_radius=RADIUS_EARTH):
    
    """ Equirectangular approximation - return distance between two points in meters
        using Pythagorean theorem. In this case, accuracy is less important.

        Keyword arguments:
	        a  -- (lat1, lon1)   lat,lon of first position
            b  -- (lat2, lon2)   lat,lon of second position
            earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        distance   -- distance in meters

    """
    lat1 = radians(a[0])
    lon1 = radians(a[1])
    lat2 = radians(b[0])
    lon2 = radians(b[1])
    
    x = (lon2 - lon1) * cos((lat1 + lat2)/2)
    y = lat2 - lat1

    return sqrt(x * x + y * y) * earth_radius


def destination_point(coordinate,
                      bearing,
                      distance,
                      earth_radius=RADIUS_EARTH):

    """ Calculate a new coordinate from a initial coordinate, bearing and distance
        Keyword arguments:
	            coordinate   -- (lat,lon) of first position
                bearing      -- bearing in radians
                distance     -- distance in meters
                earth_radius -- Earth's radius (default:6378137.0)
        Output:        
	        (lat,lon)    -- new coordinate (lat,lon) of first position

    """
    
    d   = distance/earth_radius
    
    lat1 = radians(coordinate[0])
    lon1 = radians(coordinate[1])
    
    lat = asin(sin(lat1) * cos(d) + cos(lat1) * sin(d) * cos(bearing))

    lon = lon1 + atan2(sin(bearing)* sin(d) * cos(lat1),cos(d)- sin(lat1)* sin(lat))

    lat= degrees(lat)
    lon= degrees(lon)
    
    return (lat,lon)

def midpoint(a,b):

    """
    Calculate the half-way point along a great circle path between two coordinates.
        Keyword arguments:
	        a        -- (lat,lon) of first position
	        b        -- (lat,lon) of second position
        Output:        
	        (lat,lon)    -- midpoint (lat,lon)

    """
    lat1 = radians(a[0])
    lon1 = radians(a[1])
    lat2 = radians(b[0])
    lon2 = radians(b[1])

    bx = cos(lat2) * cos(lon2-lon1)
    by = cos(lat2) * sin(lon2-lon1)

    lat = atan2(sin(lat1)+sin(lat2),\
                  sqrt(((cos(lat1)+ bx)**2)+ by**2))
    lon = lon1 + atan2(by, cos(lat1)+ bx)
    lat= degrees(lat)
    lon= degrees(lon)
    return (lat, lon)