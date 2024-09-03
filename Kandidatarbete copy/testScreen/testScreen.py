from customtkinter import *
from testScreen.listItem import ListItem
from Database import Database
from sideMenu import SideMenu

db = Database()

test_names = ['6 Min Walk', 'Grip test','Pinch test', 'Box And Block', 'Normal walking', 'Max walking']
test_icons = [ 'images/walk_icon.png', 'images/fist.png', 'images/fist.png', 'images/box.png', 'images/walk_icon.png', 'images/walk_icon.png']



class TestScreen(CTkFrame):

    window_size = 550

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pack_propagate(0)
        self.configure(width=self.window_size, height=self.window_size, border_color = "grey", border_width = 2)
        self.place(relx=0.5, rely=0.5, anchor='c')
    
    

    def setUp(self, go_to_tests, go_to_results, go_to_edit, log_out, currPatient, lastFrame):
        
        scrollable_frame = CTkScrollableFrame(self, width=self.window_size - 75, height= self.window_size - 100)
        scrollable_frame.place(relx = 0.5, rely = 0.55, anchor = "c")

        title = CTkLabel(self, text= 'Tests', font=('Arial', 30))
        title.place(relx = 0.5, rely = 0.06, anchor = 'c')

        sideMenu = SideMenu()
        sideMenu.setUp(self, go_to_tests, go_to_results, go_to_edit, log_out, lastFrame)

        r = 0
        c = 0
        for i in range(len(test_names)):
         item = ListItem(scrollable_frame)
         item.setUp(test_names[i], test_icons[i], currPatient, i)
         item.grid(row = r, column = c, pady = 20, padx = 20)
         c += 1
         if c == 2:
                c = 0
                r += 1