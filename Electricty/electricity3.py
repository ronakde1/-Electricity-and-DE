import math 
import numpy as np
from matplotlib import pyplot as plt
resistance=250
capacitance=0.001
current=10
charge=10
voltage=10
def capacitorgraph(resistance,capacitance,current,charge,voltage):
    x = np.linspace(0,1, 100)
    figure, axis = plt.subplots(2, 2)

    def exp(x,start):
        temp=(math.e)**(-x/(resistance*capacitance))
        return temp * start
    

    axis[0,0].plot(x, exp(x,current), color='red')
    axis[0,0].set_title("Current against time")
    axis[0,1].plot(x, exp(x,voltage), color='red')
    axis[0,1].set_title("Voltage against time")
    axis[1,0].plot(x, exp(x,charge), color='red')
    axis[1,0].set_title("Charge against time")
    axis[1,1].plot(x, exp(x,current)*exp(x,voltage), color='red')
    axis[1,1].set_title("Power against time")
    figure.tight_layout()
    plt.show()

capacitorgraph(resistance,capacitance,current,charge,voltage)
