from customtkinter import CTkFrame, CTkLabel, CTkButton, CTkImage
from ChoosePatient.newPatient import NewPatient
from ChoosePatient.oldPatient import OldPatient
import ChoosePatient.exitBox as exit
from PIL import ImageTk, Image

class ChoosePatient(CTkFrame):
    window_size = 550
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.pack_propagate(0)
        self.configure(width=self.window_size, height=self.window_size, border_color = "grey", border_width = 2)
        self.place(relx=0.5, rely=0.5, anchor='c')
        # self.pack_propagate(0)
        # self.configure(width=1000, height=1000)
        # self.place(relx=0.5, rely=0.5, anchor="c")

        # img = ImageTk.PhotoImage(Image.open('background8.png'))
        # background = CTkLabel(self, image=img, text='')
        # background.place(anchor='c', relx=0.5, rely=0.5)

    def setUp(self, go_to_new, go_to_old):

        frame = self
        # frame = CTkFrame(self, width=320, height=400)
        # frame.place(anchor='c', relx=0.5, rely=0.5)

        title = CTkLabel(frame, text='Welcome',font=('Century Gothic', 35))
        title.place(anchor='c', relx=0.5, rely=0.12)

        new_button = CTkButton(frame, text='New patient', width=220, font=('Century Gothic', 15), command=go_to_new)
        new_button.place(anchor='c', relx=0.5, rely=0.42)

        or_text = CTkLabel(frame, text='or', font=('Century Gothic', 13))
        or_text.place(anchor='c', relx=0.5, rely=0.5)

        old_button = CTkButton(frame, text='Already in the database', width=220, font=('Century Gothic', 15), command=go_to_old)
        old_button.place(anchor='c', relx=0.5, rely=0.58)

        company_text = CTkLabel(frame, text='Albepp © 2023', font=('Arial', 10), text_color='#B6B6B6')
        company_text.place(anchor='c', relx= 0.85, rely=0.95)