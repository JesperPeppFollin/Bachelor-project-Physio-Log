import customtkinter as ctk
class SlidePanel(ctk.CTkFrame):
  def __init__(self, parent, start_pos, end_pos):
        super().__init__(master = parent)

        self.start_pos = start_pos + 0.03
        self.end_pos = end_pos -0.01
        self.width = abs(start_pos-end_pos)

        self.pos = self.start_pos
        self.in_start_pos = True

        self.place(relx = self.start_pos, rely = 0.12, relwidth = self.width, relheight = 0.3)
  def animate(self):
        if self.in_start_pos:
              self.animate_forward()
        else:
              self.animate_backwards()

  def animate_forward(self):
        if self.pos > self.end_pos:
              self.pos -= 0.005
              self.place(relx = self.pos, rely = 0.12, relwidth = self.width, relheight = 0.3)
              self.after(2,self.animate_forward)
        else:
              self.in_start_pos = False
    
  def animate_backwards(self):
        if self.pos < self.start_pos:
              self.pos += 0.005
              self.place(relx = self.pos, rely = 0.12, relwidth = self.width, relheight = 0.3)
              self.after(2,self.animate_backwards)
        else:
              self.in_start_pos = True           