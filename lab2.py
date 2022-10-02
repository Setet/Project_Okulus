import tkinter
from tkinter import *
from tkinter import scrolledtext

import sys
import time

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from SLSQP import kp, makeData


def Lab_2_window():
    def draw():
        fig.clf()

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        x_cs = []
        y_cs = []
        z_cs = []

        for i, point in kp():
            x_cs.append(point[0])
            y_cs.append(point[1])
            z_cs.append(point[2])

        for i in range(len(x_cs)):
            if i < (len(x_cs) - 1):
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s")
            else:
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")
            
            txt.insert(INSERT, f"{i}) ({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {round(z_cs[i], 4)}\n")
            canvas.draw()

            window_lab_2.update()
            time.sleep(0.5)

    def delete():
        txt.delete(1.0, END)

    window_lab_2 = tkinter.Tk()

    if ( sys.platform.startswith('win')): 
        window_lab_2.iconbitmap(r'pic/Pop_cat_open.ico')
    else:
        window_lab_2.iconbitmap(r'@pic/Pop_cat_open.xbm')

    window_lab_2.wm_title("Лабораторная работа № 2")

    x, y, z = makeData()

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    canvas = FigureCanvasTkAgg(fig, master=window_lab_2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, window_lab_2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    lbl_5 = Label(window_lab_2, text="Функция :\n2 * x1^2 + 2 * x1^2 + 2 * x2^2 - 4 * x1 - 6 * x2")
    lbl_5.pack(side=LEFT, padx=5, pady=5, anchor=N)

    lbl_5 = Label(window_lab_2, text="Консоль лог")
    lbl_5.pack(side=TOP, padx=5, pady=5)

    txt = scrolledtext.ScrolledText(window_lab_2, width=40, height=10)
    txt.pack(side=RIGHT, padx=5, pady=5)

    btn_del = Button(window_lab_2, text="Очистить лог", width=10, command=delete)
    btn_del.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    btn = Button(window_lab_2, text="Выполнить", width=10, command=draw)
    btn.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    tkinter.mainloop()
