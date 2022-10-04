import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox

import sys

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from Rosenbrock_function import makeData


def Lab_3_window():
    def draw():
        fig.clf()

        if combo.get() == "Min":
            txt.insert(INSERT, "Что-то делаешь если Max")
        elif combo.get() == "Max:":
            txt.insert(INSERT, "Что-то делаешь если Max")

        beb = fig.add_subplot(projection='3d')
        beb.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

    def delete():
        txt.delete(1.0, END)

    window_lab_3 = tkinter.Tk()

    if sys.platform.startswith('win'):
        window_lab_3.iconbitmap(r'pic/Pop_cat_open.ico')
    else:
        window_lab_3.iconbitmap(r'@pic/Pop_cat_open.xbm')

    window_lab_3.wm_title("Лабораторная работа № 3")

    main_f = LabelFrame(window_lab_3, text="Параметры")
    left_f = Frame(main_f)
    right_f = Frame(main_f)
    txt_f = LabelFrame(window_lab_3, text="Консоль лог")

    x, y, z = makeData()

    fig = plt.figure()

    fig.add_subplot(projection='3d')

    canvas = FigureCanvasTkAgg(fig, master=window_lab_3)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, window_lab_3)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    lbl_1 = Label(left_f, text="Количество агентов")
    lbl_2 = Label(left_f, text="Количество итераций")
    lbl_3 = Label(left_f, text="Разброс мутации")
    lbl_4 = Label(left_f, text="Выбор без выбора")
    lbl_5 = Label(left_f, text="Задержка в секундах")
    lbl_6 = Label(window_lab_3, text="Функция Розенброка")

    txt_1 = Entry(right_f, width=10)
    txt_2 = Entry(right_f, width=10)
    txt_3 = Entry(right_f, width=10)
    combo = Combobox(right_f)
    combo['values'] = ("Min", "Max")
    txt_4 = Entry(right_f, width=10)
    txt = scrolledtext.ScrolledText(txt_f, width=40, height=10)
    btn_del = Button(window_lab_3, text="Очистить лог", width=10, command=delete)
    btn = Button(window_lab_3, text="Выполнить", width=10, command=draw)

    main_f.pack(side=LEFT, fill=Y, padx=5, pady=5)
    left_f.pack(side=LEFT, padx=5, pady=5)
    right_f.pack(side=RIGHT, padx=5, pady=5)
    txt_f.pack(side=RIGHT, padx=5, pady=5)

    lbl_1.pack(side=TOP, padx=5, pady=5)
    lbl_2.pack(side=TOP, padx=5, pady=5)
    lbl_3.pack(side=TOP, padx=5, pady=5)
    lbl_4.pack(side=TOP, padx=5, pady=5)
    lbl_5.pack(side=TOP, padx=5, pady=5)
    lbl_6.pack(side=TOP, padx=5, pady=5, anchor=N)

    txt_1.pack(side=TOP, padx=5, pady=5)
    txt_2.pack(side=TOP, padx=5, pady=5)
    txt_3.pack(side=TOP, padx=5, pady=5)
    combo.pack(side=TOP, padx=5, pady=5)
    txt_4.pack(side=TOP, padx=5, pady=5)

    txt.pack(padx=5, pady=5)

    btn_del.pack(side=RIGHT, padx=5, pady=5, anchor=S)
    btn.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    tkinter.mainloop()
