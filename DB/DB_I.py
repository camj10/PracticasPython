import mysql.connector
#Importación de librerías para mostrar los resultados en tabla, con la técnica del pivot
import sqlalchemy
import pymysql
import mysql.connector as sql
import pandas as pd
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="practica",
)
mycursor= mydb.cursor()
condicion= int(input("Presione 1 para cargar datos: "))
# Cargo mis datos en la DB
while condicion:
    seccionDato = input("Seccion (I-A-C-T): ").upper()#.upper() para pasar todo a mayúscula
    sucursalDato = input("Sucursal (E-A-C): ").upper()
    sueldoDato = int(input("Sueldo: "))
    sql="INSERT INTO sueldo(seccion,sucursal,salario) values (%s,%s,%s)"
    val=(seccionDato,sucursalDato,sueldoDato)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"Insertado")
    condicion= int(input("Presione 1 para seguir cargando"))
#Segunda parte: Sumar, obtener y mostrar los datos de la DB
# sentencia="SELECT sum(salario),sucursal,seccion FROM `sueldo` GROUP BY sucursal,seccion ORDER BY sucursal,seccion"
# mycursor.execute(sentencia)
# myresult= mycursor.fetchall()
#Tabla con pandas
db_connection_str = 'mysql+pymysql://root:@localhost/practica'
db_connection = sqlalchemy.create_engine(db_connection_str)
df = pd.read_sql_query('SELECT * FROM sueldo', con=db_connection)
print(df.head())

output = pd.pivot_table(data=df, index=['seccion'], columns=['sucursal'], values='salario', aggfunc='sum')
print(output)
