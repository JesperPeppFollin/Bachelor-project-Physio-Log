from customtkinter import *
from PIL import Image, ImageTk
from patientProfile import PatientProfile
from patient import Patient
from radioButton import ScrollableRadiobuttonFrame
from Database import Database


class OldPatient(CTkFrame):
    window_size=550
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pack_propagate(0)
        self.configure(width=self.window_size, height=self.window_size, border_color = "grey", border_width = 2)
        self.place(relx=0.5, rely=0.5, anchor='c')
        self.item = ''
        self.radiobutton_variable = StringVar(value='')

    def setUp(self, go_to_choose, go_to_profile, currPatient):
        db = Database()

        def open_patient_profile():
            id = len(patientList) - patientList.index(self.item)
            db.oldPatient(currPatient, id)
            go_to_profile()

        def clicked():
            self.item = self.scrollable_radiobutton_frame.get_checked_item()

        frame = self
        # frame = CTkFrame(self, width=320, height=400)
        # frame.pack_propagate(0)
        # frame.place(anchor='c', relx=0.5, rely=0.5)

        patientList = db.getAllPatients()

        if len(patientList) == 0:
            title = CTkLabel(frame, text='No patients in database', font=('Century Gothic', 25))
        else:
            title = CTkLabel(frame, text='Choose patient', font=('Century Gothic', 25))

        title.pack(pady=30)

        self.scrollable_radiobutton_frame = ScrollableRadiobuttonFrame(frame, width=550, command=clicked,
                                                                       item_list=patientList)
        self.scrollable_radiobutton_frame.configure(width=250)
        self.scrollable_radiobutton_frame.pack(padx=15, pady=15, fill=Y)

        back = CTkButton(frame, width=100, text='Back', command=go_to_choose)
        back.pack(side=LEFT, anchor='sw', padx=20, pady=20)

        choose = CTkButton(frame, width=100, text='Log in', command=open_patient_profile)
        choose.pack(side=RIGHT, anchor='se', padx=20, pady=20)








