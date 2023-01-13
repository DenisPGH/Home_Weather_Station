import datetime
import os
import sys
import tkinter as tk
from tkinter import *
from matplotlib import ticker
import matplotlib.dates as mdates
import numpy as np


from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

from day_info_function import Ortodox
from sensor_function import Sensor
from sqlite_db__function import SQLiteSensor
from statistic_function import History
from wetter_outside_function import Outside
from paths import USER, USER_CLIENT


class GUI_VIS:
    def __init__(self,win):
        self.width=700
        self.height=700
        self.value=0
        self.datetime_=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.DAY= datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
        self.SECONDS= datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[2]
        self.yesterday=datetime.datetime.today()-datetime.timedelta(days=1) # '2011-01-01'
        self.YESTERDAY=self.yesterday.strftime('%Y-%m-%d %H:%M:%S').split(" ")[0] # '2011-01-01'
        self.CURRENT_HOUR = datetime.datetime.today().strftime('%H')
        ################
        self.fg_buttons = 'White'
        self.bg_buttons = "Black"
        self.size_buttons = 17
        self.font_buttons = 'Areil'
        #self.history=History()
        self.history=SQLiteSensor()
        self.value_unit={'temperature': "C",'pressure': 'hPa', 'humidity': "%"}
        self.outside=Outside()
        self.sensor=Sensor()
        self.interval_refresh_page=10000 #4000
        self.orthodox=Ortodox()
        ###################
        self.VIDEO_ON=False
        self.VIDEO_TEXT = 'Video'
        self.FG = 'White'
        self.VIDEO_BG = 'Green'
        self.VIDEO_SIZE_FONT = 10
        self.VIDEO_TEXT_FG='White'
        self.VIDEO_STOPPED_STRING='Stopped!'
        self.VIDEO_ON_STRING='Recording...'
        self.VIDEO_MODUS=self.VIDEO_STOPPED_STRING

        self.dinamic_value_function={1: self.sensor.reading()[0],
                                     2: self.sensor.reading()[1],
                                     3: self.sensor.reading()[2],
                                     4: datetime.datetime.today().strftime('%d-%m-%Y    %H:%M'),
                                     5: self.outside.acctual_temperature_outside(),
                                     6: self.orthodox.current_day_ortodox(),
                                     }
        ####
        self.FS_LEVEL_UNITS=370
        self.FS_LEVEL_VALUES=350
        self.FS_LEVEL_TABLES=300
        self.FS_LEVEL_BUTTONS=440



    def back_button(self,win):

        # BACK BUTTON to first screen
        but = tk.Button(win, text="BACK", fg="Red", bg='Black', command=lambda: self.first_screen(win))
        but.config(font=(f"{self.font_buttons}", self.size_buttons))
        but.pack()
        but.place(x=0, y=0)



    def clean_screen_function(self,win):
        """
        cleen the screen
        :param win: current windows
        :return:
        """
        for each in win.winfo_children():
            each.destroy()

    def show_statistic(self,parameter,win,period=1):
        """

        :param parameter: 'Temperature','Humidity','Pressure'
        :param win: cur windows
        :return:
        """

        self.clean_screen_function(win)
        # tk.Label(text=f" {parameter} for last 24 hours", fg="blue")
        self.label_static("parameter", win, 270, 430, f" {parameter} for the {self.DAY}")

        # BUTTONS
        level_buttons = 430
        name_a = tk.Button(win, text="One day", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic(parameter,win,1))
        name_a.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_a.pack()
        name_a.place(x=0, y=50)

        name_b = tk.Button(win, text="7 days", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic(parameter,win,7))
        name_b.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_b.pack()
        name_b.place(x=0, y=100)


        self.back_button(win)
        self.plot_me(win, parameter.lower(), period)


    def first_screen(self,win):
        """ this function start our first windows view 800x480"""
        self.clean_screen_function(win)
        #value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        # lable function
        self.label_static("temp", win, 60, self.FS_LEVEL_TABLES, "Temperature Inside :")
        self.label_static("temprr", win, 350, self.FS_LEVEL_TABLES, "Humidity :")
        self.label_static("press", win, 600, self.FS_LEVEL_TABLES, "Pressure :")
        self.label_static("tem_outside", win, 50, 100, "Temperature Outside :")

        # labels live values ####################################################

        size_double=65
        self.label_dynamic("press", win, 65, self.FS_LEVEL_VALUES, 1, size_double) #temp
        self.label_dynamic("press4", win, 355, self.FS_LEVEL_VALUES, 2, size_double) #humidity
        self.label_dynamic("press4", win, 600, self.FS_LEVEL_VALUES, 3) # pressure
        self.label_dynamic("press5", win, 0, 0,4,50) # time
        self.label_dynamic("press6", win, 65, 180,5,size_double) # temp
        self.label_dynamic("press7", win, 380, 200,6,20) # Nameday
        self.label_dynamic("press8", win, 600, 100,7,12) # Video mode

        # labels units ########################################################
        size_units = 20
        self.label_static("temp", win, 170, self.FS_LEVEL_UNITS, " C", size_units)
        self.label_static("temprr", win, 470, self.FS_LEVEL_UNITS, " %", size_units)
        self.label_static("press", win, 740, self.FS_LEVEL_UNITS, " hPa", size_units)
        self.label_static("tem_out", win, 170, 200, " C", size_units)

        # buttons ######################
        level_buttons=440
        name_a = tk.Button(win, text="History Temperature", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Temperature", win))
        name_a.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_a.pack()
        name_a.place(x=30, y=self.FS_LEVEL_BUTTONS)

        name_b = tk.Button(win, text="History Humidity", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Humidity",win))
        name_b.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_b.pack()
        name_b.place(x=320, y=self.FS_LEVEL_BUTTONS)

        name_c = tk.Button(win, text="History Pressure", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Pressure", win))
        name_c.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_c.pack()
        name_c.place(x=570, y=self.FS_LEVEL_BUTTONS)

        # break button
        name_d = tk.Button(win, text="X", fg="Red", bg=self.bg_buttons,
                           command=lambda: self.terminate())
        name_d.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_d.pack()
        name_d.place(x=770, y=0)

        ## video button
        self.video_button(win)

        ## shutdown button
        self.shutdown_button(win)






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
            if 0< index<= 6:
                self.value = self.dinamic_value_function[index]
            elif index==6: # Nameday
                text_=self.orthodox.current_day_ortodox()
                if text_ !="":
                    self.value = f"Днес:  {text_}"
                else:
                    self.value = f"  "
            elif index == 7:
                self.value=self.VIDEO_MODUS
                self.VIDEO_BG='Red' if self.VIDEO_ON == True else 'Green'
                self.VIDEO_TEXT='Stop video' if self.VIDEO_ON == True else 'Play video'


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

    def plot_me(self, win, parameter, period):
        """
        this control the graphical windows in the tkinter page

        :param win: windows
        :param parameter: 'temperature','humidity','pressure'
        :param today: todays date
        :return:
        """


        # the figure that will contain the plot
        fig_color=0.01
        fig = Figure(figsize=(7, 5), dpi=80)
        fig.patch.set_facecolor((fig_color, fig_color, fig_color))


        # list of squares
        #ys, xs = self.history.values_for_a_period(parameter,period)
        xs,ys = self.history.return_info_for_period(parameter,period)
        plot1 = fig.add_subplot(111) # fig.patch.set_facecolor('xkcd:mint green')
        plot1.grid(color=((0.15,0.15,0.15)))
        plot1.set_facecolor((fig_color, fig_color, fig_color))
        plot1.plot(xs, ys, 'g',linewidth=4)
        #################

        word_day='day' if period==1 else 'days'
        plot1.set_xlabel(f'{period} {word_day}',fontsize=20,color='White') # xaxis.label.set_color('red')
        plot1.set_ylabel(f'{parameter}',fontsize=20,color='White')
        # set first and last
        plot1.set_xticks([plot1.get_xticks()[0],plot1.get_xticks()[-1]],[f'{plot1.get_xticklabels()[0].get_text()}',plot1.get_xticklabels()[-1]])
        plot1.tick_params(axis='x', colors='white',rotation=0,labelsize=15)
        plot1.tick_params(axis='y', colors='white')


        # print(plot1.get_xticks())
        # plot1.set_xticks([3],['now'])
        # labels = [item.get_text().split(" ")[1].split(":")[0] for item in plot1.get_xticklabels()]
        # plot1.set_xticklabels(labels)
        # plot1.set_xticklabels(FormatStrFormatter('').format_ticks(labels))
        # plot1.xaxis.set_major_formatter(mdates.DateFormatter(' %m:%d'))
        # start, end = plot1.get_xlim()
        # plot1.set_xticks(plot1.get_xticks()[-1::100])

        # plot1.xaxis.set_ticks(np.arange(start, end, 2))

        # plot1.xaxis.set_major_formatter(ticker.StrMethodFormatter('.')) # StrMethodFormatter('*')

        """ LABEL here"""
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


    def video_button(self,win):

        name_e = tk.Button(win, text=f"{self.VIDEO_TEXT}",
                           fg=f"{self.VIDEO_TEXT_FG}",
                           bg=f"{self.VIDEO_BG}",

                           command=lambda: self.video_screen(win))
        name_e.config(font=(f"{self.font_buttons}", self.VIDEO_SIZE_FONT))
        name_e.pack()
        name_e.place(x=500, y=100)

    def video_play_function(self,win):
        print('palyed')


    def video_screen(self, win):
        """
        work but not change the color
        :param win:
        :return:
        """

        # self.clean_screen_function(win)
        # self.back_button(win)
        # self.label_static("video", win, 400, 0, "VIDEO: ", 30)
        # video_play = tk.Button(win, text=f"Play Video",
        #                    fg=f"White",
        #                    bg=f"Black",
        #
        #                    command=lambda: self.video_play_function(win))
        # video_play.config(font=(f"{self.font_buttons}", 20))
        # video_play.pack()
        # video_play.place(x=620, y=10)

        if self.VIDEO_ON == False:
            self.VIDEO_ON = True
        elif self.VIDEO_ON == True:
            self.VIDEO_ON = False

        self.VIDEO_MODUS = self.VIDEO_ON_STRING if self.VIDEO_ON == True else self.VIDEO_STOPPED_STRING
        command = 'sudo systemctl start video.service' if self.VIDEO_ON == True else 'sudo systemctl stop video.service'
        print(f"{command}")
        if USER == USER_CLIENT:
            os.system(command)
        self.first_screen(win)


    def shut_down(self,win):
        """
        just shut down the raspi
        """
        self.clean_screen_function(win)
        self.label_static("byebye",win,300,200,"Bye-Bye",70)


        shut_down='sudo shutdown'
        print('shutdown')
        if USER=='raspi':
            os.system(shut_down)


    def shutdown_button(self,win):
        shutdown_size=13
        name_shutdown = tk.Button(win, text="Shtd", fg="Red", bg=self.bg_buttons,
                           command=lambda: self.shut_down(win))
        name_shutdown.config(font=(f"{self.font_buttons}", shutdown_size))
        name_shutdown.pack()
        name_shutdown.place(x=750, y=60)




