import math 
import numpy as np
from matplotlib import pyplot as plt
resistance=250
capacitance=0.001
current=10
charge=10
voltage=10
time=0.1

def exp(t,start):
    temp=(math.e)**(-t/(resistance*capacitance))
    return temp * start
print(f"Current at time {time}: {exp(time,current)}")
print(f"Voltage at time {time}: {exp(time,voltage)}")
print(f"Charge at time {time}: {exp(time,charge)}")

