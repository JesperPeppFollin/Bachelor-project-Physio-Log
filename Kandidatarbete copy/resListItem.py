from customtkinter import *
from PIL import ImageTk, Image
from Database import Database
from testScreen.test import Test
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime 


db = Database()
db.createDatabase()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)


class ResListItem(CTkFrame):
    db = Database()
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 400
        self.height = 200
        self.test = Test()
        self.pack_propagate(0)
        self.configure(width=self.width, height=self.height, border_color = "grey", border_width = 2)
        self.place(relx=0.5, rely=0.5, anchor="c")

       

    def setUp(self, test_name, test_icon, currPatient, i):
        self.test.id = i

        def openList():
            listres = ListFrame(self.winfo_toplevel())
            listres.setUp(test_name, currPatient, i)


        def openChartR():
            db.getResults(currPatient, self.test)
            
            # Extract the float values from the tuples
            values = [result[0] for result in self.test.results]

            # Extract the date strings from the tuples and convert them to `datetime` objects
            dates = [datetime.datetime.strptime(date[0], '%Y-%m-%d') for date in self.test.dates]

            if len(values)==0:
                charterr = ErrorFrame(self.winfo_toplevel())
                charterr.setUp(test_name, currPatient, i)

            else: 
                fig, ax = plt.subplots(num=test_name)
                fig.suptitle('Results in "'+test_name+'" for ' + currPatient.name)

                # Create the plot
                ax.plot(dates, values)

                # Format the x-axis as dates
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m-%Y'))

                # Set the x-axis ticks to the values in dates
                ax.set_xticks(dates)

                # Add labels and title
                plt.xlabel('Date')
                
                if i ==0:
                    unit = 'm'
                elif i == 1 or i == 2:
                    unit = 'N'

                elif i == 3:
                    unit = 'no'
                
                else: 
                    unit = 'm/s'

                plt.ylabel('Results ['+unit+']')

                
                #plt.title('Results for '+test_name)

                # Display the plot
                plt.show()
            
        def openChartP():
            db.getPercent(currPatient, self.test)

            # Extract the float values from the tuples
            values = [percent[0] for percent in self.test.percent]

            values = [round(value * 100) for value in values]

            # Extract the date strings from the tuples and convert them to `datetime` objects
            dates = [datetime.datetime.strptime(date[0], '%Y-%m-%d') for date in self.test.dates]

            if len(values)==0:
                charterr = ErrorFrame(self.winfo_toplevel())
                charterr.setUp(test_name, currPatient, i)

            else: 
                fig, ax = plt.subplots(num=test_name)
                fig.suptitle('Results in "'+test_name+'" for ' + currPatient.name)

                # Create the plot
                ax.plot(dates, values)

                # Format the x-axis as dates
                ax.xaxis.set_major_formatter(mdates.DateFormatter('%d/%m-%Y'))

                # Set the x-axis ticks to the values in dates
                ax.set_xticks(dates)

                # Add labels and title
                plt.xlabel('Date')
                plt.ylabel('Percent of expected result [%]')
                #plt.title('Results for '+test_name)

                # Display the plot
                plt.show()

        title = CTkLabel(self, text=test_name,font=('Century Gothic', 28))
        title.place(anchor='c', relx=0.5, rely=0.15)

        # img = CTkImage(dark_image=Image.open(resource_path(test_icon)), size=(50, 50))

        # image = CTkLabel(frame, image=img, text='')
        # image.place(anchor='c', relx=0.5, rely=0.5)


        # img=Image.open(test_icon)
        # imgResized=img.resize((50,50),Image.ANTIALIAS)
        # img2=ImageTk.PhotoImage(imgResized)

        # image = CTkLabel(frame, text='', image = img2)
        
        # image.pack_propagate(0)
        # image.place(anchor='c', relx=0.5, rely=0.5)



        chartP = CTkButton(self, text='Show chart of percentage', width=self.width*0.4, height = 30, font=('Century Gothic', 15), command= openChartP)
        chartP.place(anchor='c', relx=0.5, rely=0.40)

        chartR = CTkButton(self, text='Show chart of results', width=self.width*0.4, height = 30, font=('Century Gothic', 15), command= openChartR)
        chartR.place(anchor='c', relx=0.5, rely=0.6)

        lists = CTkButton(self, text='Show list of results', width=self.width*0.4, height = 30, font=('Century Gothic', 15), command= openList)
        lists.place(anchor='c', relx=0.5, rely=0.8)



