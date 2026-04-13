from flask import Flask, render_template, jsonify
from database import get_db_connection, execute_query

app = Flask(__name__)

# Ruta principal: Sirve el HTML desde la carpeta /templates
@app.route('/')
def home():
    return render_template('index.html')

# --- Rutas de la API: Sirve Para devolverlo los datos al HTML ---
@app.route('/api/perfiles', methods=['GET'])
def get_perfiles():
    query = "SELECT * FROM segperfiles"
    datos = execute_query(query, fetch=True)
    
    if datos is None:
        return jsonify({"error": "Error al consultar la base de datos"}), 500
    
    # Formateamos los datos para el frontend
    perfiles = [{"id": f[0], "Perfil": f[1]} for f in datos]
        
    return jsonify(perfiles)

if __name__ == '__main__':
    app.run(debug=True, port=5000)