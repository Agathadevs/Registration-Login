import customtkinter as ctk
ctk.set_appearance_mode("dark")
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("my app")
        self.geometry("500x400")
        self.label=label(self)
        
        
    
class label:
    def __init__(self,parent):
        self.label=ctk.CTkLabel(parent,text="test label",fg_color="blue",corner_radius=10).grid(padx=20,pady=20)
        self.button=ctk.CTkButton(parent,text="test").grid()
        self.slider=ctk.CTkSlider(parent).grid()
        self.switch=ctk.CTkSwitch(parent,text="owo").grid()  
        self.entry=ctk.CTkEntry(parent,placeholder_text="test").grid()
        def optionmenu_callback(choice):
            print("optionmenu dropdown clicked:", choice)
        self.optionmenu=ctk.CTkOptionMenu(parent,values=["opt1","opt2"],command=optionmenu_callback).grid()
        self.progressbar=ctk.CTkProgressBar(parent,orientation="horizontal").grid(padx=50,pady=50)
        self.RB=ctk.CTkRadioButton(parent,text="hmm").grid()
if __name__=="__main__" : 
    app=App()
    app.mainloop()