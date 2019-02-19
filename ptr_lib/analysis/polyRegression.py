# -*- coding: cp1252 -*-

#
# Copyright (c) 2014-2018 Alex Boava <alex.boava@usp.br> e 
# R.Pissardini <rodrigo AT pissardini DOT com> 
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


def polyRegression(ts, poly=2):

    '''
    polyRegression is a function to calculate the POLINOMIAL REGRESSION of a time series until the 5º term.
    
                                y = B0 + B1.x +  B2.x^2 + B3.x^3 ... Bn.x^n
                        
    INPUT:
        ts   - the time series
        poly - number of terms
        
    OUTPUT:
        B        - Regression output parameters
        ts_trend - Regression calculated coordinates. Output to construct graphs or calculate error of regression.
    
    '''
    
    if poly > 5:
        print("\n \t \t The number of terms must be less than or equal to 5 \n")
    else:
        ts_trend=[]
        ls      = []
        summ    = 0.0
        Z = ts
    
        for i in range(poly):
            ls.append([])
        
        for i in range(poly):
            for ind in range(len(ts)):
                ls[i].append([float(ts.index[ind])**i])
    
        A = np.hstack(lista)
        At = A.transpose()

        result1 = np.linalg.inv((At.dot(A)))
        result2 = (At.dot(Z))
        
        B = result2.dot(result1)
        
        for x in range(len(ts)):
            summ = 0.0 
            for i in range(len(B)):
                summ = summ + (B[i] * pow(x,i))
            ts_trend.append(summ)
        
        return B, ts_trend