class ErrorFrame(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 500
        self.height = 500

        self.pack_propagate(0)
        self.configure(width=self.width, height=self.height, border_color = "grey", border_width = 2)
        self.place(relx=0.5, rely=0.5, anchor="c")

    def setUp(self, test_name, currPatient, i):

        title = CTkLabel(self, text='No results are saved for this patient', font=('Century Gothic', 28))
        title.place(anchor='c', relx=0.5, rely=0.15)

        #name_var = StringVar(value='name')
        #name_entry = CTkEntry(frame, width=200, placeholder_text='name', textvariable=name_var).pack(pady=5)


        back_button = CTkButton(self, text="OK", command=self.destroy)
        back_button.place(anchor='c', relx=0.5, rely=0.5)


    
class ListFrame(CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.width = 500
        self.height = 500
        self.test = Test()

        self.pack_propagate(0)
        self.configure(width=self.width, height=self.height, border_color = "grey", border_width = 2)
        self.place(relx=0.5, rely=0.5, anchor="c")

    def setUp(self, test_name, currPatient, i):
        self.test.id = i



        #name_var = StringVar(value='name')
        #name_entry = CTkEntry(frame, width=200, placeholder_text='name', textvariable=name_var).pack(pady=5)
        db.getResults(currPatient, self.test)
        db.getPercent(currPatient,self.test)

        # Extract the float values from the tuples
        valuesR = [result[0] for result in self.test.results]
        valuesP = [percent[0] for percent in self.test.percent]

        valuesR = [int(value) if value % 1 == 0 else value for value in valuesR]


        dates = [datetime.datetime.strptime(date[0], '%Y-%m-%d') for date in self.test.dates]

        if len(valuesR)==0:
            charterr = ErrorFrame(self.winfo_toplevel())
            charterr.setUp(test_name, currPatient, i)
            self.destroy()

        else: 
            title = CTkLabel(self, text=test_name, font=('Century Gothic', 28))
            title.place(anchor='c', relx=0.5, rely=0.1)

            scrollable_frame = CTkScrollableFrame(self, width=self.width - 75, height= self.height - 150)
            scrollable_frame.place(relx = 0.5, rely = 0.55, anchor = "c")

            r=0

            if self.test.id ==0:
                unit = 'm'
            elif self.test.id == 1 or self.test.id == 2:
                unit = 'N'

            elif self.test.id == 3:
                unit = 'no'
            
            else: 
                unit = 'm/s'


            for i in range(len(valuesR)): 
                date_str = dates[i].strftime('%d/%m/%Y').lstrip('0').replace('/0', '/')
                item = CTkLabel(scrollable_frame, text=date_str+':    '+str(valuesR[i])+unit+'    ('+str(round(valuesP[i]*100))+'%)' )
                #item = CTkLabel(scrollable_frame, text=date_str+': '+str(valuesR[i])+unit+' ('+str(round(valuesP[i]*100))+'%)' )
                #item.grid(row = r, pady = 20, padx = 20)
                if i == 0:
                    item.grid(row = r, pady = (50, 10), padx = 20)
                else:
                    item.grid(row = r, pady = 10, padx = 20)
                r += 1
            
            posX = 0.1
            posY = 0.08
            xDiff = 0.15
            fontSize = 16

            date_label = CTkLabel(scrollable_frame, text = 'Date', font=('Century Gothic', fontSize, 'bold'))
            date_label.place(anchor='c', relx=posX, rely=posY)

            result_label = CTkLabel(scrollable_frame, text = 'Result', font=('Century Gothic bold', fontSize, 'bold'))
            result_label.place(anchor='c', relx=posX + xDiff, rely=posY)

            percent_label = CTkLabel(scrollable_frame, text = 'Percent', font=('Century Gothic bold', fontSize, 'bold'))
            percent_label.place(anchor='c', relx=posX  + xDiff * 2, rely=posY)



            back_button = CTkButton(self, text="Back", command=self.destroy)
            back_button.place(anchor='c', relx=0.5, rely=0.96)