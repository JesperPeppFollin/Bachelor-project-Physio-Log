from customtkinter import *
from PIL import ImageTk, Image
from patient import Patient
from sideMenu import SideMenu

class PatientProfile(CTkFrame):
    window_size = 550
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pack_propagate(0)
        self.configure(width=self.window_size, height=self.window_size, border_color = "grey", border_width = 2)
        self.place(relx=0.5, rely=0.5, anchor='c')

        test = CTkLabel(self, text='HELLOO', font=('Arial', 50))
    
    def setUp(self, go_to_tests, go_to_profile, go_to_data, log_out, currPatient):

        title = CTkLabel(self, text='Welcome '+ currPatient.name, font=('Arial', 30))
        title.place(anchor='c', relx=0.5, rely=0.06)

        sideMenu = SideMenu()
        sideMenu.setUp(self, go_to_tests, go_to_profile, go_to_data, log_out)

        age = CTkLabel(self, text='Age: '+ str(currPatient.age)).place(anchor='c', relx=0.5, rely=0.55)
        weight = CTkLabel(self, text='Weight: '+ str(currPatient.weight)).place(anchor='c', relx=0.5, rely=0.60)
        height = CTkLabel(self, text='Height: '+ str(currPatient.height)).place(anchor='c', relx=0.5, rely=0.60)
        gender = CTkLabel(self, text='Gender: '+currPatient.gender).place(anchor='c', relx=0.5, rely=0.65)


