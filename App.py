from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Conexion MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Jenny'
app.config['MYSQL_PASSWORD'] = '1004682677'
app.config['MYSQL_DB'] = 'full_stack'
mysql = MySQL(app)

# Configuraciones
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM mascotas')
    data = cur.fetchall()
    return render_template('index.html', mascotas = data)

# Agregar mascota
@app.route('/add_mascota', methods=['POST'])
def add_mascota():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        descripcion = request.form['descripcion']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO mascotas (nombre, edad, descripcion) VALUES (%s, %s, %s)', 
        (nombre, edad, descripcion))
        mysql.connection.commit()
        flash('Mascota agregada satisfactoriamente')
        return redirect(url_for('Index'))

#Editar mascota
@app.route('/editar/<int:id>')
def get_mascota(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM mascotas WHERE id = %s', (id,))
    data = cur.fetchall()
    return render_template('editar_mascota.html', mascota = data[0])

@app.route('/editar/<int:id>', methods=['POST'])
def editar_mascota(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        descripcion = request.form['descripcion']
        cur = mysql.connection.cursor()
        cur.execute("""
         UPDATE mascotas
            SET nombre = %s,
                    edad = %s,
                    descripcion = %s
            WHERE id = %s        
        """, (nombre, edad, descripcion, id))
        # Ejecutar la consulta
        mysql.connection.commit()
        flash('Mascota actualizada satisfactoriamente')
        return redirect(url_for('Index'))

# Eliminar mascota
@app.route('/eliminar/<string:id>')
def delete_mascota(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM mascotas WHERE id = %s', (id,))  # Usa parametrización
    mysql.connection.commit()
    flash('Mascota eliminada correctamente')
    return redirect(url_for('Index'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)