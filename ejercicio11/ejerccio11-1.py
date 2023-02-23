import sqlite3

def main():
    #insertTable()
    #insertData()
    viewTable("alumnos")
    name = input("Introduce el nombre del alumno: ")
    searchAlumn(name)

def insertTable():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    def create_table():
        cursor.execute("""CREATE TABLE IF NOT EXISTS alumnos(
                                id integer PRIMARY KEY, 
                                nombre TEXT, 
                                apellidos TEXT)
                        """)
    create_table()
    cursor.close()
    conn.close()

def insertData():
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    def data_entry():
        cursor.execute("INSERT INTO alumnos VALUES(1,'Oscar', 'Menendez Fernandez')")
        cursor.execute("INSERT INTO alumnos VALUES(2,'Roberto', 'Garcia Perez')")
        cursor.execute("INSERT INTO alumnos VALUES(3,'Sergio', 'Menendez Garcia')")
        cursor.execute("INSERT INTO alumnos VALUES(4,'Juanjo', 'Rodriguez Garcia')")
        cursor.execute("INSERT INTO alumnos VALUES(5,'Juan', 'Perez Garcia')")
        cursor.execute("INSERT INTO alumnos VALUES(6,'Rebeca', 'Rodriguez Fernandez')")
        cursor.execute("INSERT INTO alumnos VALUES(7,'Maria', 'Garcia Fernandez')")
        cursor.execute("INSERT INTO alumnos VALUES(8,'Oscar', 'Perez Fernandez')")
        conn.commit()
    data_entry()
    cursor.close()
    conn.close()
def viewTable(table):
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()

    row = cursor.execute(f"SELECT * FROM {table}")

    cursor.close()
    conn.close()

def searchAlumn(name):
    nombre = name
    conn = sqlite3.connect('datos.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM alumnos WHERE nombre='{nombre}';"

    rows = cursor.execute(query)
    data = rows.fetchall()
    for alumn in data:
        print(alumn[1] + " " + alumn[2])

    cursor.close()
    conn.close()



if __name__ == '__main__':
    main()