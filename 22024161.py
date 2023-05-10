#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 18:32:59 2023

@author: mukeshavudaiappan
"""
# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec

df = pd.read_csv("Uk_climate.csv")

# Set seaborn style
sns.set(style="whitegrid")

# Creating a GridSpec layout
fig = plt.figure(figsize=(20, 15))
gs = gridspec.GridSpec(4, 2, figure=fig)

# Plot 1: Boxplot of AvgTemperature by Month
ax1 = fig.add_subplot(gs[0, 0])
sns.boxplot(data=df, x='month', y='AvgTemperature', palette='magma', ax=ax1)
ax1.set_xlabel('Month', fontsize=14)
ax1.set_ylabel('Avg Temp', fontsize=14)
ax1.set_title('Monthly Average Temperature', fontsize=16)

# Plot 2: Density plot of AvgTemperature by county
ax2 = fig.add_subplot(gs[0, 1])
for county in df['county'].unique():
    sns.kdeplot(df[df['county'] == county]
                ['AvgTemperature'], label=county, ax=ax2)
ax2.set_xlabel('Avg Temp', fontsize=14)
ax2.set_ylabel('Density', fontsize=14)
ax2.set_title('County-Level Temperature dispersion', fontsize=16)
ax2.legend()

# Plot 3: Scatter plot of AvgTemperature by month of year (colored by year)
ax4 = fig.add_subplot(gs[1, 0])
sns.scatterplot(data=df, x='month', y='AvgTemperature',
                palette='magma', hue='year', ax=ax4)
ax4.set_xlabel('Month', fontsize=14)
ax4.set_ylabel('Avg Temp', fontsize=14)
ax4.set_title('Temperature by month of year', fontsize=16)

# Plot 4: Barplot of Average Temperature by county
ax3 = fig.add_subplot(gs[1, 1])
county_temp = df.groupby('county')['AvgTemperature'].mean().reset_index()
sns.barplot(data=county_temp, x='county',
            y='AvgTemperature', palette='magma', ax=ax3)
ax3.set_xlabel('County', fontsize=14)
ax3.set_ylabel('Avg Temp', fontsize=14)
ax3.set_title('County-Level Average Temperature', fontsize=16)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=30)

# Plot 5: Lineplot of AvgTemperature by Year (with error bands)
ax5 = fig.add_subplot(gs[2, :])
sns.lineplot(data=df, x='year', y='AvgTemperature',
             hue='county', ci='sd', ax=ax5)
ax5.set_xlabel('Year', fontsize=14)
ax5.set_ylabel('Avg Temp', fontsize=14)
ax5.set_title('Average Temperature by Year (with error bands)', fontsize=16)

# Adding header for chart
fig.suptitle('Temperature Analysis\nStudent Name : Mukesh Avudaiappan\nID : 22024161', fontsize=22,
             fontweight='bold')

# Adding textbox for explaination
explanation = '''This dashboard displays the five decades of temperature distribution and trends over 5 counties, months & years :

 1. Monthly Average Temperature: The range of monthly average temperatures is displayed in this box plot.
 2. County-Level Temperature dispersion: This density map shows the county-level temperature dispersion.
 3. Temperature by Month of Year: The average temperature for each month of the year is displayed on this scatter plot, which is color-coded by the year.
 4. County-Level Average Temperature: This bar graph shows the county-level average temperature.
 5. Average Temperature by Year (with Error Bands): This line plot shows the average temperature trends by year and includes error bands that indicate the 
    standard deviation.'''

# Setting position of the textbox
textbox = plt.figtext(0.1, 0.05, explanation, fontsize=16, wrap=True, bbox=dict(
    facecolor='lightgrey', edgecolor='black', boxstyle='round,pad=1'))

plt.tight_layout()
plt.subplots_adjust(top=0.9)
plt.savefig('22024161.png', dpi=300)
