
from tkinter import Tk, Button, HORIZONTAL
import time
from tkinter.ttk import Progressbar

import progressbar
ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x250+100+300')

def step():
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20

        time.sleep(1)

pb1 = Progressbar(ws, orient=HORIZONTAL, length=100)
pb1.grid(row=2,column=1)
# a=Button(ws,text="aaaa",command=step)
# a.grid(row=3,column=3)

step()
ws.mainloop()
# import tkinter as tk
# from functools import partial
#
# #
# def call_result(label_result, n1, n2):
#      num1 = (n1.get())
#      num2 = (n2.get())
#      result = int(num1) + int(num2)
#      label_result.config(text="Result = %d" % result)
#      return
# #
# #
# # root = tk.Tk()
# # root.geometry('400x200+100+200')
# #
# # root.title('Calculator')
# #
# # number1 = tk.StringVar()
# # number2 = tk.StringVar()
# #
# # labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)
# #
# # labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)
# #
# # labelResult = tk.Label(root)
# #
# # labelResult.grid(row=7, column=2)
# #
# # entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
# #
# # entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
# #
# # call_result = partial(call_result, labelResult, number1, number2)
# #
# def call_result(label_result, n1, n2):
#     num1 = (n1.get())
#     num2 = (n2.get())
#     result = int(num1) + int(num2)
#     label_result.config(text="Result = %d" % result)
#     def ok():
#        modal.destroy()
#     modal = tk.Tk()
#     modal.geometry('400x200+300+500')
#     button= tk.Button(modal, text="OK",command=ok)
#     button.grid(column=2 ,row=1, padx=40,pady=50)
#
#     return
# root = tk.Tk()
# root.geometry('800x400+100+200')
# root.title('Calculator')
# number1 = tk.StringVar()
# number2 = tk.StringVar()
#
#
# labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)
# labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)
# labelResult = tk.Label(root)
# labelResult.grid(row=7, column=2)
# entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
# entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
# call_result = partial(call_result, labelResult, number1, number2)
# buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)
# root.mainloop()