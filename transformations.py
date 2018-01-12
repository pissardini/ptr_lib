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
