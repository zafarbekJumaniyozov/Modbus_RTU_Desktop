from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


window=Tk()
window.geometry('800x500')
window.configure(bg="aqua")
window.title('Diagramma')



def graph():
    water_height=np.random.normal(1000,7200,3000)
    plt.hist(water_height,50)
    plt.show(window)
myButton=Button(window,text="Graph",command=graph)
myButton.pack()


window.mainloop()
