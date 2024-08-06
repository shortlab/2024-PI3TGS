# -*- coding: utf-8 -*-
#Script to stack-plot the various parameters from a plasma exposure

import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as ticker
import matplotlib

filepath = 'C:/Users/apcwy/OneDrive - Massachusetts Institute of Technology\MIT_postdoc/TGS/Data/Tungsten_Fuzz/2024-05/2024-05-05/plotting/'
filename_current = 'current.txt'
filename_pyrometer = 'pyrometer.txt'
filename_thermal_diff = 'TGS_therm_diff.txt'
filename_SAW_speed = 'TGS_SAW_speed.txt'
filename_TC = 'thermocouple.txt'
length_mins = 298

#populate the data:
    
#TC population block
f = open(filepath+filename_TC)
lines_TC = f.readlines()[1:]
x_TC_list, y_TC_list = [], []
for line in lines_TC:
    x_TC_list.append(line.split()[0])
    y_TC_list.append(line.split()[1])
f.close()
x_TC = [float(x) for x in x_TC_list]
y_TC = [float(x) for x in y_TC_list] 

#current population block
f = open(filepath+filename_current)
lines_current = f.readlines()[1:]
x_current_list, y_current_list = [], []
for line in lines_current:
    x_current_list.append(line.split()[0])
    y_current_list.append(line.split()[1])
f.close()
x_current = [float(x) for x in x_current_list]
y_current = [float(x) for x in y_current_list] 

#pyrometer population block
f = open(filepath+filename_pyrometer)
lines_pyrometer = f.readlines()[1:]
x_pyrometer_list, y_pyrometer_list = [], []
for line in lines_pyrometer:
    x_pyrometer_list.append(line.split()[0])
    y_pyrometer_list.append(line.split()[1])
f.close()
x_pyrometer = [float(x) for x in x_pyrometer_list]
y_pyrometer = [float(x) for x in y_pyrometer_list] 

#Therm diff population block
f = open(filepath+filename_thermal_diff)
lines_TGS_therm_diff = f.readlines()[1:]
x_TGS_therm_diff_list, y_TGS_therm_diff_list, y_TGS_therm_diff_err_list = [], [], []
for line in lines_TGS_therm_diff:
    x_TGS_therm_diff_list.append(line.split()[0])
    y_TGS_therm_diff_list.append(line.split()[1])
    y_TGS_therm_diff_err_list.append(line.split()[2])
f.close()
x_TGS_therm_diff = [float(x) for x in x_TGS_therm_diff_list]
y_TGS_therm_diff = [1000000*float(x) for x in y_TGS_therm_diff_list] 
y_TGS_therm_diff_err = [1000000*float(x) for x in y_TGS_therm_diff_err_list] 


#SAW_speed population block
f = open(filepath+filename_SAW_speed)
lines_SAW_speed = f.readlines()[1:]
x_SAW_speed_list, y_SAW_speed_list, y_SAW_speed_err_list = [], [], []
for line in lines_SAW_speed:
    x_SAW_speed_list.append(line.split()[0])
    y_SAW_speed_list.append(line.split()[1])
    y_SAW_speed_err_list.append(line.split()[2])
f.close()
x_SAW_speed = [float(x) for x in x_SAW_speed_list]
y_SAW_speed = [0.001*float(x) for x in y_SAW_speed_list] 
y_SAW_speed_err = [0.001*float(x) for x in y_SAW_speed_err_list] 

#Plot the figures 
Cfont = {'fontname':'Cambria'}
textSize = 13
fig = plt.figure(figsize = (6,10), dpi = 300)
matplotlib.rcParams['axes.linewidth'] = 0.3

# set height ratios for subplots
gs = gridspec.GridSpec(5, 1, height_ratios=[1, 1, 1, 1, 1]) 

