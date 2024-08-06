# -*- coding: utf-8 -*-
#Script to stack-plot the various parameters from a plasma exposure

import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as ticker
import matplotlib
import matplotlib.font_manager as font_manager

filepath = 'C:/Users/apcwy/OneDrive - Massachusetts Institute of Technology\MIT_postdoc/TGS/Data/Tungsten_Fuzz/Tungsten_temperature_sweep/'
filename = 'temp_tungsten_tgs.txt'
length_temp = 850

#populate the data:
#population block
f = open(filepath+filename)
lines = f.readlines()[1:]
x_temp_list, y_SAW_speed_list, y_therm_diff_list, y_therm_diff_err_list = [], [], [], []
for line in lines:
    x_temp_list.append(line.split()[0])
    y_therm_diff_list.append(line.split()[3])
    y_therm_diff_err_list.append(line.split()[4])
    y_SAW_speed_list.append(line.split()[1])
f.close()
x_temp = [float(x) for x in x_temp_list]
y_TGS_therm_diff = [1000000*float(x) for x in y_therm_diff_list] 
y_TGS_therm_diff_err = [1000000*float(x) for x in y_therm_diff_err_list] 
y_SAW_speed = [0.001*float(x) for x in y_SAW_speed_list]


#Plot the figures 
Cfont = {'fontname':'Cambria'}
fig = plt.figure(figsize = (4,6), dpi = 300)
matplotlib.rcParams['axes.linewidth'] = 0.3
font = font_manager.FontProperties(family='Cambria',
                                   style='normal', size=9)

# set height ratios for subplots
gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1]) 

# the first subplot (TC)
ax_TD = plt.subplot(gs[0])
ax_TD.set_ylabel('Thermal diffusivity [mm$^2$s$^{-1}$]', **Cfont)
#ax_SAW.set_title('TGS of Rolled Plate W Under He Helicon Plasma Exposure', **Cfont)
ax_TD.set_xlim([0, length_temp])
plt.errorbar(x_temp, y_TGS_therm_diff, yerr=y_TGS_therm_diff_err, linestyle="",linewidth=1.5, marker="o", color='#853a75', markersize=1.5, capsize=1.5, ecolor = "#853a75")
xtics_TD = ax_TD.xaxis.set_major_locator(ticker.MaxNLocator(5))
ytics_TD = ax_TD.yaxis.set_major_locator(ticker.MaxNLocator(5))
ax_TD.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
plt.yticks(**Cfont)
ax_TD.tick_params(width=0.3)

# the second subplot (TGS SAW speed)
# shared axis X
ax_SAW_speed = plt.subplot(gs[1], sharex = ax_TD)
ax_SAW_speed.set_ylabel('SAW speed [km s$^{-1}$]', **Cfont)
points_SAW_speed, = ax_SAW_speed.plot(x_temp, y_SAW_speed, color='#430c3b', linestyle="",marker="o", markersize=1.5)
plt.setp(ax_TD.get_xticklabels(), visible=False)
ytics_SAW_speed = ax_SAW_speed.yaxis.set_major_locator(ticker.MaxNLocator(5))
ax_SAW_speed.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
ax_SAW_speed.set_xlabel('Temperature [$^{\circ}$C]', **Cfont)
plt.xticks(**Cfont)
plt.yticks(**Cfont)
ax_SAW_speed.tick_params(width=0.3)

# remove vertical gap between subplots
plt.subplots_adjust(hspace=.0)
plt.show()



















