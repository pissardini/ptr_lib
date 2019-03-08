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


#General functions 

### Get Integer part from float
def get_intpart (value): 
	ipart = modf(value)
	return ipart[1]

### Get fractional part from float

def get_fracpart (value):
	fpart = modf(value)
	return fpart[0]

### Convert text to number

def str2num (text):
        try:
                number = float(text)
                return number
        except:
                return "Error: The string can not be converted to a number"


#Conversions 

def arcsec2radians (seconds):
    radians = seconds * 0.000004848
    return radians

def radians2arcsec (radians):
    seconds = radians * 206264.806247096
    return seconds

def dms2decimal (degrees, minutes, seconds, direction): #direction - N- S- W- E
    if (direction=='S' or direction=='W'):
        signal = -1
    elif (direction=='N' or direction=='E'):
        signal = 1
    else:
        print('[Error] Insert a correct direction [ N, S, W or E]\n')
        return
    
    decimal = signal * (int(degrees) + float(minutes) / 60 + float(seconds) / 3600)
    
    return decimal
    
def decimal2dms (decimal, direction): #N- E
    degrees = int(decimal)
    minutes = int (abs((decimal - int(decimal)) * 60))
    seconds = abs((abs((decimal - int(decimal)) * 60)-minutes)*60)
                  
    if (direction=='N'):
        if (decimal <0):
            direction ='S'
    elif (direction =='E'):
        if (decimal <0):
            direction ='W'
    else:
        print('[Error] Insert a correct direction [N or E]\n')
        return
    return [degrees,minutes,seconds,direction]
