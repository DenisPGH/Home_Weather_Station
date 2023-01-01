from visualisation_function import GUI_VIS
from tkinter import *



window = Tk()
window.geometry(f"800x480")
window.configure(background='black')
window.title("WETTER")
#window.attributes("-fullscreen", True)
gui=GUI_VIS(window)
gui.first_screen(window)
gui.release_windows(window)

