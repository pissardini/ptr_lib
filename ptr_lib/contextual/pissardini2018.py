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

from collections import Counter 

OUTDOOR_OPEN              = 3
OUTDOOR_BLOCKAGES         = 2
INDOOR_OPENINGS           = 1
INDOOR_WITHOUT_OPENINGS   = 0 

def sum_cno(value = 0): 
  if value>=350:
      return [3]
  elif value>=200 and value<350:
      return [2]
  elif value>=100 and value<200:
      return [1]
  return [0]

def avg_cno(value = 0): 
  if value>=30:
      return [3]
  elif value >=20 and value<30:
      return [2,1]
  return [0]

def sat(value = 0): 
  if value>3:
    return [1,2,3]
  return [0]

def dop(value = 0): 
  if value > 7: 
    return [0,1]
  else:
    return [2,3]

def pretty_cat(value):
  if value == 0:
    return [0,"Indoor without openings"]
  elif value == 1:
    return [1,"Indoor near openings"]
  elif value == 2:
    return [2,"Outdoor near blockages"]
  elif value == 3:
    return [2,"Open outdoor"]
  else:
    print("Value not found")

def classifier(data, mclass='cno'):
    """
    @article{pissardini2018,
      title={Detecção automática de cenários internos e externos utilizando mensagens NMEA de receptores GNSS},
      author={Pissardini, R.S. and Fonseca Junior, E.S.},
      journal={Revista Brasileira de Geomática},
      volume={6},
      number={4},
      pages={346--360},
      year={2018}
    }

    Input:
        data: a dictionary with following format:
            {cno  :[cno_sat1,cno_sat2,...],
             sat  :[prn1,prn2,...],
             pdop :value}
        mclass:
            - 'cno': use sum_cno only (recommended)
            - 'complete': use a combination of analysis and votation 
    Output:
        scenario: a list with scenario features.
    """
    if mclass =='cno':
      return pretty_cat(sum_cno(sum(data['cno']))[0])
    elif mclass =='complete':
      results = []
      results = sum_cno(sum(data['cno'])) +\
                avg_cno(sum(data['cno'])/len(data['cno'])) +\
                sat(len(data['sat']))+\
                dop(data['dop'])

      return pretty_cat(Counter(results).most_common(1)[0][0])
    else:
      print("Model not found")