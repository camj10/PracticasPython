print("Bienvenido!A continuacion ingrese los datos correspondientes")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
curso = int(input("Curso: "))
porcAsist= int(input("Porcentaje de asistencia: "))
modalidad = input("Modalidad de clase (P-S-D) ")
puntaje = int(input("Puntaje de la materia: "))
if(modalidad=='D' or modalidad=='d'):
    if(puntaje>=90):
        print(f"{nombre} {apellido} no aprobó por falta de puntaje")
    else:
        print("No aprobó")
elif(modalidad=='P' or modalidad=='p'):
    if(porcAsist>=80): 
        if(puntaje>=80):
            print("Aprobó la materia")
        else:
            print("No aprobó por falta de puntaje")
    else: 
        print("No aprobó por falta de asistencia")
elif(modalidad=='S' or modalidad=='s'):
    if(porcAsist>=50):
        if(puntaje>=85):
            print("Aprobó la materia")
        else:
            print("No aprobó por falta de puntaje")
    else: 
        print("No aprobó por falta de asistencia")
else:
    print("Modalidad ingresada INCORRECTA")