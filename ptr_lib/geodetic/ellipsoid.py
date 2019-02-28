# -*- coding: cp1252 -*-

#
# Copyright (c) 2014-2019 R.Pissardini <rodrigo AT pissardini DOT com>
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


import numpy as np
from ptr_lib.constants import GPS_PI

class Ellipsoid:
    def __init__(self,                        #Default values for GRS80
                 a = 6378137,
                 b = 6356752.314140347,
                 f = 0.003352810681183637418,
                 e2=0.00669438002290):
        
        self.a = a
        self.b = b
        self.f = f                             # flattening
        self.e2 = e2                           # eccentricity squared
        self.e = pow(e2,0.5)                   # eccentricity
        self.e12 = self.e2 / (1 - self.e2)     # 2nd eccentricity squared
        self.e1 = pow(self.e12,0.5)            # 2nd eccentricity

    @property
    def equatorial_radius(self):
        return self.a

    @property
    def polar_radius(self):
        return self.b

    @property
    def flattening(self):
        return self.f
    
    @property
    def aspecto_ratio(self):
        return self.b/self.a

    @property
    def reciprocal_flattening(self):
        return 1 / self.flattening
    
    @property
    def eccentricity(self):
        return self.e
    
    @property
    def eccentricity_squared(self):
        return self.e2

    @property
    def second_eccentricity(self):
        return self.e1

    @property
    def second_eccentricity_squared(self):
        return self.e12

    @property
    def linear_eccentricity(self):
        return self.equatorial_radius * self.eccentricity
