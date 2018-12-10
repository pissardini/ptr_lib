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

#Computation of date and time 

def day_of_year(year,month,day):
	doy = datetime.datetime(year, month, day).timetuple().tm_yday
	return doy

def julian_date(year,month,day,hour,minute,second): 
        MJD0 = 2400000.5
        b = 0
        
        if (month <= 2):
                month +=12
                year -= 1

        if ((10000*year+100*month+day) <= 15821004):
                b = -2 + get_intpart (year+4716) - 1179
                
        else:
                b = get_intpart(year* 0.0025)- get_intpart(year* 0.01)+\
                    get_intpart(year *0.25)

        mjdmidnight = 365 *year - 679004 + b + (30.6001*(month+1)) + day
        fracofday = ((hour+ (minute/60)+ (second/3600)))/24
        return MJD0 + mjdmidnight + fracofday
