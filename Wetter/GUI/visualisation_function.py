import datetime
import tkinter as tk
from tkinter import *

# def clean_screen_function(win):
#     """ this function cleen the scree, when call it"""
#     for each in win.winfo_children():
#         each.destroy()

# def button_login(win):
#     pass

# def first_screen(win):
#     """ this function start our first windows view"""
#     clean_screen_function(win)
#     value=20
#     tk.Label(text=f" {value}", fg="Green", bg="Red").grid(row=30, column=30)
#
#     tk.Button(win, text="LOGIN", fg="blue", bg="green", command=lambda :button_login(win)).grid(row=0, column=0)
#     tk.Button(win, text="REGISTER", fg="blue", bg="green", command= lambda :button_login(win)).grid(row=0, column=1)

# window = tk.Tk()
# window.geometry("750x700")
# window.title("WETTER")
# first_screen(window)
# window.mainloop()

class GUI_VIS:
    def __init__(self,win):
        self.width=700
        self.height=700
        self.value=0



    def clean_screen_function(self,win):
        """
        cleen the screen
        :param win: current windows
        :return:
        """
        for each in win.winfo_children():
            each.destroy()

    def show_statistic(self,parameter,win):
        """

        :param parameter: what to be shown
        :param win: cur windows
        :return:
        """

        self.clean_screen_function(win)
        tk.Label(text=f" {parameter} for last 24 hours", fg="blue").grid(row=0, column=0)
        tk.Button(win, text="BACK", fg="Red",command=lambda: self.first_screen(win)).grid(row=0, column=2)




    def first_screen(self,win):
        """ this function start our first windows view"""
        self.clean_screen_function(win)
        value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        but=tk.Button(win, text="Weather", fg="blue", bg="green", command=lambda: self.show_statistic("Temp",win))
        but.pack()
        but.place(x=120, y=62)
        but_2=tk.Button(win, text="Hummidity", fg="blue", bg="green", command=lambda: self.show_statistic("Humm",win))
        but_3=tk.Button(win, text="Presure", fg="blue", bg="green", command=lambda: self.show_statistic("Pressure",win))
        but_2.pack()
        but_2.place(x=120, y=92)
        but_3.pack()
        but_3.place(x=120, y=122)

        my_label = Label(win, text=self.value, fg="White", bg="Red")
        my_label.pack()

        def update_time():
            self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            my_label.config(text=self.value)
            my_label.after(300, update_time)
        update_time()





    def release_windows(self,win):
        """
        :param win - cur windows
        this have to be last to show the screen
        :return:
        """
        win.mainloop()

