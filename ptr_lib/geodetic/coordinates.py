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

# 22/01/2021  - insert llh2utm and utm2llh


from math import asin, asinh, atanh, atan, atan2, cos, cosh, degrees, fabs,\
    floor, pi, radians, sin, sinh, sqrt, tan,tanh
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

def polar_coordinates (coordinate:Tuple[float], 
                       distance:float, 
                       angle:float)->Tuple[float]:
    '''
        Calculate polar coordinates from xy, distance and angle (degrees)
    '''
    x = coordinate[0]
    y = coordinate[1]
    xf = (distance * cos(radians(angle))) + x
    yf = (distance * sin(radians(angle))) + y
    return (xf,yf)

def lenght_latitude_longitude(latitude:float)->Tuple[float]:
    '''
        Lenght of latitude and longitude (degrees)
    '''
    lat = radians(latitude)
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

    return (latlen, longlen)

def quat2euler(qw:float,
               qx:float,
               qy:float,
               qz:float)->Tuple[float]:
    '''
        Convert quaternions to Euler's angles
    '''

    test= qx * qy + qz * qw

    y = 0.0
    z = 0.0
    x = 0.0

    if (test > 0.499):
        y = 360/pi * atan2(qx,qw)
        z = 90
        x = 0
        return (x,y,z)

    if (test < -0.499):
        y = -360/pi*atan2(qx,qw)
        z = -90
        x = 0
        return (x,y,z)

    h     = atan2(2 * qy * qw - 2 * qx * qz, 1 - 2 * qy * qy - 2 * qz * qz)
    a     = asin (2 * qx * qy + 2 * qz * qw)
    b     = atan2(2 * qx * qw - 2 * qy * qz, 1 - 2 * qx * qx - 2 * qz * qz)
    y = h * 180/pi
    z = a * 180/pi
    x = b * 180/pi

    return (x, y, z)


def euler2quat(x:float,y:float,z:float)->Tuple[float]:
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

def rotation_coordinates(coordinate:Tuple[float], 
                         angle:float)-> Tuple[float]:
    '''
        Rotation of coordinates
    '''
    x = coordinate[0]
    y = coordinate[1]
    xf =  x * cos(radians(angle))+ y * sin(radians(angle))
    yf = -x * sin(radians(angle))+ y * cos(radians(angle))
    return (xf,yf)  

def geodetic2cartesian(coordinate:Tuple[float],
                       a:float = 6378137,
                       b:float = 6356752.314140347)->Tuple[float]:
    '''
        Convert from LLH to ECEF
    '''
    lat = coordinate[0]
    lon = coordinate[1]
    h   = coordinate[2]
    e2 = (a**2 - b**2)/a**2
    n  = a/sqrt(1. -e2 * sin(radians(lat))**2)
    x  = (n+h) * cos(radians(lat)) * cos(radians(lon))
    y  = (n+h) * cos(radians(lat)) * sin(radians(lon))
    z  = ((1.-e2) * n + h) * sin(radians(lat))
    return (x,y,z)
 
def cartesian2geodetic (coordinate:Tuple[float],
                       a:float = 6378137,
                       b:float = 6356752.314140347)->Tuple[float]:
    '''
        Convert from ECEF to LLH
    '''
    x = coordinate[0]
    y = coordinate[1]
    z   = coordinate[2]

    h    = 0.0
    v    = 0.0
    e2   = (a**2 - b**2)/a**2
    p    = sqrt(x**2 + y**2)
    lat  = atan2(z, p*(1-e2))
    lat1 = 2 * pi
        
    while fabs(lat1-lat) > 1e-15:
            v   = a/sqrt(1- e2* sin(lat)**2)
            h   = p/cos(lat)- v
            lat1 = lat
            lat = atan2(z + e2 * v * sin(lat),p)
    
    lat = degrees(lat)
    lon = degrees(atan2(radians(y), radians(x)))
    return (lat,lon,h)

def geodetic2enu (coordinate:Tuple[float],
                  a:float = 6378137,
                  b:float = 6356752.314140347)->Tuple[float]:
    '''
        Convert from LLH to ENU
    '''
    lat = coordinate[0]
    lon = coordinate[1]
    h   = coordinate[2]

    e2           = (a**2 - b**2)/ a**2
    lat          = radians(lat)
    v            = a/sqrt(1- e2* sin(lat)**2)
    small_circle = v * cos(lat)
    
    if (lon < 0):
            lon+= 360
            e   = radians(lon) * small_circle

    n = lat * a
    u = h
    return (e,n,u)
    

