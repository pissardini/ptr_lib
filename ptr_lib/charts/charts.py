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


import matplotlib.pyplot as plt
import math
import numpy as np
from random import random

def generate_colors(nr_colors = 10,
                    cmap      = None):
    """
    Generate random number of colors
    """
    if cmap is None:
        return [(random(),random(),random()) for i in range(255)]
    else:
        return plt.cm.get_cmap(cmap, nr_colors)

def skyplot_gnss (prn,
                  e,
                  az,
                  show_prn = True,
                  bgcolor  = 'white',
                  size=(10,10)):
    """
    Generate a skyplot from gnss data
    """
    fig = plt.figure()
    ax  = fig.add_subplot(111, projection='polar')

    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_ylim(0,90)
    ax.set_yticks(np.arange(0,91,30))
    ax.set_yticklabels(ax.get_yticks()[::-1])

    for sv, elev, azim in zip(prn, e, az):
        ax.plot(math.radians(azim), 90-elev,color='green', marker='o', markersize=20)
        if show_prn is True:
            ax.text(math.radians(azim), 90-elev, sv, ha='center', va='center',color='white')

    plt.show()
