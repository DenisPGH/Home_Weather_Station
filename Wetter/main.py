from GUI.visualisation_function import GUI_VIS
from database_function import DataBaseWetter
import datetime

db=DataBaseWetter()

#db.store_new_info([12,34,67],actual_time)
from tkinter import *
window = Tk()
window.geometry(f"1000x1000")
window.configure(background='black')
window.title("WETTER")
window.attributes("-fullscreen", True)



gui=GUI_VIS(window)
gui.first_screen(window)
gui.release_windows(window)

date = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
hr,min,sec=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S').split(" ")[1].split(":")
print(sec)

############################################################
# from tkinter import *
# r=Tk()
# r.geometry(f"400x400")
# r.title("WETTER")
#
# def update():
#     actual_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
#     my_label.config(text=actual_time)
#     my_label.after(10, update)
#
#
# my_label=Label(r,text='D')
# my_label.pack()
# update()
#
#
# r.mainloop()