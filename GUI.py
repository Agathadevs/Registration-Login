import customtkinter as ctk
ctk.set_appearance_mode("dark")
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("my app")
        self.geometry("500x400")
        self.label=label(self)
        self.Entry=Entry(self)
        
class label:
    """
    label(s) class
    """
    def __init__(self,parent):
        pass
       
class Entry:
    """
    Entry(s) class
    """
    def __init__(self,parent):
        self.entry=ctk.CTkEntry(parent).grid(padx=180,pady=60)
if __name__=="__main__" : 
    app=App()
    app.mainloop()