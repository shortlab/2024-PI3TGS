# -*- coding: utf-8 -*-
#Script to stack-plot the various parameters from a plasma exposure

import matplotlib.pyplot as plt
import matplotlib
import matplotlib.font_manager as font_manager
import numpy as np
import math

filepath = 'C:/Users/apcwy/OneDrive - Massachusetts Institute of Technology\MIT_postdoc/TGS/Data/Kyocera/Kyocera_W_W/'
filename_dpa = 'dpa_depth.txt'
filename_probe = 'normalised_probe_strength.txt'
max_depth = 2 #microns

#populate the data:
    
#population block
f = open(filepath+filename_dpa)
lines = f.readlines()[1:]
x_dpa_list, y_dpa_list, = [], []
for line in lines:
    x_dpa_list.append(line.split()[0])
    y_dpa_list.append(line.split()[1])
f.close()
x_dpa = [float(x) for x in x_dpa_list]
y_dpa = [float(x) for x in y_dpa_list] 

f = open(filepath+filename_probe)
lines_probe = f.readlines()[1:]
x_probe_list, y_probe_list = [], []
for line in lines_probe:
    x_probe_list.append(line.split()[0])
    y_probe_list.append(line.split()[1])
f.close()
x_probe = [float(x) for x in x_probe_list]
y_probe = [float(x) for x in y_probe_list] 

#Plot the figures 
Cfont = {'fontname':'Cambria'}
my_fontsize = 10
fig = plt.figure(figsize = (4,4), dpi = 300)
matplotlib.rcParams['axes.linewidth'] = 0.3
font = font_manager.FontProperties(family='Cambria',
                                   style='normal', size=my_fontsize-1)
# the plot 
plt.ylabel('Dose [dpa]', fontsize = my_fontsize, **Cfont)
plt.xlabel('Depth [μm]', fontsize = my_fontsize, **Cfont)
plt.ylim(0,15)
plt.xticks(np.arange(0.4, 2.1, step=0.4), fontsize = my_fontsize, **Cfont)
plt.yticks(np.arange(0, 15.5, step=3), fontsize = my_fontsize, **Cfont)
plt.xlim([0, max_depth])
points_dpa, = plt.plot(x_dpa, y_dpa, color='#853a75', linestyle="",marker="o", markersize=2, label='         Damage profile')
points_probe, = plt.plot(x_probe, y_probe, linestyle="-",marker="", markersize=0, color = "#277647", label='Thermal probe response\n           (normalised)')
plt.vlines(x = 3.5217/math.pi, ymin = 0, ymax = 5.4, colors = '#277647', linestyle="--")
plt.text(3.4/math.pi, 6.5, r'$\mathdefault{\frac{\Lambda}{\pi}}$', fontsize = 16, fontdict=Cfont)
plt.legend()
plt.legend(prop=font, frameon=False)
plt.tick_params(width=0.3)
plt.show()

#r'$\frac{\lambda}{\pi}$'
















