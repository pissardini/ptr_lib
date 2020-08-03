# -*- coding: cp1252 -*-

#
# Copyright (c) 2012-2020 R.Pissardini <rodrigo AT pissardini DOT com>
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

import joblib
import os
    
def save2zip(data,
             filename,
             compress=3):
    ''' Save data (matrices, list) to a zip file. 

        Keyword arguments:
	        data -- input data
                filename -- file to save data
                compress -- int from 0 to 9 or bool or 2-tuple (default:3)
        Output:
    '''
    joblib.dump(data, filename,compress=3)
    print ("Saved data")

def load_from_zip(filename):
    print("Loading data")
    return joblib.load(filename)

def mkdir(path):
    try:
        os.mkdir(path)
    except OSError:
        print (f"Creation of the directory {path} failed.")
    else:
        print (f"Successfully created the directory {path}.")

def rmdir(path):
    try:
        os.rmdir(path)
    except OSError as e:
        print (f"Deletion of the directory {path} failed.")
    else:
        print (f"Successfully deleted the directory {path}.")
