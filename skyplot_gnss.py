#Name: skyplot_gnss.py
#Description: A simple script to create a skyplot view for GNSS satellites.
#Author: R.S. Pissardini <rodrigo AT usp DOT br>

import numpy as np
import matplotlib.pyplot as plt
import math

sv   = [1,2,3,4,5]
elev = [10,30,40,28,55]
azim = [100,200,211,345,321]

ax = plt.subplot(111, projection='polar')
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)
ax.set_rlim(90, 0, 1)
ax.set_yticks(np.arange(0, 91, 30))
ax.set_yticklabels(ax.get_yticks()[::-1])

flag = 0
for prn, e, az in zip(sv,elev,azim):
        ax.plot(math.radians(az), 90-e,color='green', marker='o', markersize=20)
                
plt.show()
