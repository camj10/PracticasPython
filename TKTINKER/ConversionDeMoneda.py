import tkinter
import customtkinter 

def buttonConvertir_function():
    print("button pressed")
    e_text= int(entry.get())
    LabelDolar.configure(text= str(round(e_text/7200,2)) +" dolares")
    LabelPeso.configure(text= str(round(e_text/20,2)) +" pesos")
    LabelReal.configure(text= str(round(e_text/1300,2)) +" reales")

root_tk = tkinter.Tk()
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")
LabelMensaje = customtkinter.CTkLabel(master=root_tk,
                                text="Conversor de Gs a monedas extranjeras",
                                width=120,
                                height=25,
                                corner_radius=8
)
buttonConvertir = customtkinter.CTkButton(master= root_tk,
                                text="Mostrar conversiones",
                                corner_radius=10,
                                command= buttonConvertir_function
)
entry = customtkinter.CTkEntry(master=root_tk,
                                width=120,
                                height=25,
                                corner_radius=8
)
LabelDolar = customtkinter.CTkLabel(master=root_tk,
                                text="Dolar",
                                width=120,
                                height=25,
                                corner_radius=8
)
LabelPeso = customtkinter.CTkLabel(master=root_tk,
                                text="Peso",
                                width=120,
                                height=25,
                                corner_radius=8
)
LabelReal = customtkinter.CTkLabel(master=root_tk,
                                text="Real",
                                width=120,
                                height=25,
                                corner_radius=8
)
LabelMensaje.place(relx=0.5, rely=0.2, anchor= tkinter.CENTER)
entry.place(relx=0.5, rely=0.4, anchor= tkinter.CENTER)
buttonConvertir.place(relx=0.5, rely=0.6, anchor= tkinter.CENTER)
LabelDolar.place(relx=0.5, rely=0.7, anchor= tkinter.CENTER)
LabelPeso.place(relx=0.5, rely=0.8, anchor= tkinter.CENTER)
LabelReal.place(relx=0.5, rely=0.9, anchor= tkinter.CENTER)
root_tk.mainloop()
