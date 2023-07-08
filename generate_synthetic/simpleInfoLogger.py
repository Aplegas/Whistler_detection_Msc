#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:42:24 2021

@author: neural
"""
from blessings import Terminal
term = Terminal()
import numpy as np
 
def getProgressBar(progress,total, barWidth=100,processName='[iteration status]|whistler|'):
    """Returns a string that represents a progress bar that has barWidth
    bars and has progressed progress amount out of a total amount."""
    BAR = chr(9608) # Character 9608 is '█'
    progressBar = ''  # The progress bar will be a string value.
    progressBar += '|'  # Create the left end of the progress bar.

    # Make sure that the amount of progress is between 0 and total:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    # Calculate the number of "bars" to display:
    numberOfBars = int((progress / total) * barWidth)

    progressBar += BAR * numberOfBars  # Add the progress bar.
    progressBar += ' ' * (barWidth - numberOfBars)  # Add empty space.
    progressBar += '|'  # Add the right end of the progress bar.

    # Calculate the percentage complete:
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'  # Add percentage.

    # Add the numbers:
    progressBar += ' ' + str(progress) + '/' + str(total)
    #status name 
    progressBar += ' ' + str(processName)
    return progressBar

def getProgressBar2(progress,total, barWidth=100,processName='[iteration status]|whistler|'):
    """Returns a string that represents a progress bar that has barWidth
    bars and has progressed progress amount out of a total amount."""
    # Make sure that the amount of progress is between 0 and total:
    if progress > total:
        progress = total
    if progress < 0:
        progress = 0

    progressBar = '|'  # Add the right end of the progress bar.

    # Calculate the percentage complete:
    percentComplete = round(progress / total * 100, 1)
    progressBar += ' ' + str(percentComplete) + '%'  # Add percentage.

    # Add the numbers:
    progressBar += ' ' + str(progress) + '/' + str(total)
    #status name 
    progressBar += ' ' + str(processName)
    return progressBar


def processbar(bars_arr,at_bar,barlocation,L_value,n_h,modeltype="whistler"):
    "whistler function progress measure"
    index = list(np.where(bars_arr == at_bar)[0])
    if modeltype == "whistler":
        sbar=getProgressBar2(index[0]+1, len(bars_arr), barWidth=40,processName='[iteration status]|L_value: {:.5f}, n_h:{:.5f}, whistler|'.format(L_value,n_h))
        with term.location(0,barlocation):
                 print('\r'+sbar,end='')
    elif modeltype=="sferic":
        sbar=getProgressBar2(index[0]+1, len(bars_arr), barWidth=40,processName='[iteration status]|L_value: {:.5f}, sferic|'.format(L_value))
        with term.location(0,barlocation):
                 print('\r'+sbar,end='')

