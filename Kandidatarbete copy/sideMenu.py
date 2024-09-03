from customtkinter import *
from animations import SlidePanel

class SideMenu():
    
    def __init__(self):
        pass
    
    def setUp(self, master, go_to_tests, go_to_results, go_to_edit, log_out, lastFrame):

        def goTo(page):
            if page == 'tests':
                go_to_tests()
            elif page == 'results':
                go_to_results()
            elif page == 'edit':
                go_to_edit()
            else:
                log_out()

        animatedPanel =  SlidePanel(master, 1, 0.8)

        menu = CTkButton(master, width=80, height=40, text='Menu', command=animatedPanel.animate)
        menu.place(relx=0.9, rely = 0.07, anchor = 'c')
    
        edit = CTkButton(animatedPanel, width=100, text='Profile', command=lambda: goTo('edit'))
        edit.pack(expand = True, fill = 'both', padx=5, pady=3)
        tests = CTkButton(animatedPanel, width=100, text='New test', command=lambda: goTo('tests'))
        tests.pack(expand = True, fill = 'both', padx=5, pady=3)
        results = CTkButton(animatedPanel, width=100, text='Results', command=lambda: goTo('results'))
        results.pack(expand = True, fill = 'both', padx=5, pady=3)
        logout = CTkButton(animatedPanel, width=100, text='Log out', command=lambda: goTo('log_out'))
        logout.pack(expand = True, fill = 'both', padx=5, pady=3)

        if (lastFrame == 'edi'):
            pass
        elif (lastFrame == 'tes'):
            pass
        elif (lastFrame == 'res'):
            pass
        elif (lastFrame == 'log'):
            pass
