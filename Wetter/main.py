from visualisation_function import GUI_VIS
from tkinter import *






#export DISPLAY=0:0
window = Tk()
window.geometry("800x480")
window.configure(background='black')
window.title("WETTER")
#window.attributes("-fullscreen", True)
gui=GUI_VIS(window)
gui.first_screen(window)
gui.release_windows(window)

