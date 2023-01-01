import datetime
import sys
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
        ################
        self.fg_buttons = 'White'
        self.bg_buttons = "Black"
        self.size_buttons = 10
        self.font_buttons = 'Areil'



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
        # tk.Label(text=f" {parameter} for last 24 hours", fg="blue")
        self.label_static("parameter", win, 350, 0, f" {parameter} for last 24 hours")

        but=tk.Button(win, text="BACK", fg="Red",bd="White",command=lambda: self.first_screen(win))
        but.config(font=(f"{self.font_buttons}", self.size_buttons))
        but.pack()
        but.place(x=0, y=0)




    def first_screen(self,win):
        """ this function start our first windows view"""
        self.clean_screen_function(win)
        value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        # lable function
        self.label_static("temp", win, 60, 400, "Temperature")
        self.label_static("temprr", win, 450, 400, "Humidity")
        self.label_static("press", win, 800, 400, "Pressure")
        # labels units
        size_units=30
        level_units=540
        self.label_static("temp", win, 230, level_units, " C",size_units)
        self.label_static("temprr", win, 600, level_units, " %",size_units)
        self.label_static("press", win, 920, level_units, " hPa",size_units)
        # labels live values
        self.label_dynamic("press", win, 10, 500)
        self.label_dynamic("press4", win, 400, 500)
        self.label_dynamic("press4", win, 730, 500)

        # buttons ######################
        name_a = tk.Button(win, text="History Temperature", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Temp", win))
        name_a.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_a.pack()
        name_a.place(x=60, y=600)

        name_b = tk.Button(win, text="History Humidity", fg=self.fg_buttons, bg=self.bg_buttons, command=lambda: self.show_statistic("Temp",win))
        name_b.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_b.pack()
        name_b.place(x=450, y=600)

        name_c = tk.Button(win, text="History Humidity", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Temp", win))
        name_c.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_c.pack()
        name_c.place(x=800, y=600)

        # break button
        name_d = tk.Button(win, text="X", fg="Red", bg=self.bg_buttons,
                           command=lambda: self.terminate())
        name_d.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_d.pack()
        name_d.place(x=0, y=0)



        #self.button_1(win, 20, 20, "Temperature",self.show_statistic('Temp',win))
        # self.button("hum", win, 200, 300, "Hummidity",self.show_statistic('hum',win))
        #self.button("press", win, 200, 400, "Presure",self.show_statistic('Press',win))


        # my_label = Label(win, text=self.value, fg="White", bg="Red")
        # my_label.pack()
        #
        # def update_time():
        #     self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        #     my_label.config(text=self.value)
        #     my_label.after(300, update_time)
        # update_time()

    def label_static(self,name:str,win,x,y,text:str,size_text=15,font='Ariel', fg="White",bg="Black"):
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


    def label_dynamic(self,name:str,win,x,y, index=0,font='Ariel', size_text=60,fg="White",bg="Black"):
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

        name = Label(win, text=self.value, fg=fg, bg=bg,relief="groove", borderwidth=2,bd=0)
        name.config(font=(f"{font}", size_text),text=self.value)
        name.pack()
        name.place(x=x, y=y)

        # my_label = Label(win, text=self.value, fg="White", bg="Red")
        # my_label.pack()

        def update_time():
            #self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[1:] #sec
            name.config(text=self.value)
            name.after(300, update_time)

        update_time()






    def terminate(self):
        """
        terminate the program, have to add code 1234
        :return:
        """
        sys.exit()


    def release_windows(self,win):
        """
        :param win - cur windows
        this have to be last to show the screen
        :return:
        """
        win.mainloop()