# the first subplot (TC)
ax_TC = plt.subplot(gs[0])
ax_TC.set_ylabel('On-sample\nthermocouple\n[$^\circ$C]', fontsize=textSize , **Cfont)
#ax_TC.set_title('TGS of Rolled Plate W Under He Helicon Plasma Exposure', fontsize=textSize , **Cfont)
ax_TC.set_xlim([0, length_mins])
points_TC, = ax_TC.plot(x_TC, y_TC, color='#277647',linestyle="",marker="o", markersize=1)
xtics_TC = ax_TC.xaxis.set_major_locator(ticker.MaxNLocator(5))
ytics_TC = ax_TC.yaxis.set_major_locator(ticker.MaxNLocator(4))
ax_TC.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
plt.yticks(**Cfont, fontsize=textSize )
ax_TC.tick_params(width=0.3)

# the second subplot (pyrometer)
# shared axis X
ax_pyrometer = plt.subplot(gs[1], sharex = ax_TC)
ax_pyrometer.set_ylabel('Pyrometer\n[$^\circ$C]', fontsize=textSize , **Cfont)
points_pyrometer, = ax_pyrometer.plot(x_pyrometer, y_pyrometer, color='#b3cc4d', linestyle="",marker="o", markersize=1)
plt.setp(ax_TC.get_xticklabels(), visible=False)
ytics_pyrometer = ax_pyrometer.yaxis.set_major_locator(ticker.MaxNLocator(4))
ax_pyrometer.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
plt.yticks(**Cfont, fontsize=textSize )
ax_pyrometer.tick_params(width=0.3)

# # the third subplot (current)
# # shared axis X
ax_current = plt.subplot(gs[2], sharex = ax_TC)
ax_current.set_ylabel('On-sample\ncurrent\n[mA]', fontsize=textSize , **Cfont)
points_current, = ax_current.plot(x_current, y_current, color='#ffc500', linestyle="",marker="o", markersize=1.5)
plt.setp(ax_pyrometer.get_xticklabels(), visible=False)
ytics_current = ax_current.yaxis.set_major_locator(ticker.MaxNLocator(4))
ax_current.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
plt.yticks(**Cfont, fontsize=textSize )
ax_current.tick_params(width=0.3)

# the fourth subplot (TGS therm diff)
# shared axis X
ax_TGS_therm_diff = plt.subplot(gs[3], sharex = ax_TC)
ax_TGS_therm_diff.set_ylabel('Thermal diffusivity\n[mm$^2$s$^{-1}$]', fontsize=textSize , **Cfont)
plt.errorbar(x_TGS_therm_diff, y_TGS_therm_diff, yerr=y_TGS_therm_diff_err, linestyle="", marker="o", color='#853a75', markersize=1, capsize=3, ecolor = "#853a75")
plt.setp(ax_current.get_xticklabels(), visible=False)
ytics_TGS_therm_diff = ax_TGS_therm_diff.yaxis.set_major_locator(ticker.MaxNLocator(4))
ax_TGS_therm_diff.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
plt.yticks(**Cfont, fontsize=textSize )
ax_TGS_therm_diff.tick_params(width=0.3)

# the fifth subplot (TGS SAW speed)
# shared axis X
ax_SAW_speed = plt.subplot(gs[4], sharex = ax_TC)
ax_SAW_speed.set_ylabel('SAW speed\n[km s$^{-1}$]', fontsize=textSize , **Cfont)
points_SAW_speed, = ax_SAW_speed.plot(x_SAW_speed, y_SAW_speed, color='#430c3b', linestyle="",marker="o", markersize=1)
plt.setp(ax_TGS_therm_diff.get_xticklabels(), visible=False)
ytics_SAW_speed = ax_SAW_speed.yaxis.set_major_locator(ticker.MaxNLocator(4))
ax_SAW_speed.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
ax_SAW_speed.set_xlabel('Time [minutes]', fontsize=textSize , **Cfont)
plt.xticks(**Cfont, fontsize=textSize )
plt.yticks(**Cfont, fontsize=textSize )
ax_SAW_speed.tick_params(width=0.3)

# remove vertical gap between subplots
plt.subplots_adjust(hspace=.0)
plt.show()

















