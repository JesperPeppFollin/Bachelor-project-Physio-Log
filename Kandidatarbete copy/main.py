from ChoosePatient.choosePatient import ChoosePatient
from ChoosePatient.altChoosePatient import AltChoosePatient
from ChoosePatient.newPatient import NewPatient
from ChoosePatient.oldPatient import OldPatient
from ChoosePatient.editPatient import EditPatient
from testScreen.testScreen import TestScreen
from patientProfile import PatientProfile
from results import Results
import customtkinter as ctk
from Database import Database
from patient import Patient
from PIL import Image
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Physio Log")
app.minsize(550, 550)
app.maxsize(550,550)
app.after(201, lambda:app.iconbitmap('images/icon.ico'))

# app.attributes('-fullscreen',True)
db  = Database()
db.createDatabase()
currPatient = Patient()
lastFrame = ''

def buttonFunctions(currentFrame, newFrame, lastFrame):

    newIns = globals()[newFrame](app, height=550, width=550)

    if type(newIns) != type(currentFrame):
        lastFrame = str(currentFrame)[2:5]

    if newFrame == "ChoosePatient":
        newIns.setUp(
            lambda: buttonFunctions(newIns, "NewPatient",lastFrame),
            lambda: buttonFunctions(newIns, "OldPatient",lastFrame))

    elif newFrame == "NewPatient":
        newIns.setUp(
            lambda: buttonFunctions(newIns, "AltChoosePatient",lastFrame),
            lambda: buttonFunctions(newIns, "TestScreen",lastFrame),
            currPatient)

    elif newFrame == "OldPatient":
        newIns.setUp(
            lambda: buttonFunctions(newIns, "AltChoosePatient",lastFrame),
            lambda: buttonFunctions(newIns, "TestScreen",lastFrame),
            currPatient)
        
    elif newFrame == "TestScreen":
        newIns.setUp(
            lambda: buttonFunctions(newIns, "TestScreen",lastFrame),
            lambda: buttonFunctions(newIns, "Results",lastFrame),
            lambda: buttonFunctions(newIns, "EditPatient",lastFrame),
            lambda: buttonFunctions(newIns, "AltChoosePatient",lastFrame),
            currPatient,
            lastFrame)
    
    elif newFrame == "EditPatient":
        newIns.setUp(
            lambda: buttonFunctions(newIns, "TestScreen",lastFrame),
            lambda: buttonFunctions(newIns, "Results",lastFrame),
            lambda: buttonFunctions(newIns, "EditPatient",lastFrame),
            lambda: buttonFunctions(newIns, "AltChoosePatient",lastFrame),
            currPatient,
            lastFrame)
    
    elif newFrame == "Results":
        newIns.setUp(
            lambda: buttonFunctions(newIns, "TestScreen",lastFrame),
            lambda: buttonFunctions(newIns, "Results",lastFrame),
            lambda: buttonFunctions(newIns, "EditPatient",lastFrame),
            lambda: buttonFunctions(newIns, "AltChoosePatient",lastFrame),
            currPatient,
            lastFrame)
        
    elif newFrame == "AltChoosePatient":
        newIns.setUp(
            lambda: buttonFunctions(CP, "NewPatient",lastFrame),
            lambda: buttonFunctions(CP, "TestScreen",lastFrame), 
            currPatient)
        
        
    currentFrame.destroy()


CP = AltChoosePatient(app, height=550, width=550)
CP.setUp(
    lambda: buttonFunctions(CP, "NewPatient",lastFrame),
    lambda: buttonFunctions(CP, "TestScreen",lastFrame), 
    currPatient)

app.mainloop()
