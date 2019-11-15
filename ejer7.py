# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 08:42:05 2019

@author: lab
"""

devices=["R1","R2","R3","S1","S2"]
switches=[]
for item in devices:
    if "S" in item:
    switches.append(item)