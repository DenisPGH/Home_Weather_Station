from paths import USER_CLIENT, USER
from sqlite_db__function import SQLiteSensor
from visualisation_function import GUI_VIS
from tkinter import *

if USER ==USER_CLIENT:
    # run once
    # 1.inital db
    db = SQLiteSensor()
    # 2.create table
    db.create_table()
    # 3.copy csv
    db.csv__to_sqlite()
    # 4. print all infos
    db.print_all_info_from_table()





window = Tk()
window.geometry("800x480")
window.configure(background='black')
window.title("WETTER")
if USER == USER_CLIENT:
    window.attributes("-fullscreen", True)
gui=GUI_VIS(window)
gui.first_screen(window)
gui.release_windows(window)

