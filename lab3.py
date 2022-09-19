import tkinter
from tkinter import *
from tkinter import scrolledtext

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from gradient_d import makeData, Funct_consider


def Lab_3_window():
    window_lab_3 = tkinter.Tk()
    window_lab_3.wm_title("Лабораторная работа № 3")

    x, y, z = makeData()

    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")

    canvas = FigureCanvasTkAgg(fig, master=window_lab_3)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, window_lab_3)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    lbl_1 = Label(window_lab_3, text="X")
    lbl_1.pack(side=LEFT, padx=5, pady=5)

    txt_1 = Entry(window_lab_3, width=10)
    txt_1.pack(side=LEFT, padx=5, pady=5)

    lbl_2 = Label(window_lab_3, text="Y")
    lbl_2.pack(side=LEFT, padx=5, pady=5)

    txt_2 = Entry(window_lab_3, width=10)
    txt_2.pack(side=LEFT, padx=5, pady=5)

    lbl_3 = Label(window_lab_3, text="Начальный шаг")
    lbl_3.pack(side=LEFT, padx=5, pady=5)

    txt_3 = Entry(window_lab_3, width=10)
    txt_3.pack(side=LEFT, padx=5, pady=5)

    lbl_4 = Label(window_lab_3, text="Число Итераций")
    lbl_4.pack(side=LEFT, padx=5, pady=5)

    txt_4 = Entry(window_lab_3, width=10)
    txt_4.pack(side=LEFT, padx=5, pady=5)

    lbl_5 = Label(window_lab_3, text="Функция Химмельблау")
    lbl_5.pack(side=LEFT, padx=5, pady=5, anchor=N)

    lbl_5 = Label(window_lab_3, text="Консоль лог")
    lbl_5.pack(side=TOP, padx=5, pady=5)

    txt = scrolledtext.ScrolledText(window_lab_3, width=40, height=10)
    txt.pack(side=RIGHT, padx=5, pady=5)

    btn_del = Button(window_lab_3, text="Очистить лог", width=10)
    btn_del.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    btn = Button(window_lab_3, text="Выполнить", width=10)
    btn.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    tkinter.mainloop()