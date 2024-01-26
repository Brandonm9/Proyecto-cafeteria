import sqlite3

#cur.execute('CREATE TABLE IF NOT EXISTS clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre_com TEXT, numero_tel INT, correo TEXT, direccion TEXT, contraseña TEXT)')

def ingresar_dato(nombre, numero, correo, direccion, contraseña):
    con = sqlite3.connect(r'/home/brandon/Documentos/cafeteria_copia/base_de_datos/cliente.db')
    cur = con.cursor()
    cur.execute('INSERT INTO clientes VALUES(NULL,?,?,?,?,?)',
                (nombre, numero, correo, direccion, contraseña))
    print("Se a completado el ingreso de datos")
    con.commit()
    con.close()

def validar_usuario(correo, contraseña):
    con = sqlite3.connect(r'/home/brandon/Documentos/cafeteria_copia/base_de_datos/cliente.db')
    cur = con.cursor()
    cur.execute('SELECT * FROM Clientes WHERE correo = ? AND contraseña = ?', (correo, contraseña))
    if cur.fetchone():
        print("si hay")
        resultado = True
    else:
        resultado = False
    con.close()
    return resultado