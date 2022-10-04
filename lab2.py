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

        beb = fig.add_subplot(projection='3d')
        beb.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
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
                beb.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s")
            else:
                beb.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")

            txt.insert(INSERT, f"{i}) ({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {round(z_cs[i], 4)}\n")
            canvas.draw()

            window_lab_2.update()
            delay = txt_1.get()
            time.sleep(float(delay))

    def delete():
        txt.delete(1.0, END)

    window_lab_2 = tkinter.Tk()

    if sys.platform.startswith('win'):
        window_lab_2.iconbitmap(r'pic/Pop_cat_open.ico')
    else:
        window_lab_2.iconbitmap(r'@pic/Pop_cat_open.xbm')

    window_lab_2.wm_title("Лабораторная работа № 2")

    main_f = LabelFrame(window_lab_2, text="Параметры")
    left_f = Frame(main_f)
    right_f = Frame(main_f)
    txt_f = LabelFrame(window_lab_2, text="Консоль лог")

    x, y, z = makeData()

    fig = plt.figure()
    fig.add_subplot(projection='3d')

    canvas = FigureCanvasTkAgg(fig, master=window_lab_2)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, window_lab_2)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    lbl_1 = Label(left_f, text="Задержка в секундах")
    lbl_2 = Label(window_lab_2, text="Функция :\n2 * x1^2 + 2 * x1^2 + 2 * x2^2 - 4 * x1 - 6 * x2")

    txt_1 = Entry(right_f, width=10)

    txt = scrolledtext.ScrolledText(txt_f, width=40, height=10)

    btn_del = Button(window_lab_2, text="Очистить лог", width=10, command=delete)
    btn = Button(window_lab_2, text="Выполнить", width=10, command=draw)

    main_f.pack(side=LEFT, fill=Y, padx=5, pady=5)
    left_f.pack(side=LEFT, padx=5, pady=5)
    right_f.pack(side=RIGHT, padx=5, pady=5)
    txt_f.pack(side=RIGHT, padx=5, pady=5)

    lbl_1.pack(side=TOP, padx=5, pady=5)
    lbl_2.pack(side=TOP, padx=5, pady=5)

    txt_1.pack(side=TOP, padx=5, pady=5)

    txt.pack(padx=5, pady=5)

    btn_del.pack(side=RIGHT, padx=5, pady=5, anchor=S)
    btn.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    tkinter.mainloop()
