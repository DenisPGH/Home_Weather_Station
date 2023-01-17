from paths import USER_CLIENT, USER
from sqlite_db__function import SQLiteSensor
from visualisation_function import GUI_VIS
from tkinter import *



# _*_ coding: utf-8 _*_




window = Tk()
window.geometry("800x480")
window.configure(background='black')
window.title("WETTER")
if USER == USER_CLIENT:
    window.attributes("-fullscreen", True)
gui=GUI_VIS(window)
gui.first_screen(window)
gui.release_windows(window)





