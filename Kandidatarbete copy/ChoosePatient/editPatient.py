from customtkinter import *
from PIL import ImageTk, Image
from patient import Patient
from patientProfile import PatientProfile
from Database import Database
from sideMenu import SideMenu
from errorMessage import ErrorMessage

class EditPatient(CTkFrame):
    
    window_size = 550
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pack_propagate(0)
        self.configure(width=self.window_size, height=self.window_size, border_color = "grey", border_width = 2)
        self.place(relx=0.5, rely=0.5, anchor='c')

    def setUp(self, go_to_tests, go_to_results, go_to_edit, log_out, currPatient, lastFrame):
        frame = self

        sideMenu = SideMenu()
        sideMenu.setUp(self, go_to_tests, go_to_results, go_to_edit, log_out, lastFrame)

        def edit():
            if (name_var.get() == '' or name_var.get().isdigit() or name_var.get() == 'name'):
                error = ErrorMessage(self)
                error.setUp('Invalid Input', 'Please enter a valid name.')
            elif not (age_var.get().isdigit() and weight_var.get().isdigit() and height_var.get().isdigit()) or age_var.get() == 'age' or weight_var.get() == 'weight' or height_var.get() == 'height':
                error = ErrorMessage(self)
                error.setUp('Invalid Input', 'Please enter a number for age, weight and height.')
            elif gender_var == 'gender':
                error = ErrorMessage(self)
                error.setUp('Invalid Input', 'Please enter a gender')
            else:
                db = Database()
                currPatient.name = name_var.get()
                currPatient.age = age_var.get()
                currPatient.weight = weight_var.get()
                currPatient.height = height_var.get()
                currPatient.gender = gender_var.get()
                db.editPatient(currPatient)
                db.showDatabase()
                goBack()

        def goBack():
            if (lastFrame == 'tes'):
                go_to_tests()
            elif (lastFrame == 'res'):
                go_to_results()
            elif (lastFrame == 'edi'):
                go_to_edit()
            else:
                log_out()

        title = CTkLabel(frame, text='Patient information', font=('Century Gothic', 25)).pack(pady=50)
        name_var = StringVar(value=currPatient.name)
        name_entry = CTkEntry(frame, width=200, height = 35, placeholder_text='name', textvariable=name_var).pack(pady=10)
        name_label = CTkLabel(frame, text='Name: ',height=35,font=('Century Gothic', 15)).place(relx=0.22, rely=0.25)
        age_var = StringVar(value=currPatient.age)
        age_entry = CTkEntry(frame, width=200, height = 35, placeholder_text='age', textvariable=age_var).pack(pady=10)
        age_label = CTkLabel(frame, text='Age: ',height=35,font=('Century Gothic', 15)).place(relx=0.24, rely=0.35)
        weight_var = StringVar(value=currPatient.weight)
        weight_entry = CTkEntry(frame, width=200, height = 35, placeholder_text='weight', textvariable=weight_var).pack(pady=10)
        weight_label = CTkLabel(frame, text='Weight: ',height=35,font=('Century Gothic', 15)).place(relx=0.2, rely=0.45)
        height_var = StringVar(value=currPatient.height)
        height_entry = CTkEntry(frame, width=200, height = 35, placeholder_text='height', textvariable=height_var).pack(pady=10)
        height_label = CTkLabel(frame, text='Height: ',height=35,font=('Century Gothic', 15)).place(relx=0.21, rely=0.55)

        gender_var = StringVar(value=currPatient.gender)
        gender = CTkComboBox(
            frame,
            width=200, 
            height = 35,
            values=["Male", "Female"],
            variable=gender_var,
            state='readonly').pack(pady=(15, 10))
        gender_label = CTkLabel(frame, text='Gender: ',height=35,font=('Century Gothic', 15)).place(relx=0.2, rely=0.66)


        back = CTkButton(frame, width=100, text='Cancel', command=goBack).place(anchor='sw', relx=0.05, rely=0.95)
        save = CTkButton(frame, width=100, text='Save', command=edit).place(anchor='se', relx=0.95, rely=0.95)

        