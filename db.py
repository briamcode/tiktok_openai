import sqlite3

# Conectar a la base de datos SQLite
conexion = sqlite3.connect("cola_lifo.db")

# Crear una tabla para la cola
conexion.execute("CREATE TABLE IF NOT EXISTS cola (id INTEGER PRIMARY KEY AUTOINCREMENT, elemento TEXT)")

# Insertar un elemento en la cola
def insertar_elemento(elemento):
    conexion.execute("INSERT INTO cola (elemento) VALUES (?)", (elemento,))
    conexion.commit()

# Extraer y eliminar el elemento inferior de la cola
def extraer_elemento():
    cursor = conexion.execute("SELECT id, elemento FROM cola ORDER BY id ASC LIMIT 1")
    elemento = cursor.fetchone()
    if elemento:
        conexion.execute("DELETE FROM cola WHERE id = ?", (elemento[0],))
        conexion.commit()
        return elemento[1]
    else:
        return None



# Ejemplo de uso
#insertar_elemento("Elemento 1")
#insertar_elemento("Elemento 2")
#insertar_elemento("Elemento 3")

#elemento_extraido = extraer_elemento()
#print("Elemento extraído:", elemento_extraido)

# Cerrar la conexión a la base de datos
#conexion.close()
