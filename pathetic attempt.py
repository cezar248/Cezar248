import PySimpleGUI as sg
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import re


def draw_plot():
    plot((arange(100) / 100))

    x = np.array(range(100))
    y = eval(values["your input"])

    # Create the plot
    plt.plot(x, y, label='your input')

    # Add a title
    plt.title("your tittle here")

    # Add X and y Label
    plt.xlabel('x axis')
    plt.ylabel('y axis')

    # Add a grid
    plt.grid(alpha=.4, linestyle='--')

    # Add a Legend
    plt.legend()

    # Show the plot
    plt.show()


layout = [[sg.Button('Plot'), sg.Cancel(), sg.Button('Popup'), sg.Input(key="your input")]]

window = sg.Window('Have some Matplotlib....', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    elif event == 'Plot':
        draw_plot()
    elif event == 'Popup':
        sg.popup('Yes, your application is still running')


window.close()