def helmert_transformation (x:float,
                            y:float,
                            z:float,
                            tx:float,
                            ty:float,
                            tz:float,
                            s:float,
                            rx:float,
                            ry:float,
                            rz:float,
                            a:float = 6378137,
                            b:float = 6356752.314140347)->Tuple[float]:
    '''
        Helmert Transformation
    '''
    xp = tx + ((1 + s) * x) - (rz * y) + (ry * z)
    yp = ty + (rz * x) + ((1 + s) * y) - (rx * z)
    zp = tz - (ry * x) + (rx * y) + ((1 + s) * z)
    
    return (xp,yp,zp)

def sad2sirgas(coordinates:Tuple[float])->Tuple[float]:
    '''
        Convert from SAD69 to SIRGAS 2000
    '''
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]

    xf = x - 67.35
    yf = y + 3.88
    zf = z - 38.22
    return (xf,yf,zf)

def sirgas2sad(coordinates:Tuple[float])->Tuple[float]:
    '''
        Convert from SIRGAS200 to SAD69
    '''
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]

    xf = x + 67.35
    yf = y - 3.88
    zf = z + 38.22
    return (xf,yf,zf)

def corregoalegre2sirgas(coordinates:Tuple[float])->Tuple[float]:
    '''
        Convert from Corrego Alegre to SIRGAS
    '''
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]

    xf = x - 206.048
    yf = y + 168.279
    zf = z - 3.283
    return (xf,yf,zf)

def sirgas2corregoalegre(coordinates:Tuple[float])->Tuple[float]:
    '''
        Convert from SIRGAS to Corrego Alegre
    '''
    x = coordinates[0]
    y = coordinates[1]
    z = coordinates[2]

    xf = x + 206.048
    yf = y - 168.279
    zf = z + 3.283
    return (xf,yf,zf)

