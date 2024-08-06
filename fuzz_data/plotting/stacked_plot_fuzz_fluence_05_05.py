# -*- coding: utf-8 -*-
#Script to stack-plot the various parameters from a plasma exposure

import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as ticker
import matplotlib

filepath = 'C:/Users/apcwy/OneDrive - Massachusetts Institute of Technology\MIT_postdoc/TGS/Data/Tungsten_Fuzz/2024-05/2024-05-05/plotting/'
filename = 'TGS_vs_fluence.txt'
length_fluence = 1.17806

#populate the data:
    
#fluence population block
f = open(filepath+filename)
lines_fluence = f.readlines()[1:]
x_fluence_list, y_TGS_therm_diff_list, y_TGS_therm_diff_err_list, y_SAW_speed_list = [], [], [], []
for line in lines_fluence:
    x_fluence_list.append(line.split()[0])
    y_TGS_therm_diff_list.append(line.split()[2])
    y_TGS_therm_diff_err_list.append(line.split()[3])
    y_SAW_speed_list.append(line.split()[1])
f.close()
x_fluence = [1E-18*float(x) for x in x_fluence_list] 
y_TGS_therm_diff = [1000000*float(x) for x in y_TGS_therm_diff_list] 
y_TGS_therm_diff_err = [1000000*float(x) for x in y_TGS_therm_diff_err_list] 
y_SAW_speed = [0.001*float(x) for x in y_SAW_speed_list] 

#Plot the figures 
Cfont = {'fontname':'Cambria'}
textSize = 13
fig = plt.figure(figsize = (4,6), dpi = 300)
matplotlib.rcParams['axes.linewidth'] = 0.3

# set height ratios for subplots
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1]) 

# the first subplot (TC)
ax_TD = plt.subplot(gs[0])
ax_TD.set_ylabel('Thermal diffusivity [mm$^2$s$^{-1}$]', **Cfont)
#ax_SAW.set_title('TGS of Rolled Plate W Under He Helicon Plasma Exposure', **Cfont)
ax_TD.set_xlim([-0.001, length_fluence+0.023])
plt.errorbar(x_fluence, y_TGS_therm_diff, yerr=y_TGS_therm_diff_err, linestyle="",linewidth=0.7, marker="o", color='#853a75', markersize=0.7, capsize=0.7, ecolor = "#853a75", label='In-situ TGS')
xtics_TD = ax_TD.xaxis.set_major_locator(ticker.MaxNLocator(7))
ytics_TD = ax_TD.yaxis.set_major_locator(ticker.MaxNLocator(5))
ax_TD.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
plt.yticks(**Cfont)
ax_TD.tick_params(width=0.3)

# the second subplot (TGS SAW speed)
# shared axis X
ax_SAW_speed = plt.subplot(gs[1], sharex = ax_TD)
ax_SAW_speed.set_ylabel('SAW speed [km s$^{-1}$]', **Cfont)
points_SAW_speed, = ax_SAW_speed.plot(x_fluence, y_SAW_speed, color='#430c3b', linestyle="",marker="o", markersize=1)
plt.setp(ax_TD.get_xticklabels(), visible=False)
ytics_SAW_speed = ax_SAW_speed.yaxis.set_major_locator(ticker.MaxNLocator(5))
ax_SAW_speed.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
ax_SAW_speed.set_xlabel('Fluence [10$^{18}$ cm$^{-2}$]', **Cfont)
plt.xticks(**Cfont)
plt.yticks(**Cfont)
ax_SAW_speed.tick_params(width=0.3)

# remove vertical gap between subplots
plt.subplots_adjust(hspace=.0)
plt.show()

















