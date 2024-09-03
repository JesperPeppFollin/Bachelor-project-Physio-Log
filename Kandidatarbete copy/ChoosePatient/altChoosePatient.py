from customtkinter import *
from PIL import Image, ImageTk
from patientProfile import PatientProfile
from patient import Patient
from radioButton import ScrollableRadiobuttonFrame
from Database import Database
from errorMessage import ErrorMessage


class AltChoosePatient(CTkFrame):
    window_size=550
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pack_propagate(0)
        self.configure(width=self.window_size, height=self.window_size, border_color = "grey", border_width = 2)
        self.place(relx=0.5, rely=0.5, anchor='c')
        self.item = ''
        self.radiobutton_variable = StringVar(value='')

    def setUp(self, go_to_new, go_to_profile, currPatient):
        db = Database()

        def open_patient_profile():
            if (self.item == ''):
                error = ErrorMessage(self)
                if len(patientList)!=0:
                    error.setUp('Invalid input', 'Please select a patient')
                else:
                    error.setUp('Invalid input', 'Create a new patient')
            else:
                id = len(patientList) - patientList.index(self.item)
                db.oldPatient(currPatient, id)
                go_to_profile()

        def clicked():
            self.item = self.scrollable_radiobutton_frame.get_checked_item()

        frame = self
        
        patientList = db.getAllPatients()

        if len(patientList) == 0:
            titlebar ='No patients in database'
        else:
            titlebar ='Choose a patient'

        title = CTkLabel(frame, text='Welcome to Physio Log', font=('Century Gothic', 45))
        title.pack(pady=30)

        self.scrollable_radiobutton_frame = ScrollableRadiobuttonFrame(frame, width=550, command=clicked,
                                                                       item_list=patientList, 
                                                                       label_text = titlebar)
        self.scrollable_radiobutton_frame.configure(width=400, height = 250)
        self.scrollable_radiobutton_frame.pack(padx=5, pady=5, fill=Y)


        choose = CTkButton(frame, width=300, height = 40, text='Log in', command=open_patient_profile)
        choose.pack(side=TOP, anchor='c', padx=20, pady=10)

      
        back = CTkButton(frame, width=300, height = 40, text='New Patient', command=go_to_new)
        back.pack(side=TOP, anchor='c', padx=20, pady=10)

        

        albert = CTkLabel(frame, text='Albert Ahnlide', font=('Arial', 8), text_color='#B6B6B6')
        albert.place(anchor='c', relx= 0.88, rely=0.92)
        jesper = CTkLabel(frame, text='Jesper Follin © 2023', font=('Arial', 8), text_color='#B6B6B6')
        jesper.place(anchor='c', relx= 0.88, rely=0.95)

        

        

        








