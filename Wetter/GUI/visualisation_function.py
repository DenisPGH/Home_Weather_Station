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
        tk.Label(text=f" {parameter} for last 24 hours", fg="blue")
        tk.Button(win, text="BACK", fg="Red",command=lambda: self.first_screen(win))




    def first_screen(self,win):
        """ this function start our first windows view"""
        self.clean_screen_function(win)
        value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.label_static("temp", win, 50, 200, "Temperature")
        self.label_static("temprr", win, 50, 300, "Humidity")
        self.label_static("press", win, 50, 400, "Pressure")

        #self.button_1(win, 20, 20, "Temperature",self.show_statistic('Temp',win))
        # self.button("hum", win, 200, 300, "Hummidity",self.show_statistic('hum',win))
        #self.button("press", win, 200, 400, "Presure",self.show_statistic('Press',win))


        my_label = Label(win, text=self.value, fg="White", bg="Red")
        my_label.pack()

        def update_time():
            self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            my_label.config(text=self.value)
            my_label.after(300, update_time)
        update_time()

    def label_static(self,name:str,win,x,y,text:str,font='Ariel', size_text=15,fg="Black",bg="White"):
        """
        :param font: font of the text
        :param size_text: size of the text
        :param name: name of the label
        :param win: windows
        :param x: coord of x
        :param y: of y
        :param text: what shoud be shown
        :param fg: color of the text
        :param bg: beckground color
        :return: nothing
        """
        # border= "flat", "raised", "sunken", "ridge", "solid", and "groove".

        name = Label(win, text=text, fg=fg, bg=bg,relief="groove", borderwidth=2,bd=0)
        name.config(font=(f"{font}", size_text))
        name.pack()
        name.place(x=x, y=y)

    def button(self,name_b:str,win,x,y,text:str,function,font='Ariel', size_text=10,fg="Black",bg="Green"):
        """
        :param function: what shoud it do
        :param font: font of the text
        :param size_text: size of the text
        :param name: name of the label
        :param win: windows
        :param x: coord of x
        :param y: of y
        :param text: what shoud be shown
        :param fg: color of the text
        :param bg: beckground color
        :return: nothing
        """
        # border= "flat", "raised", "sunken", "ridge", "solid", and "groove".

        name_b = tk.Button(win, text=text, fg=fg, bg=bg, command=lambda: function)
        name_b.config(font=(f"{font}", size_text))
        name_b.pack()
        name_b.place(x=x, y=y)

    def button_1(self,win,x,y,text:str,function,font='Ariel', size_text=10,fg="Black",bg="Green"):
        """
        :param function: what shoud it do
        :param font: font of the text
        :param size_text: size of the text
        :param name: name of the label
        :param win: windows
        :param x: coord of x
        :param y: of y
        :param text: what shoud be shown
        :param fg: color of the text
        :param bg: beckground color
        :return: nothing
        """
        # border= "flat", "raised", "sunken", "ridge", "solid", and "groove".

        name_1 = tk.Button(win, text=text, fg=fg, bg=bg, command=lambda: function)
        name_1.config(font=(f"{font}", size_text))
        name_1.pack()
        name_1.place(x=x, y=y)









    def release_windows(self,win):
        """
        :param win - cur windows
        this have to be last to show the screen
        :return:
        """
        win.mainloop()

