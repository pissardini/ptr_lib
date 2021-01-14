# -*- coding: cp1252 -*-

#
# Copyright (c) 2014-2021 R.Pissardini <rodrigo AT pissardini DOT com>
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

import pissardini2018

def context            (data,
                       model  ='pissardini2018',
                       mclass = 'cno'):

    """
    Input:
        data: a dictionary with following format:
            {cno  :[cno_sat1,cno_sat2,...],
             sat  :[prn1,prn2,...],
             pdop :value}
        model: model of scenario detection
            pissardini2018: Detecção automática de cenários internos e externos utilizando mensagens NMEA de receptores GNSS
            mclass: 
                - 'cno': use sum_cno only (recommended)
                - 'complete': use a combination of analysis and votation 
    Output:
        scenario: a list with scenario features.
    """
    if model =='pissardini2018':
        return pissardini2018.classifier(data, mclass)
    print("Model not found")