def llh2utm(coordinates:Tuple[float],
            a:float = 6378137,
            f:float = 1/298.257223563)->Dict:
    '''
        Convert from lat, lon, h to utm
        Based on https://www.movable-type.co.uk/scripts/latlong-utm-mgrs.html
        Reference: Karney 2011 ‘Transverse Mercator with an accuracy of a few nanometers’
        
        Keyword arguments:
            coordinates  -- (lat, lon, h)
            a  -- Earth's radius (default:6378137.0)
            f  -- flattening (default:1/298.257223563)
        Output:        
	        dictionary -- {
                zone: UTM zone,
                coordinate: tuple with utm coordinate (easting, northing, hemisphere),
                convergence: meridian convergence (bearing of grid north
                            clockwise from true north), in degrees.
                scale: grid scale factor
            }

    '''
    latitude  = coordinates[0]
    longitude = coordinates[1]

    assert latitude > -90.0 and\
           latitude < 90.0 and\
           longitude > -180.0 and\
           longitude <= 180.0, 'Insert correct coordinates'

    #calculate longitude zone
    if longitude < 0.0:
        zone = floor(((180.0 + longitude) / 6) + 1)
    else:
        zone = floor((longitude / 6) + 31)
    
    #longitude of central meridian
    longitude_0           = radians((zone-1)*6 - 180 + 3)

    ## handling Norway/Svalbard exceptions

    mgrsLatBands       = 'CDEFGHJKLMNPQRSTUVWXX'
    latBand            = mgrsLatBands[floor(latitude/8+10)]
    rad_six            = radians(6)
    
    #adjusting zone and central meridian for Norway
    if zone==31 and latBand=='V' and longitude>= 3:
        zone     += 1
        longitude_0 += rad_six 
 
    #adjust zone & central meridian for Svalbard
    if zone==32 and latBand=='X' and longitude<9:
        zone     -= 1
        longitude_0 -= rad_six 

    if zone==32 and latBand=='X' and longitude>= 9:
        zone     += 1
        longitude_0 += rad_six 

    if zone==34 and latBand=='X' and longitude< 21:
        zone     -= 1
        longitude_0 -= rad_six 
    if zone==34 and latBand=='X' and longitude>=21:
        zone     += 1
        longitude_0 += rad_six 
    if zone==36 and latBand=='X' and longitude< 33:
        zone     -= 1
        longitude_0 -= rad_six 
    if zone==36 and latBand=='X' and longitude>=33:
        zone     += 1
        longitude_0 += rad_six 

    lat       = latitude
    latitude  = radians(latitude)
    longitude = radians(longitude) -longitude_0

    # easting, northing: Karney 2011 Eq 7-14, 29, 35:

    e         = sqrt(f*(2-f)) #eccentricity
    n         = f / (2 - f)   #3rd flattening 
    n2        = n**2
    n3        = n**3
    n4        = n**4
    n5        = n**5
    n6        = n**6

    cos_l     = cos(longitude)
    sin_l     = sin(longitude)
    tan_l     = tan(longitude)

    tau       = tan(latitude)
    sigma     = sinh(e* atanh(e* tau/ sqrt(1+ tau**2)))
    tau_p     = tau * sqrt(1+sigma**2) - sigma * sqrt(1+ tau**2)

    xi_p      = atan2(tau_p, cos_l)
    eta_p     = asinh(sin_l / sqrt(tau_p**2 + cos_l**2))

    a_s       = a/( 1 + n ) * ( 1 + 1/4 * n2 + 1/64 * n4 + 1/256 * n6)

    alpha     = [None, 
                    1/2 * n - 2/3 * n2 + 5/16 * n3 +   41/180 * n4 - 127/288 * n5 + 7891/37800 * n6,
                    13/48 * n2 -  3/5 * n3 + 557/1440 * n4 + 281/630 * n5 - 1983433/1935360 * n6,
                    61/240 * n3 -  103/140 * n4 + 15061/26880 * n5 + 167603/181440 * n6,
                    49561/161280 * n4 - 179/168 * n5 + 6601661/7257600 * n6,
                    34729/80640 * n5 - 3418889/1995840 * n6,
                    212378941/319334400 * n6 ]

    xi        = xi_p
    
    for j in range(1,7,1):
        xi += alpha[j] * sin(2 * j * xi_p) * cosh(2 * j * eta_p)

    eta       = eta_p

    for j in range(1,7,1):
        eta += alpha [j] * cos(2* j * xi_p) * sinh(2 * j* eta_p)

    x         = 0.9996 * a_s * eta #0.996 = UTM scale on the central meridian
    y         = 0.9996 * a_s * xi

    # convergence: Karney 2011 Eq 23, 24
    p_p       = 1
    
    for j in range(1,7,1):
        p_p += 2 * j * alpha[j] * cos(2 * j * xi_p) * cosh(2 * j * eta_p)

    q_p       = 0
    
    for j in range(1,7,1):
    	q_p += 2 * j * alpha[j] * sin(2 * j * xi_p) * sinh(2 * j * eta_p)

    gamma_p  = atan(tau_p / sqrt(1+tau_p**2)*tan_l)
    gamma_pp = atan2(q_p, p_p)
    gamma    = gamma_p + gamma_pp

    # scale: Karney 2011 Eq 25

    sin_lat = sin(latitude)
    k_p     = sqrt(1 - e**2 * sin_lat**2) *\
              sqrt(1 + tau**2) / sqrt(tau_p**2 + cos_l**2)

    k_pp    = a_s / a * sqrt(p_p**2 + q_p**2)
    k       = 0.9996 * k_p * k_pp

    x       = x + 500e3

    if (y < 0):
        y += 10000e3

    return {'zone':zone,
            'coordinate':(round(x,9),round(y,9),"N" if lat>0 else "S"),
            'convergence': round(degrees(gamma),9),
            'scale': round(k,12)
            }

