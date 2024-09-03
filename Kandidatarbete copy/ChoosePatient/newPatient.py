from customtkinter import *
from PIL import ImageTk, Image
from patientProfile import PatientProfile
from Database import Database
from errorMessage import ErrorMessage


class NewPatient(CTkFrame):
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

    def setUp(self, go_to_choose, go_to_test,currPatient):

        frame = self
        # frame = CTkFrame(self, width=320, height=400)
        # frame.pack_propagate(0)
        # frame.place(anchor='c', relx=0.5, rely=0.5)

        def createPatient():
            if name_var.get() == '' or name_var.get() == 'name':
                error = ErrorMessage(self)
                error.setUp('Invalid Input', 'Please enter a valid name.')
            elif not (age_var.get().isdigit() and weight_var.get().isdigit() and height_var.get().isdigit()) or age_var.get() == 'age' or weight_var.get() == 'weight' or height_var.get() == 'height':
                error = ErrorMessage(self)
                error.setUp('Invalid Input',
                            'Please enter a number for age, weight and height.')
            elif gender_var.get() == 'gender':
                error = ErrorMessage(self)
                error.setUp('Invalid Input', 'Please enter a gender')
            else:
                db = Database()
                currPatient.name = name_var.get()
                currPatient.age = age_var.get()
                currPatient.weight = weight_var.get()
                currPatient.height = height_var.get()
                currPatient.gender = gender_var.get()
                db.newPatient(currPatient)
                db.showDatabase()
                go_to_test()

        title = CTkLabel(frame, text='Patient information', font=('Century Gothic', 25)).pack(pady=50)

        name_var = StringVar(value='name')
        name_entry = CTkEntry(frame, width=200, height = 35, placeholder_text='name', textvariable=name_var).pack(pady=10)
        name_label = CTkLabel(frame, text='Name: ',height=35,font=('Century Gothic', 15)).place(relx=0.22, rely=0.25)
        age_var = StringVar(value='age')
        age_entry = CTkEntry(frame, width=200, height = 35, placeholder_text='age', textvariable=age_var).pack(pady=10)
        age_label = CTkLabel(frame, text='Age: ',height=35,font=('Century Gothic', 15)).place(relx=0.24, rely=0.35)
        weight_var = StringVar(value='weight')
        weight_entry = CTkEntry(frame, width=200, height = 35, placeholder_text='weight', textvariable=weight_var).pack(pady=10)
        weight_label = CTkLabel(frame, text='Weight: ',height=35,font=('Century Gothic', 15)).place(relx=0.2, rely=0.45)
        height_var = StringVar(value='height')
        height_entry = CTkEntry(frame, width=200, height = 35, placeholder_text='height', textvariable=height_var).pack(pady=10)
        height_label = CTkLabel(frame, text='Height: ',height=35,font=('Century Gothic', 15)).place(relx=0.21, rely=0.55)

        gender_var = StringVar(value="gender")
        gender = CTkComboBox(
            frame,
            width=200, 
            height = 35,
            values=["Male", "Female"],
            variable=gender_var,
            state='readonly').pack(pady=(15, 10))
        gender_label = CTkLabel(frame, text='Gender: ',height=35,font=('Century Gothic', 15)).place(relx=0.2, rely=0.66)
        
        back = CTkButton(frame, width=100, text='Back', command=go_to_choose).place(anchor='sw', relx=0.05, rely=0.95)
        add = CTkButton(frame, width=100, text='Add', command=createPatient).place(anchor='se', relx=0.95, rely=0.95)

         