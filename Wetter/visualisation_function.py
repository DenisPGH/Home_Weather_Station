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
                                     5: self.outside.acctual_temperature_outside()[0],
                                     6: self.outside.acctual_temperature_outside()[1],
                                     7: self.outside.acctual_temperature_outside()[2],

                                     }
        ####
        #values
        self.FS_VALUE_SIZE=65
        self.FS_LEVEL_VALUES=350
        self.FS_VALUE_X_TEMP = 65
        self.FS_VALUE_X_HUM = 355
        self.FS_VALUE_X_PRESS = 600
        self.FS_VALUE_X_TEMP_OUTSIDE = 380
        self.FS_VALUE_Y_TEMP_OUTSIDE = 200
        self.FS_VALUE_X_TIME = 0
        self.FS_VALUE_Y_TIME = 0
        self.FS_SIZE_VALUE_TIME = 50

        self.FS_VALUE_X_NAMEDAY = 380
        self.FS_VALUE_Y_NAMEDAY = 200
        self.FS_SIZE_VALUE_NAMEDAY =20

        self.FS_VALUE_X_NAMEDAY = 0
        self.FS_VALUE_Y_NAMEDAY = 100
        self.FS_SIZE_VALUE_NAMEDAY = 20

        self.FS_VALUE_X_VIDEO_MODE = 600
        self.FS_VALUE_Y_VIDEO_MODE = 100
        self.FS_SIZE_VALUE_VIDEO_MODE = 12

        self.FS_VALUE_X_WETTER_STATUS = 380
        self.FS_VALUE_Y_WETTER_STATUS = 175
        self.FS_SIZE_VALUE_WETTER_STATUS = 16

        self.FS_VALUE_X_PRESSURE_OUTSIDE = 600
        self.FS_VALUE_Y_PRESSURE_OUTSIDE = 230
        self.FS_SIZE_VALUE_PRESSURE_OUTSIDE = 20


        self.FS_VIDEO_BUTTON_X=500
        self.FS_VIDEO_BUTTON_Y=100
        # table
        self.FS_LEVEL_TABLES = 320
        self.FS_TABLE_X_TEMP=60
        self.FS_TABLE_X_HUM=350
        self.FS_TABLE_X_PRESS=600
        self.FS_TABLE_X_TEMP_OUTSIDE=345
        self.FS_TABLE_Y_TEMP_OUTSIDE=150
        self.FS_TABLE_X_PRESS_OUTSIDE=600
        self.FS_TABLE_Y_PRESS_OUTSIDE=200
        #units
        self.FS_SIZE_UNITS=20
        self.FS_LEVEL_UNITS = 370
        self.FS_UNITS_X_TEMP = 170
        self.FS_UNITS_X_HUM = 470
        self.FS_UNITS_X_PRESS = 720
        self.FS_UNITS_X_TEMP_OUTSIDE = 470
        self.FS_UNITS_Y_TEMP_OUTSIDE = 240

        self.FS_UNITS_X_PRESSURE_OUTSIDE = 720
        self.FS_UNITS_Y_PRESSURE_OUTSIDE = 250
        #buttons
        self.FS_LEVEL_BUTTONS = 440
        self.FS_BUTTON_X_HISTORY_TEMP = 30
        self.FS_BUTTON_X_HISTORY_HUM = 320
        self.FS_BUTTON_X_HISTORY_PRESS = 570
        self.FS_BUTTON_X_BREAK = 770
        self.FS_BUTTON_Y_BREAK = 0

        self.FS_BUTTON_X_SHUTDOWN = 750
        self.FS_BUTTON_Y_SHUTDOWN = 60
        self.FS_SHUTDOWN_SIZE=13






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
        self.label_static("temp", win, self.FS_TABLE_X_TEMP, self.FS_LEVEL_TABLES, "Temperature Inside :")
        self.label_static("temprr", win, self.FS_TABLE_X_HUM, self.FS_LEVEL_TABLES, "Humidity Inside:")
        self.label_static("press", win, self.FS_TABLE_X_PRESS, self.FS_LEVEL_TABLES, "Pressure Inside:")
        self.label_static("tem_outside", win, self.FS_TABLE_X_TEMP_OUTSIDE, self.FS_TABLE_Y_TEMP_OUTSIDE, "Temperature Outside :")
        self.label_static("press_outside", win, self.FS_TABLE_X_PRESS_OUTSIDE, self.FS_TABLE_Y_PRESS_OUTSIDE, "Pressure Outside :")

        # labels live values ####################################################
        self.label_dynamic("press", win, self.FS_VALUE_X_TEMP, self.FS_LEVEL_VALUES, 1, self.FS_VALUE_SIZE) #temp
        self.label_dynamic("press4", win, self.FS_VALUE_X_HUM, self.FS_LEVEL_VALUES, 2, self.FS_VALUE_SIZE) #humidity
        self.label_dynamic("press4", win, self.FS_VALUE_X_PRESS, self.FS_LEVEL_VALUES, 3) # pressure
        self.label_dynamic("press5", win, self.FS_VALUE_X_TIME, self.FS_VALUE_Y_TIME,4,self.FS_SIZE_VALUE_TIME) # time
        self.label_dynamic("press6", win, self.FS_VALUE_X_TEMP_OUTSIDE, self.FS_VALUE_Y_TEMP_OUTSIDE,5,self.FS_VALUE_SIZE) # temp out
        self.label_dynamic("press7", win, self.FS_VALUE_X_NAMEDAY, self.FS_VALUE_Y_NAMEDAY,99,self.FS_SIZE_VALUE_NAMEDAY) # Nameday
        self.label_dynamic("press8", win,self.FS_VALUE_X_VIDEO_MODE, self.FS_VALUE_Y_VIDEO_MODE,100,self.FS_SIZE_VALUE_VIDEO_MODE) # Video mode
        self.label_dynamic("press9", win,self.FS_VALUE_X_WETTER_STATUS, self.FS_VALUE_Y_WETTER_STATUS,6,self.FS_SIZE_VALUE_WETTER_STATUS,"Calibri") # wetter status
        self.label_dynamic("press9", win,self.FS_VALUE_X_PRESSURE_OUTSIDE, self.FS_VALUE_Y_PRESSURE_OUTSIDE,7) # presure outside

        # labels units ########################################################
        self.label_static("temp", win, self.FS_UNITS_X_TEMP, self.FS_LEVEL_UNITS, " C", self.FS_SIZE_UNITS)
        self.label_static("temprr", win, self.FS_UNITS_X_HUM, self.FS_LEVEL_UNITS, " %", self.FS_SIZE_UNITS)
        self.label_static("press", win, self.FS_UNITS_X_PRESS, self.FS_LEVEL_UNITS, " hPa", self.FS_SIZE_UNITS)
        self.label_static("tem_out", win, self.FS_UNITS_X_TEMP_OUTSIDE, self.FS_UNITS_Y_TEMP_OUTSIDE, " C", self.FS_SIZE_UNITS)
        self.label_static("pressure_out", win, self.FS_UNITS_X_PRESSURE_OUTSIDE, self.FS_UNITS_Y_PRESSURE_OUTSIDE, " hPa", self.FS_SIZE_UNITS)

        # buttons ######################
        name_a = tk.Button(win, text="History Temperature", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Temperature", win))
        name_a.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_a.pack()
        name_a.place(x=self.FS_BUTTON_X_HISTORY_TEMP, y=self.FS_LEVEL_BUTTONS)

        name_b = tk.Button(win, text="History Humidity", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Humidity",win))
        name_b.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_b.pack()
        name_b.place(x=self.FS_BUTTON_X_HISTORY_HUM, y=self.FS_LEVEL_BUTTONS)

        name_c = tk.Button(win, text="History Pressure", fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Pressure", win))
        name_c.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_c.pack()
        name_c.place(x=self.FS_BUTTON_X_HISTORY_PRESS, y=self.FS_LEVEL_BUTTONS)

        # break button
        name_d = tk.Button(win, text="X", fg="Red", bg=self.bg_buttons,
                           command=lambda: self.terminate())
        name_d.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_d.pack()
        name_d.place(x=self.FS_BUTTON_X_BREAK, y=self.FS_BUTTON_Y_BREAK)

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
            if 0< index <= len(self.dinamic_value_function):
                self.value = self.dinamic_value_function[index]
            elif index==99: # Nameday
                text_=self.orthodox.current_day_ortodox()
                if text_ !="":
                    self.value = f"Днес:  {text_}"
                else:
                    self.value = f" DENISLAV PETROV "
            elif index == 100:
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
        name_e.place(x=self.FS_VIDEO_BUTTON_X, y=self.FS_VIDEO_BUTTON_Y)

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
        name_shutdown = tk.Button(win, text="Shtd", fg="Red", bg=self.bg_buttons,
                           command=lambda: self.shut_down(win))
        name_shutdown.config(font=(f"{self.font_buttons}", self.FS_SHUTDOWN_SIZE))
        name_shutdown.pack()
        name_shutdown.place(x=self.FS_BUTTON_X_SHUTDOWN, y=self.FS_BUTTON_Y_SHUTDOWN)




