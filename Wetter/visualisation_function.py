import datetime
import sys
import tkinter as tk
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

from day_info_function import Ortodox
from sensor_function import Sensor
from statistic_function import History
from wetter_outside_function import Outside


class GUI_VIS:
    def __init__(self,win):
        self.width=700
        self.height=700
        self.value=0
        self.DAY= datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
        self.SECONDS= datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[2]
        self.yesterday=datetime.datetime.today()-datetime.timedelta(days=1) # '2011-01-01'
        self.YESTERDAY=self.yesterday.strftime('%Y-%m-%d %H:%M:%S').split(" ")[0] # '2011-01-01'
        self.CURRENT_HOUR = datetime.datetime.today().strftime('%H')
        ################
        self.fg_buttons = 'White'
        self.bg_buttons = "Black"
        self.size_buttons = 10
        self.font_buttons = 'Areil'
        self.history=History()
        self.value_unit={'temperature': "C",'pressure': 'hPa', 'humidity': "%"}
        self.outside=Outside()
        self.sensor=Sensor()
        self.interval_refresh_page=2000
        self.orthodox=Ortodox()


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

        :param parameter: 'Temperature','Humidity','Pressure'
        :param win: cur windows
        :return:
        """

        self.clean_screen_function(win)
        # tk.Label(text=f" {parameter} for last 24 hours", fg="blue")
        self.label_static("parameter", win, 270, 430, f" {parameter} for the {self.DAY}")

        but=tk.Button(win, text="BACK", fg="Red",bg='Black',command=lambda: self.first_screen(win))
        but.config(font=(f"{self.font_buttons}", self.size_buttons))
        but.pack()
        but.place(x=0, y=0)
        self.plot_me(win, parameter.lower(), self.DAY,self.YESTERDAY)


    def first_screen(self,win):
        """ this function start our first windows view 800x480"""
        self.clean_screen_function(win)
        value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        # lable function
        level_tables=300
        self.label_static("temp", win, 60, level_tables, "Temperature :")
        self.label_static("temprr", win, 350, level_tables, "Humidity :")
        self.label_static("press", win, 600, level_tables, "Pressure :")
        self.label_static("tem_outside", win, 50, 100, "Temperature Outside :")

        # labels live values ####################################################
        level_values=350
        size_double=50
        self.label_dynamic("press", win, 65, level_values,1,size_double) #temp
        self.label_dynamic("press4", win, 355, level_values,2,size_double) #humidity
        self.label_dynamic("press4", win, 600, level_values,3) # pressure
        self.label_dynamic("press5", win, 180, 0,4) # time
        self.label_dynamic("press6", win, 65, 180,5,size_double) # temp
        self.label_dynamic("press7", win, 400, 100,6,20) # Nameday

        # labels units ########################################################
        size_units = 20
        level_units = 370
        self.label_static("temp", win, 150, level_units, " C", size_units)
        self.label_static("temprr", win, 430, level_units, " %", size_units)
        self.label_static("press", win, 730, level_units, " hPa", size_units)
        self.label_static("tem_out", win, 150, 200, " C", size_units)

        # buttons ######################
        level_buttons=440
        name_a = tk.Button(win, text="History Temperature", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Temperature", win))
        name_a.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_a.pack()
        name_a.place(x=60, y=level_buttons)

        name_b = tk.Button(win, text="History Humidity", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Humidity",win))
        name_b.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_b.pack()
        name_b.place(x=350, y=level_buttons)

        name_c = tk.Button(win, text="History Pressure", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Pressure", win))
        name_c.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_c.pack()
        name_c.place(x=600, y=level_buttons)

        # break button
        name_d = tk.Button(win, text="X", fg="Red", bg=self.bg_buttons,
                           command=lambda: self.terminate())
        name_d.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_d.pack()
        name_d.place(x=770, y=0)



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


    def label_dynamic(self,name:str,win,x,y, index=0,size_text=40,font='Ariel', fg="White",bg="Black"):
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

        def update_time():
            """
            have to change here the source information from the sensor

            :return: new value of the index 1=Temp, 2=hum, 3=Presure, 4=time
            """
            if index==1: # temperature
                #self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[2]  # sec
                self.value =self.sensor.reading()[0]
            elif index==2: # humidity
                #self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[2]  # sec
                self.value = self.sensor.reading()[1]
            elif index==3: # pressure
                #self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[1:]  # sec
                self.value = self.sensor.reading()[2]
            elif index==4: # time
                self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M')
            elif index==5: # temperature outside
                #self.value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[2]  # sec
                self.value = self.outside.acctual_temperature_outside()
            elif index==6: # Nameday
                text_=self.orthodox.current_day_ortodox()
                if text_ !="":
                    self.value = f"Днес:  {text_}"
                else:
                    self.value = f" Schön dass du da bist!!!"


            name.config(text=self.value)
            name.after(self.interval_refresh_page, update_time)

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

    def plot_me(self, win, parameter, today, yesterday):
        """
        this control the graphical windows in the tkinter page

        :param win: windows
        :param parameter: 'temperature','humidity','pressure'
        :param today: todays date
        :return:
        """


        # the figure that will contain the plot
        fig_color=0.01
        fig = Figure(figsize=(8.5, 5), dpi=80)
        fig.patch.set_facecolor((fig_color, fig_color, fig_color))


        # list of squares
        ys, xs = self.history.get_values(parameter, today,yesterday,self.CURRENT_HOUR)
        plot1 = fig.add_subplot(111) # fig.patch.set_facecolor('xkcd:mint green')
        plot1.grid(color=((0.15,0.15,0.15)))
        plot1.set_facecolor((fig_color, fig_color, fig_color))
        plot1.plot(xs, ys, 'g',linewidth=3)
        #################
        plot1.set_xlabel('Hours',fontsize=20,color='White') # xaxis.label.set_color('red')
        plot1.set_ylabel(f'{parameter}',fontsize=20,color='White')
        plot1.tick_params(axis='x', colors='white')
        plot1.tick_params(axis='y', colors='white')
        ## label here down ###############################
        # for x, y in zip(xs, ys):
        #     #label = "{:.2f}".format(y)
        #     label = f"{y:.2f} {self.value_unit[parameter]}"
        #
        #     plot1.annotate(label,  # this is the text
        #                  (x, y),  # these are the coordinates to position the label
        #                  textcoords="offset points",  # how to position the text
        #                  xytext=(0, 10),  # distance from text to points (x,y)
        #                  ha='center')  # horizontal alignment can be left, right or cente


        canvas = FigureCanvasTkAgg(fig,master=win)
        canvas.draw()
        canvas.get_tk_widget().pack()


