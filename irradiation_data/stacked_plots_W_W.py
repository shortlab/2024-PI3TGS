# -*- coding: utf-8 -*-
#Script to stack-plot the various parameters from a plasma exposure

import matplotlib.pyplot as plt
from matplotlib import gridspec
import matplotlib.ticker as ticker
import matplotlib
import matplotlib.font_manager as font_manager

filepath = 'C:/Users/apcwy/OneDrive - Massachusetts Institute of Technology\MIT_postdoc/TGS/Data/Kyocera/Kyocera_W_W/'
filename = 'processed_data_W_into_W.txt'
filenameReza = 'Reza_2020_W_into_W_dpa_scaled.txt'
length_dpa = 8

#populate the data:
    
#population block
f = open(filepath+filename)
lines = f.readlines()[1:]
x_dpa_list, y_SAW_speed_list, y_therm_diff_list, y_therm_diff_err_list = [], [], [], []
for line in lines:
    x_dpa_list.append(line.split()[1])
    y_therm_diff_list.append(line.split()[2])
    y_therm_diff_err_list.append(line.split()[3])
    y_SAW_speed_list.append(line.split()[4])
f.close()
x_dpa = [float(x) for x in x_dpa_list]
y_TGS_therm_diff = [1000000*float(x) for x in y_therm_diff_list] 
y_TGS_therm_diff_err = [1000000*float(x) for x in y_therm_diff_err_list] 
y_SAW_speed = [0.001*float(x) for x in y_SAW_speed_list]

# f = open(filepath+filenameReza)
# lines_Reza = f.readlines()[1:]
# x_Reza_dpa_list, y_Reza_therm_diff_list, y_Reza_therm_diff_err_list = [], [], []
# for line_Reza in lines_Reza:
#     x_Reza_dpa_list.append(line_Reza.split()[0])
#     y_Reza_therm_diff_list.append(line_Reza.split()[1])
#     y_Reza_therm_diff_err_list.append(line_Reza.split()[2])
# f.close()
x_Reza_dpa =                [float(0.000000000),float(5.97065E-05),float(0.000190969),float(0.000595886),float(0.001921704),float(0.006045981),float(0.010857469),float(0.019179096),float(0.033878772),float(0.060840041),float(0.192997132),float(0.602212697),float(1.942108867),float(6.06)]
y_Reza_TGS_therm_diff =     [float(67.51517678),float(67.81460093),float(60.64513351),float(59.59704952),float(49.82527791),float(41.02658502),float(37.98360011),float(35.36305857),float(34.19354699),float(31.56106827),float(30.37033504),float(30.99935786),float(29.88522151),float(31.62605956)] 
y_Reza_TGS_therm_diff_err = [float(2.272295252),float(2.442669765),float(2.800056651),float(1.264248016),float(1.091948043),float(0.807866878),float(0.640560961),float(0.598910111),float(0.672224824),float(0.720810925),float(0.580447954),float(0.499523573),float(0.674062609),float(0.81241919),] 

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
ax_TD.set_xlim([-0.1, length_dpa])
plt.errorbar(x_dpa, y_TGS_therm_diff, yerr=y_TGS_therm_diff_err, linestyle="",linewidth=0.5, marker="o", color='#853a75', markersize=0.5, capsize=0.5, ecolor = "#853a75", label='In-situ TGS')
plt.errorbar(x_Reza_dpa, y_Reza_TGS_therm_diff, yerr=y_Reza_TGS_therm_diff_err, linestyle="",linewidth=1, marker="o", color='#fca636', markersize=1, capsize=1, ecolor = "#fca636", label='Reza et al.')
xtics_TD = ax_TD.xaxis.set_major_locator(ticker.MaxNLocator(5))
ytics_TD = ax_TD.yaxis.set_major_locator(ticker.MaxNLocator(5))
ax_TD.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.0f'))
plt.yticks(**Cfont)
handles, labels = ax_TD.get_legend_handles_labels()
ax_TD.legend(handles, labels)
ax_TD.legend(prop=font)
ax_TD.tick_params(width=0.3)

# the second subplot (TGS SAW speed)
# shared axis X
ax_SAW_speed = plt.subplot(gs[1], sharex = ax_TD)
ax_SAW_speed.set_ylabel('SAW speed [km s$^{-1}$]', **Cfont)
points_SAW_speed, = ax_SAW_speed.plot(x_dpa, y_SAW_speed, color='#430c3b', linestyle="",marker="o", markersize=1)
plt.setp(ax_TD.get_xticklabels(), visible=False)
ytics_SAW_speed = ax_SAW_speed.yaxis.set_major_locator(ticker.MaxNLocator(5))
ax_SAW_speed.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
ax_SAW_speed.set_xlabel('Dose [dpa]', **Cfont)
plt.xticks(**Cfont)
plt.yticks(**Cfont)
ax_SAW_speed.tick_params(width=0.3)

# remove vertical gap between subplots
plt.subplots_adjust(hspace=.0)
plt.show()


















