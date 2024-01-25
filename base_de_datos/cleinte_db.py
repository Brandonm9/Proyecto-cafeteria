import sqlite3

con = sqlite3.connect(r'/home/brandon/Documentos/cafeteria/base_de_datos/cliente.db')

cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_com TEXT, numero_tel INT, correo TEXT, direccion TEXT, contraseña TEXT)')


def ingresar_dato(nombre, numero, correo, direccion, contraseña):
    cur.execute('INSERT INTO clientes(nombre_com, numero_tel, correo, direccion, contraseña) VALUES(?,?,?)',
                nombre, numero, correo, direccion, contraseña)
    con.commit()
    con.close()

def validar_usuario(correo, contraseña):
    if con.execute('SELECT * FROM Clientes WHERE correo = ? AND contraseña = ?', (correo, contraseña)):
        print("si hay")
    else:
        print("no hay")
    con.close()