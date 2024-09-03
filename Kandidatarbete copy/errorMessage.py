from customtkinter import *

class ErrorMessage(CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 320
        self.height = 160

        self.pack_propagate(0)
        self.configure(width=self.width, height=self.height, border_color="grey", border_width=2)
        self.place(relx=0.5, rely=0.5, anchor="c")

    def setUp(self, title, breadText):

        title = CTkLabel(self, text=title, font=('Century Gothic', 28))
        title.place(anchor='c', relx=0.5, rely=0.2)

        text = CTkLabel(self, text=breadText, font=('Century Gothic', 14), wraplength=200)
        text.place(anchor='c', relx=0.5, rely=0.5)

        ok_button = CTkButton(self, text='Ok', command = self.destroy)
        ok_button.place(anchor='c', relx=0.5, rely=0.85)