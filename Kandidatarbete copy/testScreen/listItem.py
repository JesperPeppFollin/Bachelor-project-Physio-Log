from customtkinter import *
from PIL import ImageTk, Image
from Database import Database
from testScreen.test import Test
from datetime import date
from errorMessage import ErrorMessage

db = Database()
db.createDatabase()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

class ListItem(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 200
        self.height = 200

        self.pack_propagate(0)
        self.configure(width=self.width, height=self.height,
                       border_color="grey", border_width=2)
        self.place(relx=0.5, rely=0.5, anchor="c")

    def setUp(self, test_name, test_icon, currPatient, i):

        def openTest():
            test = TestFrame(self.winfo_toplevel())
            test.setUp(test_name, currPatient, i)

        title = CTkLabel(self, text=test_name, font=('Century Gothic', 25))
        title.place(anchor='c', relx=0.5, rely=0.15)

        # img = CTkImage(dark_image=Image.open(resource_path(test_icon)), size=(50, 50))

        # image = CTkLabel(self, image=img, text='')
        # image.place(anchor='c', relx=0.5, rely=0.5)
        
        # img = Image.open(test_icon)
        # imgResized = img.resize((50, 50), Image.ANTIALIAS)
        # img2 = ImageTk.PhotoImage(imgResized)

        # image = CTkLabel(self, text='', image=img2)
        # image = CTkLabel(self, text='', image=img)

        # image.pack_propagate(0)
        # image.place(anchor='c', relx=0.5, rely=0.5)

        # img.pack_propagate(0)
        # img.place(anchor='c', relx=0.5, rely=0.5)

        # img.configure(ANCHOR='c')

        new_button = CTkButton(self, text='Open', width=self.width *
                               0.8, font=('Century Gothic', 15), command=openTest)
        new_button.place(anchor='c', relx=0.5, rely=0.85)


class TestFrame(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 500
        self.height = 500
        self.unit = ''

        self.pack_propagate(0)
        self.configure(width=self.width, height=self.height, border_color="grey", border_width=2)
        self.place(relx=0.5, rely=0.5, anchor="c")

    def setUp(self, test_name, currPatient, i):

        test = Test()
        test.id = i
        self.output_var = StringVar(value='')

        if i ==0:
            self.unit = 'm'
        elif i == 1 or i == 2:
            self.unit = 'N'

        elif i == 3:
            self.unit = 'no'
        
        else: 
            self.unit = 'm/s'

        def saveTest():
            try:
                input_value = float(input_var.get().replace(',','.'))
                if i != 0:
                    input_value2 = float(input_var2.get().replace(',','.'))
            except ValueError:
                error = ErrorMessage(self)
                if i == 0:
                    error.setUp('Invalid input', 'Please enter a valid number for the result')
                else:
                    error.setUp('Invalid input', 'Please enter a valid number for the results')

                input_var.set('')
                input_var2.set('')
                return
            if i == 0:
                mean_value = float(test.createResults(currPatient, i))
            else: 
                mean_value = input_value2
            
            patient_value = input_value

            
            percent = patient_value / mean_value
            
            
            

            db.newTest(currPatient, test, patient_value, percent)

            savedBox = SavedBox(self)
            savedBox.setUp(patient_value, percent, currPatient, self.unit)

            db.showDatabase()

        title = CTkLabel(self, text=test_name, font=('Century Gothic', 28))
        title.place(anchor='c', relx=0.5, rely=0.15)
        if i == 0:
            input_label = CTkLabel(self, text='Result ['+self.unit+']')
            input_label.place(anchor='c', relx=0.5, rely=0.45)
            input_var = StringVar(value='')
            input_entry = CTkEntry(self, textvariable=input_var)
            input_entry.place(anchor='c', relx=0.5, rely=0.5)

        else: 
            input_label = CTkLabel(self, text='Result ['+self.unit+']')
            input_label.place(anchor='c', relx=0.5, rely=0.35)
            input_var = StringVar(value='')
            input_entry = CTkEntry(self, textvariable=input_var)
            input_entry.place(anchor='c', relx=0.5, rely=0.4)

            input_label2 = CTkLabel(self, text='Expected result ['+self.unit+']')
            input_label2.place(anchor='c', relx=0.5, rely=0.55)
            input_var2 = StringVar(value='')
            input_entry2 = CTkEntry(self, textvariable=input_var2)
            input_entry2.place(anchor='c', relx=0.5, rely=0.6)

        back_button = CTkButton(self, text="Back", command=self.destroy)
        back_button.place(anchor='sw', relx=0.04, rely=0.96)

        save_button = CTkButton(self, text="Save", command=saveTest)
        save_button.place(anchor='se', relx=1-0.04, rely=0.96)


class SavedBox(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 550
        self.height = 550

        self.pack_propagate(0)
        self.configure(width=self.width, height=self.height, border_color="grey", border_width=20)
        self.place(relx=0.5, rely=0.5, anchor="c")

    def setUp(self, result, percent, currPatient, unit):

        if result % 1 == 0:
            result = round(result)

        
        resultstr = str(result) + unit

        def destroy_parent_frame():
            # Get the parent of the current frame
            parent = self.winfo_parent()
            # Destroy the parent widget
            if parent:
                parent_widget = self._nametowidget(parent)
                parent_widget.destroy()

        title = CTkLabel(self, text='Test saved succesfully!',
                         font=('Century Gothic', 30))
        title.place(anchor='c', relx=0.5, rely=0.15)

        name_entry = CTkLabel(self, text='Patient: ' + currPatient.name)
        name_entry.place(anchor='c', relx=0.5, rely=0.3)

        result_entry = CTkLabel(self, text='Result: ' + str(resultstr))
        result_entry.place(anchor='c', relx=0.5, rely=0.4)

        percent_entry = CTkLabel(
            self, text='Percent of expected value: ' + str(round(percent*100))+'%')
        percent_entry.place(anchor='c', relx=0.5, rely=0.5)

        date_entry = CTkLabel(self, text='Date of test: ' + str(date.today()))
        date_entry.place(anchor='c', relx=0.5, rely=0.6)

        tests_button = CTkButton(
            self, text='Ok!', command=destroy_parent_frame)
        tests_button.place(relx=0.5, rely=0.75, anchor="c")
