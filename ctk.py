import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
window=ctk.CTk()
window.configure()
window.title("test")
window.geometry('600x400')
label=ctk.CTkLabel(window,
                   text=".w.",
                   fg_color="blue",
                   text_color="white",
                   corner_radius=10)
label.pack()

button=ctk.CTkButton(window,text="按鈕"
                     ,corner_radius=10
                     ,fg_color="#FF0"
                     ,text_color="#000"
                     ,hover_color="AA0")
button.pack()

window.mainloop()
