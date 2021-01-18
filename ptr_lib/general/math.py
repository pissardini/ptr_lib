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

from math import *


def get_intpart (number):
    """ Get the integer part of a float number. 

        Keyword arguments:
	        number -- input number
        Output:
                ipart  -- integer part
    """
    ipart = modf(number)
    return ipart[1]


def get_fracpart (number):
    """ Get the fractional part of a float number. 

        Keyword arguments:
	        number -- input number
        Output:
                fpart  -- decimal part
    """
    fpart = modf(number)
    return fpart[0]

def str2num (text):
    """ Convert string to number. 

        Keyword arguments:
	        text    -- number in string format
        Output:
                number  -- number converted
    """
    try:
        number = float(text)
        return number
    except:
        print("Error: The string can not be converted to a number")

def avg(ls):
    """ Calculate average between numbers of a list 
    """
    return sum(ls)/float(len(ls))

def pvariance(ls):
    """
    Populational variance
    """
    avg = sum(ls) / len(ls)
    return sum([(xi - avg) ** 2 for xi in ls]) / len(ls)


def stdev(ls, population=False): #False: Excel mode
    """
    Standard-deviation
        population: False: Excel standard.
    """
    num_items = len(ls)  
    mean = sum(ls) / len(ls)
    differences = [x - mean for x in ls]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)
    
    if population is True: #population
        variance = ssd / num_items
    else: #sample
        variance = ssd / (num_items - 1)
    sd = sqrt(variance)
    return sd
