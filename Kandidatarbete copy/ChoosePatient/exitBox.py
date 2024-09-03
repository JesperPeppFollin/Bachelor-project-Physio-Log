from customtkinter import CTkFrame, CTkButton, CTkLabel, CTkImage, CTkCanvas
from PIL import Image, ImageTk
from tkinter import Label, PhotoImage

width = 350
height = 121
background = '#2C2C2C'

def run(root):

    frame_main = CTkFrame(root, width=width, height=height)
    frame_main.pack_propagate(0)
    frame_main.place(anchor='n', relx=0.5, rely=0.5)

    label = Label(frame_main, text='Are you sure you want to exit?')
    label.place(anchor='n', relx=0.5, rely=0.1) #byta till place för att inte blanda pack och place?
    
    button_back = CTkButton(frame_main, text='back', command=frame_main.destroy)
    button_back.place(anchor='c', relx=0.25, rely=0.75)
    button_quit = CTkButton(frame_main, text='quit', command=quit)
    button_quit.place(anchor='c', relx=0.75, rely=0.75)