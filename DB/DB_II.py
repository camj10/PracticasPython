import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Ejemplo",
)
c=0
print("Sistema Libros")
while c==0:
    print("A - Agregar")
    print("B- Borrar")
    print("A - Actualizar")
    print("L - Listar")

    operacion=input("Ingrese la accion: ")
    if operacion=="A":
        isbn=input("Isbn: ")
        titulo=input("Titulo: ")
        autor=input("Autor: ")
        generos=input("Generos: ")
        idiomas=input("Idioma: ")
        mycursor = mydb.cursor()
        sql = "INSERT INTO libros (isbn, titulo, autor,generos,idiomas) VALUES (%s, %s,%s, %s, %s)"
        val = (isbn, titulo, autor, generos,idiomas)
        mycursor.execute(sql, val)
        mydb.commit()
        print("Insertado")
        # print(mycursor.rowcount, "Insertado")
    if operacion=="B":
        isbn=input("Ingrese el isbn del libro que desee borrar: ")
        mycursor = mydb.cursor()
        sql = "DELETE FROM libros where isbn=%s"
        val = (isbn,)
        
        mycursor.execute(sql)
        mydb.commit()
    if operacion=="A":
        isbn = input("Ingrese el isbn del libro que desee actualizar: ")
        titulo = input("titulo: ")
        autor = input("Autor: ")
        generos = input("generos: ")
        idiomas = input("Idioma: ")

        mycursor = mydb.cursor()
        val (titulo,autor,generos,idiomas)
        
        sql = "update libros set"
        mycursor.execute(sql, val)
        mydb.commit()
    if operacion=="L":
            mycursor.execute( "SELECT* FROM isbn,autor,titulo, autor, genero,idioma")
            myresult = mycursor.fetchall()
            print("Los datos del libro son: ")
            for x in myresult:
                print(x)
    cond=input("Cerrar programa= 1 Seguir utilizando=0: ")
    if (cond):
        c=1
    else: c=0