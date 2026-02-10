from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from db import get_connection

app = Flask(__name__)
app.secret_key = 'clave_secreta_examen_2026'


@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, created_at FROM usuarios ORDER BY id DESC")
    usuarios = cursor.fetchall()
    conn.close()
    return render_template('index.html', usuarios=usuarios)


@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form.get('nombre', '').strip()

    if not nombre:
        flash('El nombre es obligatorio.', 'danger')
        return redirect(url_for('index'))

    # Query parametrizada - protegida contra SQL injection
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nombre, email, password_hash) VALUES (?, '', '')", (nombre,))
    conn.commit()
    conn.close()

    flash('Usuario guardado.', 'success')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>', methods=['POST'])
def editar(id):
    nombre = request.form.get('nombre', '').strip()

    if not nombre:
        flash('El nombre es obligatorio.', 'danger')
        return redirect(url_for('index'))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE usuarios SET nombre = ? WHERE id = ?", (nombre, id))
    conn.commit()
    conn.close()

    flash('Usuario actualizado.', 'success')
    return redirect(url_for('index'))


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    flash('Usuario eliminado.', 'warning')
    return redirect(url_for('index'))


@app.route('/obtener/<int:id>')
def obtener(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre FROM usuarios WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return jsonify({'id': row.id, 'nombre': row.nombre})
    return jsonify({'error': 'No encontrado'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
