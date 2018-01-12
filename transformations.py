import math

def geodetic2cartesian(lat,lon,alt):
    lat = (lat * math.pi / 180.0)
    lon = (lon * math.pi / 180.0)
    
    a = 6378137.0 #semi-eixo maior
    e2 = 6.6943799901377997e-3 #1a excentricidade
    v = a/(math.sqrt(1-e2 * (math.sin(lat)*math.sin(lat))))

    x = (v + alt)* math.cos(lat)*math.cos(lon)
    y = (v + alt)* math.cos(lat)*math.sin(lon)
    z = (v * (1-e2)+ alt) * math.sin(lat)

    return [x,y,z]

#Transformations between quaternions and Euler's angles

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
        Y = 360/math.pi * math.atan2(qx,qw)
        Z = 90
        X = 0
        return [X,Y,Z]

    if (test < -0.499):
        Y = -360/math.pi*math.atan2(qx,qw)
        Z = -90
        X = 0
        return [X,Y,Z]

    h     = math.atan2(2 * qy * qw - 2 * qx * qz, 1 - 2 * qy * qy - 2 * qz * qz)
    a     = math.asin (2 * qx * qy + 2 * qz * qw)
    b     = math.atan2(2 * qx * qw - 2 * qy * qz, 1 - 2 * qx * qx - 2 * qz * qz)
    Y = h * 180/math.pi
    Z = a * 180/math.pi
    X = b * 180/math.pi

    return [X, Y, Z]


def euler2quat(X,Y,Z):
    
    h  = Y * math.pi/360
    a  = Z * math.pi/360
    b  = X * math.pi/360
    c1 = math.cos(h)
    c2 = math.cos(a)
    c3 = math.cos(b)
    s1 = math.sin(h)
    s2 = math.sin(a)
    s3 = math.sin(b)
    qw = ((c1 * c2 * c3 - s1 * s2 * s3)* 100000)/100000
    qx = ((s1 * s2 * c3 + c1 * c2 * s3)* 100000)/100000
    qy = ((s1 * c2 * c3 + c1 * s2 * s3)* 100000)/100000
    qz = ((c1 * s2 * c3 - s1 * c2 * s3)* 100000)/100000
    return [qw, qx, qy, qz]

