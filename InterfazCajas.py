import tkinter
import customtkinter # <- import the CustomTkinter module


def functionSumar():
    print("button pressed")
    textoAProyectar = int(Label._text)+1
    Label.configure(text= textoAProyectar)
    if(Label._text==10):
        Label.configure(text=0)
        LabelDer.configure(text=int(LabelDer._text)+1)
        
def functionRestar():
    print("button pressed")
    textoAProyectar = int(Label._text)-1
    Label.configure(text= textoAProyectar)
    if(Label._text==-10):
        Label.configure(text=0)
        LabelIzq.configure(text=int(LabelIzq._text)+1)

    
root_tk = tkinter.Tk() 
root_tk.geometry("800x480")
root_tk.title("CustomTkinter Test")

buttonRestar = customtkinter.CTkButton(master=root_tk,
                            text= " + ",
                            width=20,
                            height=30,
                            corner_radius=30,
                            command=functionSumar)

buttonSumar = customtkinter.CTkButton(master=root_tk,
                            text= " - ",
                            width=20,
                            height=30,
                            corner_radius=30,
                            command=functionRestar)


Label = customtkinter.CTkLabel(master=root_tk,
                            text='0',
                            width=120,
                            height=25,
                            corner_radius=8)

LabelDer = customtkinter.CTkLabel(master=root_tk,
                            text='0',
                            width=120,
                            height=25,
                            corner_radius=8)

LabelIzq = customtkinter.CTkLabel(master=root_tk,
                            text='0',
                            width=120,
                            height=25,
                            corner_radius=20)

Label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
LabelDer.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)
LabelIzq.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
buttonSumar.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
buttonRestar.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

root_tk.mainloop()