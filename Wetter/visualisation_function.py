import datetime
import os
import sys
import tkinter as tk
from tkinter import *

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)

from cpu_monitoring_function import MonitoringCPU
from day_info_function import Ortodox
from switch_function import Switch_helper
from sensor_function import Sensor
from sqlite_db__function import SQLiteSensor

from wetter_outside_function import Outside
from paths import USER, USER_CLIENT

from variables_function import Variables


class GUI_VIS(Variables):
    def __init__(self,win):
        super().__init__()
        self.history = SQLiteSensor()
        self.my_switch = Switch_helper()
        self.outside = Outside()
        self.sensor = Sensor()
        self.orthodox = Ortodox()
        self.cpu_raspi=MonitoringCPU()
        self.datetime_=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        self.DAY= datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
        self.SECONDS= datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")[2]
        self.yesterday=datetime.datetime.today()-datetime.timedelta(days=1) # '2011-01-01'
        self.YESTERDAY=self.yesterday.strftime('%Y-%m-%d %H:%M:%S').split(" ")[0] # '2011-01-01'
        self.CURRENT_HOUR = datetime.datetime.today().strftime('%H')



    def back_button(self,win):

        # BACK BUTTON to first screen
        but = tk.Button(win, text=self.STRING_BUTTON_BACK, fg="Red", bg='Black', command=lambda: self.first_screen(win))
        but.config(font=(f"{self.font_buttons}", self.size_buttons))
        but.pack()
        but.place(x=self.FS_BUTTON_X_BACK, y=self.FS_BUTTON_Y_BACK)



    def clean_screen_function(self,win):
        """
        cleen the screen
        :param win: current windows
        :return:
        """
        for each in win.winfo_children():
            each.destroy()

    def show_statistic(self,parameter,win,table,period=1):
        """
        :param table: table in DB
        :param parameter: 'Temperature','Humidity','Pressure'
        :param win: cur windows
        :return:
        """

        self.clean_screen_function(win)
        # tk.Label(text=f" {parameter} for last 24 hours", fg="blue")
        self.label_static("parameter", win, self.SS_TABLE_X_LABEL_CHART, self.SS_TABLE_Y_LABEL_CHART, f" {parameter.replace('_',' ')} for the {self.DAY}")

        # BUTTONS
        name_a = tk.Button(win, text=self.STRING_BUTTON_HISTORY_ONE_DAY, fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic(parameter,win,table,1))
        name_a.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_a.pack()
        name_a.place(x=self.FS_BUTTON_X_ONE_DAY, y=self.FS_BUTTON_Y_ONE_DAY)

        name_b = tk.Button(win, text=self.STRING_BUTTON_HISTORY_7_DAYS, fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic(parameter,win,table,7))
        name_b.config(font=(f"{self.font_buttons}", self.size_buttons))
        name_b.pack()
        name_b.place(x=self.FS_BUTTON_X_7_DAY, y=self.FS_BUTTON_Y_7_DAY)


        self.back_button(win)
        self.plot_me(win, parameter.lower(), period,table)


    def first_screen(self,win):
        """ this function start our first windows view 800x480"""
        self.clean_screen_function(win)
        #value = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        # lable function
        self.label_static("temp", win, self.FS_TABLE_X_TEMP, self.FS_LEVEL_TABLES, self.STRING_TABLE_TEMP_IN)
        self.label_static("temprr", win, self.FS_TABLE_X_HUM, self.FS_LEVEL_TABLES, self.STRING_TABLE_HUM_IN)
        self.label_static("press", win, self.FS_TABLE_X_PRESS, self.FS_LEVEL_TABLES, self.STRING_TABLE_PRESS_IN)
        self.label_static("tem_outside", win, self.FS_TABLE_X_TEMP_OUTSIDE, self.FS_TABLE_Y_TEMP_OUTSIDE, self.STRING_TABLE_TEMP_OUT)
        self.label_static("press_outside", win, self.FS_TABLE_X_PRESS_OUTSIDE, self.FS_TABLE_Y_PRESS_OUTSIDE, self.STRING_TABLE_PRESS_OUT)
        self.label_static("cpu temp", win, self.FS_TABLE_X_CPU_TEMP, self.FS_TABLE_Y_CPU_TEMP, self.STRING_TABLE_CPU)

        # labels live values ####################################################
        self.label_dynamic(f"{self.INDEX_TEMP_INSIDE}", win, self.FS_VALUE_X_TEMP, self.FS_LEVEL_VALUES, self.INDEX_TEMP_INSIDE, self.FS_VALUE_SIZE) #temp
        self.label_dynamic("press4", win, self.FS_VALUE_X_HUM, self.FS_LEVEL_VALUES, self.INDEX_HUM, self.FS_VALUE_SIZE) #humidity
        self.label_dynamic("press4", win, self.FS_VALUE_X_PRESS, self.FS_LEVEL_VALUES, self.INDEX_PRESS_INSIDE) # pressure
        self.label_dynamic("press5", win, self.FS_VALUE_X_TIME, self.FS_VALUE_Y_TIME,self.INDEX_TIME,self.FS_SIZE_VALUE_TIME) # time
        self.label_dynamic("press6", win, self.FS_VALUE_X_TEMP_OUTSIDE, self.FS_VALUE_Y_TEMP_OUTSIDE,self.INDEX_TEMP_OUTSIDE,self.FS_VALUE_SIZE) # temp out
        self.label_dynamic("press7", win, self.FS_VALUE_X_NAMEDAY, self.FS_VALUE_Y_NAMEDAY,self.INDEX_NAMEDAY,self.FS_SIZE_VALUE_NAMEDAY) # Nameday
        self.label_dynamic("press8", win,self.FS_VALUE_X_VIDEO_MODE, self.FS_VALUE_Y_VIDEO_MODE,self.INDEX_VIDEO_STATUS,self.FS_SIZE_VALUE_VIDEO_MODE) # Video mode
        self.label_dynamic("press9", win,self.FS_VALUE_X_WETTER_STATUS, self.FS_VALUE_Y_WETTER_STATUS,self.INDEX_STATUS_OUTSIDE,self.FS_SIZE_VALUE_WETTER_STATUS,"Calibri") # wetter status
        self.label_dynamic("press9", win,self.FS_VALUE_X_PRESSURE_OUTSIDE, self.FS_VALUE_Y_PRESSURE_OUTSIDE,self.INDEX_PRESS_OUTSIDE) # presure outside
        self.label_dynamic("press10", win,self.FS_VALUE_X_CPU_TEMP, self.FS_VALUE_Y_CPU_TEMP,self.INDEX_CPU_TEMP,self.FS_SIZE_VALUE_CPU_TEMP) # cpu temp

        # labels units ########################################################
        self.label_static("temp", win, self.FS_UNITS_X_TEMP, self.FS_LEVEL_UNITS, self.STRING_DEGREES, self.FS_SIZE_UNITS)
        self.label_static("temprr", win, self.FS_UNITS_X_HUM, self.FS_LEVEL_UNITS, " %", self.FS_SIZE_UNITS)
        self.label_static("press", win, self.FS_UNITS_X_PRESS, self.FS_LEVEL_UNITS, " hPa", self.FS_SIZE_UNITS_hPa)
        #.label_static("tem_out", win, self.FS_UNITS_X_TEMP_OUTSIDE, self.FS_UNITS_Y_TEMP_OUTSIDE, " C", self.FS_SIZE_UNITS)
        self.label_static("pressure_out", win, self.FS_UNITS_X_PRESSURE_OUTSIDE, self.FS_UNITS_Y_PRESSURE_OUTSIDE, " hPa", self.FS_SIZE_UNITS_hPa)
        self.label_static("temp cpu", win, self.FS_UNITS_X_CPU_TEMP, self.FS_UNITS_Y_CPU_TEMP, self.STRING_DEGREES, self.FS_SIZE_UNITS)

        # buttons ######################
        button_a = tk.Button(win, text=self.STRING_BUTTON_HISTORY_TEMP, fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Temperature", win,self.history.NAME_TABLE))
        button_a.config(font=(f"{self.font_buttons}", self.size_buttons))
        button_a.pack()
        button_a.place(x=self.FS_BUTTON_X_HISTORY_TEMP, y=self.FS_LEVEL_BUTTONS)

        button_b = tk.Button(win, text=self.STRING_BUTTON_HISTORY_HUM, fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Humidity",win,self.history.NAME_TABLE))
        button_b.config(font=(f"{self.font_buttons}", self.size_buttons))
        button_b.pack()
        button_b.place(x=self.FS_BUTTON_X_HISTORY_HUM, y=self.FS_LEVEL_BUTTONS)

        button_c = tk.Button(win, text=self.STRING_BUTTON_HISTORY_PRESS, fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Pressure", win,self.history.NAME_TABLE))
        button_c.config(font=(f"{self.font_buttons}", self.size_buttons))
        button_c.pack()
        button_c.place(x=self.FS_BUTTON_X_HISTORY_PRESS, y=self.FS_LEVEL_BUTTONS)

        button_temp_out = tk.Button(win, text=self.STRING_BUTTON_HISTORY_TEMP_OUT, fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Temperature_outside", win,self.history.NAME_TABLE_OUTSIDE))
        button_temp_out.config(font=(f"{self.font_buttons}", self.FS_HISTORY_TEMP_OUTSIDE_SIZE))
        button_temp_out.pack()
        button_temp_out.place(x=self.FS_BUTTON_X_HISTORY_TEMP_OUTSIDE, y=self.FS_BUTTON_Y_HISTORY_TEMP_OUTSIDE)

        button_cpu = tk.Button(win, text=self.STRING_BUTTON_HISTORY_CPU, fg=self.fg_buttons, bg=self.bg_buttons,
                           command=lambda: self.show_statistic("Temperature_cpu", win,
                                                               self.history.NAME_TABLE_CPU))
        button_cpu.config(font=(f"{self.font_buttons}", self.FS_HISTORY_HISTORY_CPU_SIZE))
        button_cpu.pack()
        button_cpu.place(x=self.FS_BUTTON_X_HISTORY_CPU_TEMP, y=self.FS_BUTTON_Y_HISTORY_CPU_TEMP)

        # break button
        button_break = tk.Button(win, text="X", fg="Red", bg=self.bg_buttons,
                           command=lambda: self.logout_screen(win))
        button_break.config(font=(f"{self.font_buttons}", self.size_buttons))
        button_break.pack()
        button_break.place(x=self.FS_BUTTON_X_BREAK, y=self.FS_BUTTON_Y_BREAK)

        ## video button
        self.video_button(win)

        ## shutdown button
        self.shutdown_button(win)

        ## reset tries logout
        self.TRIES_ENTER_PASSWORD =0






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
        function for dynamic updating of the values
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

        # def update_time(index):
        #     """ just update the screens"""
        #     # dinamic_value_function =      {1: self.sensor.reading()[0], #temp inside
        #     #                                2: self.sensor.reading()[1],# hum inside
        #     #                                3: self.sensor.reading()[2], # presurre inside
        #     #                                4: datetime.datetime.today().strftime('%H:%M  %d-%m-%Y'),# time
        #     #                                5: self.outside.acctual_temperature_outside()[0], # temp outside
        #     #                                #6: self.outside.acctual_temperature_outside()[1], # status outside
        #     #                                7: self.outside.acctual_temperature_outside()[2], # pressure outside
        #     #                                8: self.cpu_raspi.temperature_CPU(), # CPU temp
        #     #                                9: f"Wrong password! You have {self.MAX_ENTERS_PASSWORD-self.TRIES_ENTER_PASSWORD} more times." # wrong password
        #
        #                                    # }
        #     # if index in dinamic_value_function.keys():
        #     #     self.value=dinamic_value_function[index]
        #     """ """
        #     if index==self.INDEX_TEMP_INSIDE: #temp
        #         self.value = self.sensor.reading()[0]
        #
        #     elif index==self.INDEX_HUM: # hum
        #         self.value = self.sensor.reading()[1]
        #     elif index==self.INDEX_PRESS_INSIDE: # pressure
        #         self.value = self.sensor.reading()[2]
        #
        #     elif index==self.INDEX_TIME: # time
        #         self.value = datetime.datetime.today().strftime('%H:%M  %d-%m-%Y')
        #
        #         ### restat here ##############################################
        #         hh,mm=self.value.split("  ")[0].split(":")
        #         if f"{hh}:{mm}" == self.TIME_RESTART and USER==USER_CLIENT and self.IS_REBOOT==False:
        #             print('Reboot')
        #             self.IS_REBOOT = True
        #             os.system('sudo reboot')
        #
        #     elif index==self.INDEX_TEMP_OUTSIDE: #temp outside
        #         self.value =self.outside.acctual_temperature_outside()[0]
        #
        #     elif index==self.INDEX_STATUS_OUTSIDE: #status outside
        #         #self.value =self.outside.acctual_temperature_outside()[1]
        #         word =self.outside.acctual_temperature_outside()[1]
        #         if word in self.DICTIONARY_DE_to_BG.keys():
        #             self.value=self.DICTIONARY_DE_to_BG[word]
        #         else:
        #             self.value = self.outside.acctual_temperature_outside()[1]
        #
        #
        #     elif index==self.INDEX_PRESS_OUTSIDE: #presure outside
        #         self.value =self.outside.acctual_temperature_outside()[2]
        #
        #     elif index==self.INDEX_CPU_TEMP: #cpu temp
        #         self.value =self.cpu_raspi.temperature_CPU()
        #         ### if it is too hot, shutdown
        #         if USER==USER_CLIENT and self.value>self.MAX_TEMPERATURE_CPU and self.IS_REBOOT==False:
        #             self.IS_REBOOT = True
        #             os.system("sudo shutdown")
        #
        #
        #     elif index==self.INDEX_WRONG_PASSWORD_STRING: #message passowrd
        #         self.value =f"Wrong password! You have {self.MAX_ENTERS_PASSWORD-self.TRIES_ENTER_PASSWORD} more times."
        #
        #
        #     elif index==self.INDEX_NAMEDAY: # Nameday
        #         text_=self.orthodox.current_day_ortodox()
        #         if text_ !="":
        #             self.value = f"????????:  {text_}"
        #         else:
        #             self.value = self.STRING_NO_NAMEDAY
        #
        #     elif index == self.INDEX_VIDEO_STATUS:
        #         self.value=self.VIDEO_MODUS
        #         self.VIDEO_BG='Red' if self.VIDEO_ON == True else 'Green'
        #         self.VIDEO_TEXT='Stop video' if self.VIDEO_ON == True else 'Play video'
        #
        #
        #     #self.value = self.my_switch.searched_index(index)
        #     name.config(text=self.value)
        #     name.after(self.interval_refresh_page, update_time,index)

        #update_time(index)
        self._update_function(name,index)

    def _update_function(self,name,index):
        """
        function for the update the screens
        every dynamic label hat own functionality and source to get the new value
        :param name: name of the dynamic label
        :param index: index in the system for searching
        :return:
        """

        """ """
        if index == self.INDEX_TEMP_INSIDE:  # temp
            self.value = self.sensor.reading()[0]

        elif index == self.INDEX_HUM:  # hum
            self.value = self.sensor.reading()[1]
        elif index == self.INDEX_PRESS_INSIDE:  # pressure
            self.value = self.sensor.reading()[2]

        elif index == self.INDEX_TIME:  # time
            self.value = datetime.datetime.today().strftime('%H:%M  %d-%m-%Y')
            ### restat here ##############################################
            hh, mm = self.value.split("  ")[0].split(":")
            if f"{hh}:{mm}" == self.TIME_RESTART and USER == USER_CLIENT and self.IS_REBOOT == False:
                print('Reboot')
                self.IS_REBOOT = True
                os.system('sudo reboot')

            if f"{hh}:{mm}" == self.TIME_UPDATE and USER == USER_CLIENT:
                os.system('sudo apt-get update')

            if f"{hh}:{mm}" == self.TIME_SHUTDOWN and USER == USER_CLIENT:
                os.system('sudo shutdown')

        elif index == self.INDEX_TEMP_OUTSIDE:  # temp outside
            self.value = self.outside.acctual_temperature_outside()[0]

        elif index == self.INDEX_STATUS_OUTSIDE:  # status outside
            # self.value =self.outside.acctual_temperature_outside()[1]
            word = self.outside.acctual_temperature_outside()[1]
            if word in self.DICTIONARY_DE_to_BG.keys():
                self.value = self.DICTIONARY_DE_to_BG[word]
            else:
                self.value = self.outside.acctual_temperature_outside()[1]


        elif index == self.INDEX_PRESS_OUTSIDE:  # presure outside
            self.value = self.outside.acctual_temperature_outside()[2]

        elif index == self.INDEX_CPU_TEMP:  # cpu temp
            self.value = self.cpu_raspi.temperature_CPU()
            ### if it is too hot, shutdown
            if USER == USER_CLIENT and self.value > self.MAX_TEMPERATURE_CPU and self.IS_REBOOT == False:
                self.IS_REBOOT = True
                os.system("sudo shutdown")


        elif index == self.INDEX_WRONG_PASSWORD_STRING:  # message passowrd
            self.value = f"Wrong password! You have {self.MAX_ENTERS_PASSWORD - self.TRIES_ENTER_PASSWORD} more times."


        elif index == self.INDEX_NAMEDAY:  # Nameday
            text_ = self.orthodox.current_day_ortodox()
            if text_ != "":
                self.value = f"????????:  {text_}"
            else:
                self.value = self.STRING_NO_NAMEDAY

        elif index == self.INDEX_VIDEO_STATUS:
            self.value = self.VIDEO_MODUS
            self.VIDEO_BG = 'Red' if self.VIDEO_ON == True else 'Green'
            self.VIDEO_TEXT = 'Stop video' if self.VIDEO_ON == True else 'Play video'

        # self.value = self.my_switch.searched_index(index)
        name.config(text=self.value)
        name.after(self.interval_refresh_page, self._update_function, name,index)

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

    def plot_me(self, win, parameter, period,table):
        """
        this control the graphical windows in the tkinter page
        :param table: which table in DB
        :param win: windows
        :param parameter: 'temperature','humidity','pressure'
        :param today: todays date
        :return:
        """


        # the figure that will contain the plot
        fig_color=0.01
        fig = Figure(figsize=(13, 5), dpi=80)
        fig.patch.set_facecolor((fig_color, fig_color, fig_color))


        # list of squares
        #ys, xs = self.history.values_for_a_period(parameter,period)
        xs,ys = self.history.return_info_for_period(parameter,table,period)
        plot1 = fig.add_subplot(111) # fig.patch.set_facecolor('xkcd:mint green')
        plot1.grid(color=((0.15,0.15,0.15)))
        plot1.set_facecolor((fig_color, fig_color, fig_color))
        plot1.plot(xs, ys, 'g',linewidth=4)
        #################

        word_day='day' if period==1 else 'days'
        plot1.set_xlabel(f'{period} {word_day}',fontsize=20,color='White') # xaxis.label.set_color('red')
        plot1.set_ylabel(f'{parameter.replace("_"," ")}',fontsize=20,color='White')
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
        self.label_static("byebye",win,300,200,self.STRING_SHUTDOWN,70)


        shut_down='sudo shutdown'

        if USER=='raspi':
            os.system(shut_down)
        else:
            print(shut_down)
            exit()


    def shutdown_button(self,win):
        name_shutdown = tk.Button(win, text="Shtd", fg="Red", bg=self.bg_buttons,
                           command=lambda: self.shut_down(win))
        name_shutdown.config(font=(f"{self.font_buttons}", self.FS_SHUTDOWN_SIZE))
        name_shutdown.pack()
        name_shutdown.place(x=self.FS_BUTTON_X_SHUTDOWN, y=self.FS_BUTTON_Y_SHUTDOWN)

##################################################################################################
    def logout_screen(self,win):
        """
        page where to show keyboard and logout function
        :param win: current windows
        :return:
        """

        self.clean_screen_function(win)
        if self.TRIES_ENTER_PASSWORD==0:
            self.back_button(win)
        self.label_static("enter", win, self.LS_TABLE_ENTER_X, self.LS_TABLE_ENTER_Y, "Password :",self.LS_TABLE_ENTER_SIZE)
        if self.TRIES_ENTER_PASSWORD>0:
            self.label_dynamic("tries", win, self.LS_WRONG_PASSWORD_X, self.LS_WRONG_PASSWORD_Y, self.INDEX_WRONG_PASSWORD_STRING, self.LS_WRONG_PASSWORD_FONT,'Areil',self.LS_WRONG_PASSWORD_COLOR)  # temp
        self.password = tk.Entry(win, show="*", width=10, font=self.LS_ENTER_FONT)
        self.password.pack()
        self.password.place(x=self.LS_ENTER_FIELD_X,y=self.LS_ENTER_FIELD_Y)

        button_enter = tk.Button(win, text="Enter", fg="White", bg=self.bg_buttons,
                                 command=lambda: self.__check_if_right_password(self.password.get(),win))
        button_enter.config(font=(f"{self.font_buttons}", self.size_buttons))
        button_enter.pack()
        button_enter.place(x=self.LS_ENTER_BUTTON_X, y=self.LS_ENTER_BUTTON_Y)

        button_clear = tk.Button(win, text="Empty", fg="White", bg=self.bg_buttons,
                                 command=lambda: self.__clear_function(win))
        button_clear.config(font=(f"{self.font_buttons}", self.size_buttons))
        button_clear.pack()
        button_clear.place(x=self.LS_CLEAR_BUTTON_X, y=self.LS_CLEAR_BUTTON_Y)
        self.__create_keypad(win)

        if self.TRIES_ENTER_PASSWORD >= self.MAX_ENTERS_PASSWORD:
            self.shut_down(win)
        self.TRIES_ENTER_PASSWORD += 1


    def __check_if_right_password(self, password,win):
        """
        check if the entered password is corect
        :param password: entered password
        :param win:
        :return:
        """

        if password == self.PASSWORD:
            exit()
        else:
            self.logout_screen(win)

    def __create_keypad(self,win):
        """
        create the buttons of the keyboard
        :param win:
        :return:
        """


        for y in range(3):
            for x in range(1,4):
                val = y * 3 + x
                text = str(val)
                button_key = tk.Button(win, text=text, command=lambda txt=text: self.__insert_text(txt))
                button_key.config(font=(f"{self.font_buttons}", self.LS_SIZE_FONT_BUTTONS))
                button_key.pack()
                button_key.place(x=self.LS_KEYBOARD_X+(x*self.LS_SIZE_BUTTONS), y=self.LS_KEYBOARD_Y+y*self.LS_SIZE_BUTTONS)

    def __insert_text(self, text):
        """
        :param text : text to be insert into enter field
        """
        self.password.insert('end', text)

    def __clear_function(self,win):
        """
        clear the entry field
        :param win:
        :return:
        """

        self.TRIES_ENTER_PASSWORD -= 1
        self.logout_screen(win)











