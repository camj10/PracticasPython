import tkinter
import customtkinter 

def buttonConvertir_function():
    print("button pressed")
    e_textPeso = float(entryPeso.get())
    e_textAltura = float(entryAltura.get())
    imc = e_textPeso / ( e_textAltura*e_textAltura)
    if(imc<18.4): 
        LabelIMC.configure(text= "Insuficiencia ponderal/Bajo peso con IMC "+str(round(imc,2)))
    elif(imc<25):
        LabelIMC.configure(text= "Peso normal "+str(round(imc,2)))
    elif(imc<30):
        LabelIMC.configure(text= "Sobrepeso "+str(round(imc,2)))
    elif(imc<35):
        LabelIMC.configure(text= "Obesidad grado I "+str(round(imc,2)))
    elif(imc<40):
        LabelIMC.configure(text= "Obesidad grado II "+str(round(imc,2)))
    else:
        LabelIMC.configure(text= "Obesidad grado III o morbida "+str(round(imc,2)))

root_tk = tkinter.Tk()
root_tk.geometry("400x240")
root_tk.title("CustomTkinter Test")
LabelMensaje = customtkinter.CTkLabel(master=root_tk,
                                text="Calculadora de IMC",
                                width=120,
                                height=25,
                                corner_radius=8
)
buttonConvertir = customtkinter.CTkButton(master= root_tk,
                                text="Calcular",
                                corner_radius=10,
                                command= buttonConvertir_function
)
LabelMensajePeso = customtkinter.CTkLabel(master=root_tk,
                                text="Ingrese peso en kg: ",
                                width=120,
                                height=25,
                                corner_radius=8
)
entryPeso = customtkinter.CTkEntry(master=root_tk,
                                width=120,
                                height=25,
                                corner_radius=8
)
LabelMensajeAltura = customtkinter.CTkLabel(master=root_tk,
                                text="Ingrese altura en metros:",
                                width=120,
                                height=25,
                                corner_radius=8
)
entryAltura = customtkinter.CTkEntry(master=root_tk,
                                width=120,
                                height=25,
                                corner_radius=8
)
LabelIMC = customtkinter.CTkLabel(master=root_tk,
                                width=120,
                                height=25,
                                corner_radius=8
)
LabelMensaje.place(relx=0.5, rely=0.1, anchor= tkinter.CENTER)
LabelMensajePeso.place(relx=0.5, rely=0.2, anchor= tkinter.CENTER)
entryPeso.place(relx=0.5, rely=0.3, anchor= tkinter.CENTER)
LabelMensajeAltura.place(relx=0.5, rely=0.4, anchor= tkinter.CENTER)
entryAltura.place(relx=0.5, rely=0.5, anchor= tkinter.CENTER)
buttonConvertir.place(relx=0.5, rely=0.6, anchor= tkinter.CENTER)
LabelIMC.place(relx=0.5, rely=0.7, anchor= tkinter.CENTER)
root_tk.mainloop()