def utm2llh(
            zone:float,
            coordinate:Tuple[float],
            a:float = 6378137, 
            f:float = 1/298.257223563)->Dict:
    
    '''
        Convert from utm to latlon
        Based on https://www.movable-type.co.uk/scripts/latlong-utm-mgrs.html
        Reference: Karney 2011 ‘Transverse Mercator with an accuracy of a few nanometers’

        Keyword arguments:
            zone         -- UTM zone
            coordinate  -- (easting,northing,hemisphere)
            a  -- Earth's radius (default:6378137.0)
            f  -- flattening (default:1/298.257223563)        
        Output:        
	        dictionary -- {
                coordinate: tuple with latlon coordinates
                convergence: meridian convergence (bearing of grid north 
                            clockwise from true north), in degrees.
                scale: grid scale factor
            }

    '''
    
    easting    = coordinate[0]
    northing   = coordinate[1]
    h          = coordinate[2]

    x          = easting - 500e3
    if h=='S':
        y = northing - 10000e3
    else:
        y = northing
    
    # from Karney 2011 Eq 15-22, 36

    e         = sqrt(f*(2-f)) #eccentricity
    n         = f / (2 - f)   #3rd flattening 
    n2        = n**2
    n3        = n**3
    n4        = n**4
    n5        = n**5
    n6        = n**6
    
    a_s         = a/(1 + n) * (1 + 1/4 * n2 + 1/64 * n4 + 1/256 * n6)
    eta       = x /(0.9996 * a_s)
    xi        = y /(0.9996 * a_s)

    beta = [None,
                1/2 * n - 2/3 * n2 + 37/96 * n3 - 1/360 * n4 - 81/512 * n5 + 96199/604800 * n6,
                1/48 * n2 + 1/15 * n3 - 437/1440 * n4 + 46/105 * n5 - 1118711/3870720 * n6,
                17/480 * n3 - 37/840 * n4 - 209/4480 * n5 + 5569/90720 * n6,
                4397/161280 * n4 - 11/504 * n5 - 830251/7257600 * n6,
                4583/161280 * n5 - 108847/3991680 * n6,
                20648693/638668800 * n6]

    xi_p = xi
    
    for j in range(1,6,1):
        xi_p -= beta[j] * sin(2 * j * xi) * cosh(2 * j * eta)

    eta_p = eta
    
    for j in range(1,6,1):
        eta_p -= beta[j] * cos(2 * j * xi) * sinh(2 * j * eta)

    sinh_eta_p  = sinh(eta_p)
    sin_xi_p    = sin(xi_p)
    cos_xi_p    = cos(xi_p)

    tau_p       = sin_xi_p / sqrt(sinh_eta_p**2 + cos_xi_p**2)

    delta_tau_i = 1e12
    tau_i       = tau_p
    
    while (abs(delta_tau_i) > 1e-12):
        sigma_i     = sinh(e * atanh(e * tau_i/ sqrt(1+tau_i**2)))
        tau_i_p     = tau_i * sqrt(1 + sigma_i**2) - sigma_i * sqrt(1 + tau_i**2)
        delta_tau_i = (tau_p - tau_i_p)/sqrt(1 + tau_i_p**2) *\
                      (1 + (1 - e**2)* tau_i**2) / ((1-e**2)*sqrt(1+tau_i**2))
        tau_i += delta_tau_i
    
    tau     = tau_i
    phi     = atan(tau)
    lambda_ = atan2(sinh_eta_p, cos_xi_p)

    #convergence: Karney 2011 Eq 26, 27
    p = 1
    
    for j in range(1,7,1):
        p -= 2 * j * beta[j] * cos(2 * j * xi) * cosh(2 * j * eta)
        
    q = 0
    for j in range(1,7,1):
        q += 2 * j * beta[j] * sin(2 * j * xi) * sinh(2 * j * eta)

    gamma_p  = atan(tan(xi_p) * tanh(eta_p))
    gamma_pp = atan2(q, p)
    gamma    = gamma_p + gamma_pp

    #Karney 2011 Eq 28

    sin_phi = sin(phi)
    k_p = sqrt(1 - e**2 * sin_phi**2) * sqrt(1 + tau**2) *\
          sqrt(sinh_eta_p**2 + cos_xi_p**2)
    
    k_pp = a_s / a / sqrt(p**2 + q**2)

    k = 0.9996 * k_p * k_pp


    lambda_0 = radians((zone-1)*6 - 180 + 3)
    lambda_ += lambda_0
    
    return {
            'coordinate': (round(degrees(phi),14),
                           round(degrees(lambda_),14)),
            'convergence': round(degrees(gamma),9),
            'scale': round(k,12),               
            }