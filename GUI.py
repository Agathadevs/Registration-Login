import customtkinter as ctk
import json
ctk.set_appearance_mode("dark")
class ToplevelSignupWindow(ctk.CTkToplevel):
       def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x300")
        self.entry1=ctk.CTkEntry(self,placeholder_text="example@gmail.com",width=200)
        self.entry1.pack(padx=10,pady=15)
        

        self.entry2=ctk.CTkEntry(self,placeholder_text="passward",width=200)
        self.entry2.pack(padx=10,pady=15)
        

        self.btn1=ctk.CTkButton(self,text="Creat",corner_radius=10,command=self.creat).pack(padx=10,pady=10)
       def creat(self):
            acc=self.entry1.get()
            ps=self.entry2.get()
            if str(acc)[-10:]=="@gmail.com":
                ndata={acc:ps}
                with open('info.json', 'r') as f:
                    data = json.load(f)
                data["User"].update(ndata)
                with open("info.json","w") as f:
                    json.dump(data,f)        
            else:
                 pass
             
class ToplevelLogInWindow(ctk.CTkToplevel):
       def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("500x300")
        self.label=ctk.CTkLabel(self,text="ew")
        self.label.pack()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("my app")
        self.geometry("500x300")
        self.entry=ctk.CTkEntry(self,placeholder_text="example@gmail.com",width=200).pack(padx=10,pady=15)
        self.entry2=ctk.CTkEntry(self,placeholder_text="passward",width=200).pack(padx=10,pady=15)
        self.btn1=ctk.CTkButton(self,text="Log in",corner_radius=10,command=self.log_in).pack(padx=10,pady=10)
        self.btn2=ctk.CTkButton(self,text="Sign up",corner_radius=10,command=self.open_toplevel).pack(padx=10,pady=10)
    def log_in(self):
            ToplevelLogInWindow(self)
    def open_toplevel(self):
            ToplevelSignupWindow(self)

if __name__=="__main__" :  
    app=App()
    app.mainloop()