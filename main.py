import tkinter
import time
import sys

from tkinter import *
from tkinter import scrolledtext, messagebox
from tkinter.ttk import Combobox, Notebook, Style
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from Gradient import make_data_lab_1, funct_consider
from SLSQP import make_data_lab_2, kp
from Rosenbrock_function import make_data_lab_3, rosenbrock_2
from genetic_algorithm_l3 import GeneticAlgorithmL3
from pso import PSO
from bees import Bees


def main():
    window = Tk()

    if sys.platform.startswith('win'):
        window.iconbitmap(r'pic/Pop_cat_open.ico')
    else:
        window.iconbitmap(r'@pic/Pop_cat_open.xbm')

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    window.geometry("%dx%d" % (width, height))

    window.title("⠑⠎⠇⠊ ⠞⠮ ⠟⠊⠞⠁⠑⠱⠾ ⠪⠞⠕⠂ ⠞⠕ ⠞⠮ ⠁⠝⠊⠍⠑ ⠙⠑⠃⠊⠇⠖")

    fig = plt.figure(figsize=(14, 14))
    fig.add_subplot(projection='3d')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    sky = "#DCF0F2"
    yellow = "#F2C84B"

    style = Style()

    style.theme_create("dummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": sky},
            "map": {"background": [("selected", yellow)],
                    "expand": [("selected", [1, 1, 1, 0])]}}})

    style.theme_use("dummy")

    tab_control = Notebook(window)

    # Лаба 1

    def draw_lab_1():
        fig.clf()

        x, y, z = make_data_lab_1()

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        res_x = txt_1_tab_1.get()
        res_y = txt_2_tab_1.get()
        res_step = txt_3_tab_1.get()
        res_iterations = txt_4_tab_1.get()

        x_cs, y_cs, z_cs = funct_consider(float(res_x), float(res_y), float(res_step), int(res_iterations))

        for i in range(len(x_cs)):
            if i < (len(x_cs) - 1):
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s")
            else:
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")

            canvas.draw()
            txt_tab_1.insert(INSERT, f"{i}) ({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {z_cs[i]}\n")

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            window.update()
            delay = txt_5_tab_1.get()
            time.sleep(float(delay))
        messagebox.showinfo('Уведомление', 'Готово')

    def delete_lab_1():
        txt_tab_1.delete(1.0, END)

    tab_1 = Frame(tab_control)
    tab_control.add(tab_1, text="Lab_1")

    main_f_tab_1 = LabelFrame(tab_1, text="Параметры")
    left_f_tab_1 = Frame(main_f_tab_1)
    right_f_tab_1 = Frame(main_f_tab_1)
    txt_f_tab_1 = LabelFrame(tab_1, text="Консоль лог")

    lbl_1_tab_1 = Label(left_f_tab_1, text="X")
    lbl_2_tab_1 = Label(left_f_tab_1, text="Y")
    lbl_3_tab_1 = Label(left_f_tab_1, text="Начальный шаг")
    lbl_4_tab_1 = Label(left_f_tab_1, text="Число Итераций")
    lbl_5_tab_1 = Label(tab_1, text="Функция Химмельблау")
    lbl_6_tab_1 = Label(left_f_tab_1, text="Задержка в секундах")

    txt_1_tab_1 = Entry(right_f_tab_1)
    txt_2_tab_1 = Entry(right_f_tab_1)
    txt_3_tab_1 = Entry(right_f_tab_1)
    txt_4_tab_1 = Entry(right_f_tab_1)
    txt_5_tab_1 = Entry(right_f_tab_1)

    txt_tab_1 = scrolledtext.ScrolledText(txt_f_tab_1)
    btn_del_tab_1 = Button(tab_1, text="Очистить лог", command=delete_lab_1)
    btn_tab_1 = Button(tab_1, text="Выполнить", foreground="black", background="#00FFFF", command=draw_lab_1)

    lbl_5_tab_1.pack(side=TOP, padx=5, pady=5)
    main_f_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_1.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_1.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_6_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_1.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_1.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_1.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_1.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_1.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 2

    def draw_lab_2():
        fig.clf()

        x, y, z = make_data_lab_2()

        res_x = txt_1_tab_2.get()
        res_y = txt_2_tab_2.get()

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        x_cs = []
        y_cs = []
        z_cs = []

        for i, point in kp(res_x, res_y):
            x_cs.append(point[0])
            y_cs.append(point[1])
            z_cs.append(point[2])

        for i in range(len(x_cs)):
            if i < (len(x_cs) - 1):
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s")
            else:
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")

            txt_tab_2.insert(INSERT, f"{i}) ({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {round(z_cs[i], 4)}\n")
            canvas.draw()
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            window.update()
            delay = txt_3_tab_2.get()
            time.sleep(float(delay))
        messagebox.showinfo('Уведомление', 'Готово')

    def delete_lab_2():
        txt_tab_2.delete(1.0, END)

    tab_2 = Frame(tab_control)
    tab_control.add(tab_2, text="Lab_2")

    main_f_tab_2 = LabelFrame(tab_2, text="Параметры")
    left_f_tab_2 = Frame(main_f_tab_2)
    right_f_tab_2 = Frame(main_f_tab_2)
    txt_f_tab_2 = LabelFrame(tab_2, text="Консоль лог")

    lbl_1_tab_2 = Label(tab_2, text="Функция :\n2 * x1^2 + 3 * x2^2 + 4 * x1 * x2 - 6 * x1 - 3 * x2")
    lbl_2_tab_2 = Label(left_f_tab_2, text="X")
    lbl_3_tab_2 = Label(left_f_tab_2, text="Y")
    lbl_4_tab_2 = Label(left_f_tab_2, text="Задержка в секундах")

    txt_1_tab_2 = Entry(right_f_tab_2)
    txt_2_tab_2 = Entry(right_f_tab_2)
    txt_3_tab_2 = Entry(right_f_tab_2)

    txt_tab_2 = scrolledtext.ScrolledText(txt_f_tab_2)
    btn_del_tab_2 = Button(tab_2, text="Очистить лог", command=delete_lab_2)
    btn_tab_2 = Button(tab_2, text="Выполнить", foreground="black", background="#00FFFF", command=draw_lab_2)

    lbl_1_tab_2.pack(side=TOP, padx=5, pady=5)
    main_f_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_2.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_2.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_2_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_2.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_2.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_2.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_2.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_2.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 3

    def draw_lab_3():
        fig.clf()

        x, y, z = make_data_lab_3()

        pop_number = int(txt_1_tab_3.get())
        iter_number = int(txt_2_tab_3.get())
        survive = float(txt_3_tab_3.get())
        mutation = float(txt_4_tab_3.get())
        delay = txt_5_tab_3.get()

        if combo.get() == "Min":
            min_max = True
        else:
            min_max = False

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        genetic = GeneticAlgorithmL3(rosenbrock_2, iter_number, min_max, mutation, survive, pop_number)
        genetic.generate_start_population(5, 5)

        for j in range(pop_number):
            ax.scatter(genetic.population[j][0], genetic.population[j][1], genetic.population[j][2], c="black", s=1,
                       marker="s")
        if min_max:
            gen_stat = list(genetic.statistic()[1])
        else:
            gen_stat = list(genetic.statistic()[0])

        ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")
        canvas.draw()
        window.update()

        # Эти 4 строки ниже это считай удалить точку/точки
        fig.clf()
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        for i in range(50):
            for j in range(pop_number):  # Последовательность циклов и объекта genetic советую не менять
                ax.scatter(genetic.population[j][0], genetic.population[j][1], genetic.population[j][2], c="black", s=1,
                           marker="s")

            genetic.select()
            genetic.mutation(i)

            if min_max:
                gen_stat = list(genetic.statistic()[1])
            else:
                gen_stat = list(genetic.statistic()[0])

            ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")

            txt_tab_3.insert(INSERT,
                             f"{i}) ({round(gen_stat[1][0], 4)}) ({round(gen_stat[1][1], 4)}) = "
                             f" ({round(gen_stat[1][2], 4)})\n")

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection='3d')
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for j in range(pop_number):
            ax.scatter(genetic.population[j][0], genetic.population[j][1], genetic.population[j][2], c="black", s=1,
                       marker="s")
        if min_max:
            gen_stat = list(genetic.statistic()[1])
        else:
            gen_stat = list(genetic.statistic()[0])

        ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")

        canvas.draw()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        window.update()

        messagebox.showinfo('Уведомление', 'Готово')

    def delete_lab_3():
        txt_tab_3.delete(1.0, END)

    tab_3 = Frame(tab_control)
    tab_control.add(tab_3, text="Lab_3")

    main_f_tab_3 = LabelFrame(tab_3, text="Параметры")
    left_f_tab_3 = Frame(main_f_tab_3)
    right_f_tab_3 = Frame(main_f_tab_3)
    txt_f_tab_3 = LabelFrame(tab_3, text="Консоль лог")

    lbl_1_tab_3 = Label(left_f_tab_3, text="Размер популяции")
    lbl_2_tab_3 = Label(left_f_tab_3, text="Количество итераций")
    lbl_3_tab_3 = Label(left_f_tab_3, text="Выживаемость")
    lbl_7_tab_3 = Label(left_f_tab_3, text="Шанс мутации")
    lbl_4_tab_3 = Label(left_f_tab_3, text="Выбор точки поиска")
    lbl_5_tab_3 = Label(left_f_tab_3, text="Задержка в секундах")
    lbl_6_tab_3 = Label(tab_3, text="Функция Розенброка")

    txt_1_tab_3 = Entry(right_f_tab_3)
    txt_2_tab_3 = Entry(right_f_tab_3)
    txt_3_tab_3 = Entry(right_f_tab_3)
    txt_4_tab_3 = Entry(right_f_tab_3)
    txt_5_tab_3 = Entry(right_f_tab_3)

    combo = Combobox(right_f_tab_3)
    combo['values'] = ("Min", "Max")

    txt_tab_3 = scrolledtext.ScrolledText(txt_f_tab_3)
    btn_del_tab_3 = Button(tab_3, text="Очистить лог", command=delete_lab_3)
    btn_tab_3 = Button(tab_3, text="Выполнить", foreground="black", background="#00FFFF", command=draw_lab_3)

    lbl_6_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_3.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_3.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_7_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_5_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)  # задержка в секундах
    txt_5_tab_3.pack(side=TOP, padx=5, pady=5, fill=BOTH)  # шанс мутации
    combo.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_3.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_3.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_3.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_3.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 4

    def draw_lab_4():
        fig.clf()

        x, y, z = make_data_lab_3()

        iter_number = int(txt_1_tab_4.get())
        particle_number = int(txt_2_tab_4.get())
        fi_p = float(txt_4_tab_4.get())
        fi_g = float(txt_5_tab_4.get())
        delay = txt_6_tab_4.get()

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        pso_obj = PSO(rosenbrock_2, particle_number, 5.0, 5.0, fi_p, fi_g)

        for particle in pso_obj.particles:
            ax.scatter(particle[0], particle[1], particle[2], c="black", s=1, marker="s")

        ax.scatter(pso_obj.generation_best[0], pso_obj.generation_best[1], pso_obj.generation_best[2], c="red")
        canvas.draw()
        window.update()

        # Эти 4 строки ниже это считай удалить точку/точки
        fig.clf()
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        for i in range(iter_number):
            pso_obj.next_iteration()
            for particle in pso_obj.particles:
                ax.scatter(particle[0], particle[1], particle[2], c="black", s=1, marker="s")

            ax.scatter(pso_obj.generation_best[0], pso_obj.generation_best[1], pso_obj.generation_best[2], c="red")

            txt_tab_4.insert(INSERT,
                             f"{i + 1}) ({round(pso_obj.generation_best[0], 8)})"
                             f" ({round(pso_obj.generation_best[1], 8)}) = "
                             f" ({round(pso_obj.generation_best[2], 8)})\n")

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection='3d')
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for particle in pso_obj.particles:
            ax.scatter(particle[0], particle[1], particle[2], c="black", s=1, marker="s")

        ax.scatter(pso_obj.generation_best[0], pso_obj.generation_best[1], pso_obj.generation_best[2], c="red")

        canvas.draw()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        window.update()

        messagebox.showinfo('Уведомление', 'Готово')

    def delete_lab_4():
        txt_tab_4.delete(1.0, END)

    tab_4 = Frame(tab_control)
    tab_control.add(tab_4, text="Lab_4")

    main_f_tab_4 = LabelFrame(tab_4, text="Параметры")
    left_f_tab_4 = Frame(main_f_tab_4)
    right_f_tab_4 = Frame(main_f_tab_4)
    txt_f_tab_4 = LabelFrame(tab_4, text="Консоль лог")

    lbl_1_tab_4 = Label(left_f_tab_4, text="Количество итераций")
    lbl_2_tab_4 = Label(left_f_tab_4, text="Количество частиц")
    lbl_4_tab_4 = Label(left_f_tab_4, text="Коэффициент g")
    lbl_5_tab_4 = Label(left_f_tab_4, text="Задержка в секундах")
    lbl_6_tab_4 = Label(tab_4, text="Функция Розенброка")
    lbl_7_tab_4 = Label(left_f_tab_4, text="Коэффициент p")

    txt_1_tab_4 = Entry(right_f_tab_4)
    txt_2_tab_4 = Entry(right_f_tab_4)
    txt_4_tab_4 = Entry(right_f_tab_4)
    txt_5_tab_4 = Entry(right_f_tab_4)
    txt_6_tab_4 = Entry(right_f_tab_4)

    txt_tab_4 = scrolledtext.ScrolledText(txt_f_tab_4)
    btn_del_tab_4 = Button(tab_4, text="Очистить лог", command=delete_lab_4)
    btn_tab_4 = Button(tab_4, text="Выполнить", foreground="black", background="#00FFFF", command=draw_lab_4)

    lbl_6_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_4.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_4.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_7_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_5_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_6_tab_4.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_4.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_4.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_4.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_4.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 5

    def draw_lab_5():
        fig.clf()

        if combo.get() == "Химмельблау":
            print("1")
        elif combo.get() == "Розенброка":
            print("2")
        else:
            print("3")

        x, y, z = make_data_lab_3()

        iter_number = int(txt_1_tab_5.get())
        scouts_number = int(txt_2_tab_5.get())
        # elite = int(txt_3_tab_5.get())
        # perspective = int(txt_4_tab_5.get())
        # b_to_leet = txt_5_tab_5.get()
        # b_to_persp = txt_6_tab_5.get()
        delay = txt_7_tab_5.get()

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        bees_swarm = Bees(rosenbrock_2, scouts_number, 2, 3, 10, 8, 1, 5, 5)

        for scout in bees_swarm.scouts:
            ax.scatter(scout[0], scout[1], scout[2], c="blue", s=1, marker="s")

        bees_swarm.research_reports()
        bees_swarm.selected_search(1)

        for worker in bees_swarm.workers:
            ax.scatter(worker[0], worker[1], worker[2], c="black", s=1, marker="s")

        b = bees_swarm.get_best()
        ax.scatter(b[0], b[1], b[2], c="red")

        canvas.draw()
        window.update()

        fig.clf()
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        for i in range(iter_number):

            bees_swarm.send_scouts()
            for scout in bees_swarm.scouts:
                ax.scatter(scout[0], scout[1], scout[2], c="blue", s=1, marker="s")

            bees_swarm.research_reports()
            bees_swarm.selected_search(1 / (i + 1))

            for worker in bees_swarm.workers:
                ax.scatter(worker[0], worker[1], worker[2], c="black", s=1, marker="s")

            b = bees_swarm.get_best()
            ax.scatter(b[0], b[1], b[2], c="red")

            txt_tab_5.insert(INSERT,
                             f"{i + 1}) ({round(b[0], 8)})"
                             f" ({round(b[1], 8)}) = "
                             f" ({round(b[2], 8)})\n")

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection='3d')
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for scout in bees_swarm.scouts:
            ax.scatter(scout[0], scout[1], scout[2], c="blue", s=1, marker="s")

        for worker in bees_swarm.workers:
            ax.scatter(worker[0], worker[1], worker[2], c="black", s=1, marker="s")

        b = bees_swarm.get_best()
        ax.scatter(b[0], b[1], b[2], c="red")

        result_1 = [int(item) for item in txt_8_tab_5.get().split(",")]  # x
        result_2 = [int(item) for item in txt_9_tab_5.get().split(",")]  # y
        result_3 = [int(item) for item in txt_10_tab_5.get().split(",")]  # z

        result_1.append(result_1[0])
        result_2.append(result_2[0])
        result_3.append(result_3[0])

        ax.plot(result_1, result_2, result_3, label='parametric curve')

        canvas.draw()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        window.update()

        messagebox.showinfo('Уведомление', 'Готово')

    def delete_lab_5():
        txt_tab_5.delete(1.0, END)

    tab_5 = Frame(tab_control)
    tab_control.add(tab_5, text="Lab_5")

    main_f_tab_5 = LabelFrame(tab_5, text="Параметры")
    left_f_tab_5 = Frame(main_f_tab_5)
    right_f_tab_5 = Frame(main_f_tab_5)
    txt_f_tab_5 = LabelFrame(tab_5, text="Консоль лог")

    lbl_5_tab_5 = Label(tab_5, text="ХЗ")
    lbl_1_tab_5 = Label(left_f_tab_5, text="iter_number")
    lbl_2_tab_5 = Label(left_f_tab_5, text="scouts_number")
    lbl_3_tab_5 = Label(left_f_tab_5, text="elite")
    lbl_4_tab_5 = Label(left_f_tab_5, text="Задержка в секундах")
    lbl_6_tab_5 = Label(left_f_tab_5, text="perspective")
    lbl_7_tab_5 = Label(left_f_tab_5, text="Выборы 2022")
    lbl_8_tab_5 = Label(left_f_tab_5, text="b_to_leet")
    lbl_9_tab_5 = Label(left_f_tab_5, text="b_to_persp")

    lbl_10_tab_5 = Label(left_f_tab_5, text="X")
    lbl_11_tab_5 = Label(left_f_tab_5, text="Y")
    lbl_12_tab_5 = Label(left_f_tab_5, text="Z")

    txt_1_tab_5 = Entry(right_f_tab_5)
    txt_2_tab_5 = Entry(right_f_tab_5)
    txt_3_tab_5 = Entry(right_f_tab_5)
    txt_4_tab_5 = Entry(right_f_tab_5)
    txt_5_tab_5 = Entry(right_f_tab_5)
    txt_6_tab_5 = Entry(right_f_tab_5)
    txt_7_tab_5 = Entry(right_f_tab_5)

    txt_8_tab_5 = Entry(right_f_tab_5)
    txt_9_tab_5 = Entry(right_f_tab_5)
    txt_10_tab_5 = Entry(right_f_tab_5)

    combo = Combobox(right_f_tab_5)
    combo['values'] = ("Химмельблау", "Розенброка", "Растрыгина")

    txt_tab_5 = scrolledtext.ScrolledText(txt_f_tab_5)
    btn_del_tab_5 = Button(tab_5, text="Очистить лог", command=delete_lab_5)
    btn_tab_5 = Button(tab_5, text="Выполнить", foreground="black", background="#00FFFF", command=draw_lab_5)

    lbl_5_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_5.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_5.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_6_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_8_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_9_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    lbl_10_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_11_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_12_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    lbl_7_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_6_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_7_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_8_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_9_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_10_tab_5.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    combo.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_5.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_5.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_5.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_5.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 6

    def draw_lab_6():
        fig.clf()

        x, y, z = make_data_lab_3()

        pop_number = int(txt_1_tab_3.get())
        iter_number = int(txt_2_tab_3.get())
        survive = float(txt_3_tab_3.get())
        mutation = float(txt_4_tab_3.get())
        delay = txt_5_tab_3.get()

        if combo.get() == "Min":
            min_max = True
        else:
            min_max = False

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        genetic = GeneticAlgorithmL3(rosenbrock_2, iter_number, min_max, mutation, survive, pop_number)
        genetic.generate_start_population(5, 5)

        for j in range(pop_number):
            ax.scatter(genetic.population[j][0], genetic.population[j][1], genetic.population[j][2], c="black", s=1,
                       marker="s")
        if min_max:
            gen_stat = list(genetic.statistic()[1])
        else:
            gen_stat = list(genetic.statistic()[0])

        ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")
        canvas.draw()
        window.update()

        # Эти 4 строки ниже это считай удалить точку/точки
        fig.clf()
        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        for i in range(50):
            for j in range(pop_number):  # Последовательность циклов и объекта genetic советую не менять
                ax.scatter(genetic.population[j][0], genetic.population[j][1], genetic.population[j][2], c="black", s=1,
                           marker="s")

            genetic.select()
            genetic.mutation(i)

            if min_max:
                gen_stat = list(genetic.statistic()[1])
            else:
                gen_stat = list(genetic.statistic()[0])

            ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")

            txt_tab_3.insert(INSERT,
                             f"{i}) ({round(gen_stat[1][0], 4)}) ({round(gen_stat[1][1], 4)}) = "
                             f" ({round(gen_stat[1][2], 4)})\n")

            canvas.draw()
            window.update()
            time.sleep(float(delay))

            fig.clf()
            ax = fig.add_subplot(projection='3d')
            ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
            canvas.draw()

        for j in range(pop_number):
            ax.scatter(genetic.population[j][0], genetic.population[j][1], genetic.population[j][2], c="black", s=1,
                       marker="s")
        if min_max:
            gen_stat = list(genetic.statistic()[1])
        else:
            gen_stat = list(genetic.statistic()[0])

        ax.scatter(gen_stat[1][0], gen_stat[1][1], gen_stat[1][2], c="red")

        canvas.draw()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        window.update()

        messagebox.showinfo('Уведомление', 'Готово')

    def delete_lab_6():
        txt_tab_3.delete(1.0, END)

    tab_6 = Frame(tab_control)
    tab_control.add(tab_6, text="Lab_6")

    main_f_tab_6 = LabelFrame(tab_6, text="Параметры")
    left_f_tab_6 = Frame(main_f_tab_6)
    right_f_tab_6 = Frame(main_f_tab_6)
    txt_f_tab_6 = LabelFrame(tab_6, text="Консоль лог")

    lbl_1_tab_6 = Label(left_f_tab_6, text="Что-то 1")
    lbl_2_tab_6 = Label(left_f_tab_6, text="Что-то 2")
    lbl_3_tab_6 = Label(left_f_tab_6, text="Что-то 3")
    lbl_7_tab_6 = Label(left_f_tab_6, text="Что-то 4")
    lbl_4_tab_6 = Label(left_f_tab_6, text="Выбор")
    lbl_5_tab_6 = Label(left_f_tab_6, text="Задержка в секундах")
    lbl_6_tab_6 = Label(tab_6, text="ХЗ")

    txt_1_tab_6 = Entry(right_f_tab_6)
    txt_2_tab_6 = Entry(right_f_tab_6)
    txt_3_tab_6 = Entry(right_f_tab_6)
    txt_4_tab_6 = Entry(right_f_tab_6)
    txt_5_tab_6 = Entry(right_f_tab_6)

    combo = Combobox(right_f_tab_6)
    combo['values'] = ("1", "2", "3")

    txt_tab_6 = scrolledtext.ScrolledText(txt_f_tab_6)
    btn_del_tab_6 = Button(tab_6, text="Очистить лог", command=delete_lab_6)
    btn_tab_6 = Button(tab_6, text="Выполнить", foreground="black", background="#00FFFF", command=draw_lab_6)

    lbl_6_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    main_f_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH, expand=True)
    left_f_tab_6.pack(side=LEFT, fill=BOTH, expand=True)
    right_f_tab_6.pack(side=RIGHT, fill=BOTH, expand=True)

    lbl_1_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_2_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_3_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_7_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_5_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    lbl_4_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_1_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_2_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_3_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_4_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    txt_5_tab_6.pack(side=TOP, padx=5, pady=5, fill=BOTH)
    combo.pack(side=TOP, padx=5, pady=5, fill=BOTH)

    txt_tab_6.pack(padx=5, pady=5, fill=BOTH, expand=True)

    btn_tab_6.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    txt_f_tab_6.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)
    btn_del_tab_6.pack(side=BOTTOM, padx=5, pady=5, fill=BOTH, expand=True)

    # Лаба 7
    tab_7 = Frame(tab_control)
    tab_control.add(tab_7, text="Lab_7")

    # Лаба 8
    tab_8 = Frame(tab_control)
    tab_control.add(tab_8, text="Lab_8")

    tab_control.pack(side=RIGHT, fill=BOTH, expand=True)
    window.mainloop()


if __name__ == '__main__':
    main()
