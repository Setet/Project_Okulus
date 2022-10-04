import tkinter
from tkinter import *

import sys

from lab1 import Lab_1_window
from lab2 import Lab_2_window
from lab3 import Lab_3_window


def Lab_4_window():
    window_lab_4 = tkinter.Tk()
    window_lab_4.wm_title("Лабораторная работа № 4")


def Lab_5_window():
    window_lab_5 = tkinter.Tk()
    window_lab_5.wm_title("Лабораторная работа № 5")


def Lab_6_window():
    window_lab_6 = tkinter.Tk()
    window_lab_6.wm_title("Лабораторная работа № 6")


def Lab_7_window():
    window_lab_7 = tkinter.Tk()
    window_lab_7.wm_title("Лабораторная работа № 7")


def Lab_8_window():
    window_lab_8 = tkinter.Tk()
    window_lab_8.wm_title("Лабораторная работа № 8")


def main():
    window = Tk()

    window.title("Окно выбора лабораторной работы")

    if sys.platform.startswith('win'):
        window.iconbitmap(r'pic/Pop_cat_closed.ico')
    else:
        window.iconbitmap(r'@pic/Pop_cat_closed.xbm')

    window.geometry('400x600')

    btn_lab1 = Button(window, text="Лабораторная работа № 1", foreground="white", background="#FF69B4",
                      command=Lab_1_window)
    btn_lab1.pack(fill=BOTH, side=TOP, expand=True)

    btn_lab2 = Button(window, text="Лабораторная работа № 2", foreground="white", background="#FF0000",
                      command=Lab_2_window)
    btn_lab2.pack(fill=BOTH, side=TOP, expand=True)

    btn_lab3 = Button(window, text="Лабораторная работа № 3", foreground="black", background="#FFA500",
                      command=Lab_3_window)
    btn_lab3.pack(fill=BOTH, side=TOP, expand=True)

    btn_lab4 = Button(window, text="Лабораторная работа № 4", foreground="black", background="#FFFF00")
    btn_lab4.pack(fill=BOTH, side=TOP, expand=True)

    btn_lab5 = Button(window, text="Лабораторная работа № 5", foreground="white", background="#008000")
    btn_lab5.pack(fill=BOTH, side=TOP, expand=True)

    btn_lab6 = Button(window, text="Лабораторная работа № 6", foreground="black", background="#00FFFF")
    btn_lab6.pack(fill=BOTH, side=TOP, expand=True)

    btn_lab7 = Button(window, text="Лабораторная работа № 7", foreground="white", background="#00008B")
    btn_lab7.pack(fill=BOTH, side=TOP, expand=True)

    btn_lab8 = Button(window, text="Лабораторная работа № 8", foreground="white", background="#800080")
    btn_lab8.pack(fill=BOTH, side=TOP, expand=True)

    window.mainloop()


if __name__ == '__main__':
    main()
