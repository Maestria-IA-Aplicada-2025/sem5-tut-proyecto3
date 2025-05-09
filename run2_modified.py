
from flask import Flask, render_template, request, jsonify  # Importar render_template para manejar plantillas HTML

import joblib  # joblib se usa para cargar el modelo de machine learning previamente entrenado y guardado
import pickle  # pickle se utiliza para cargar objetos serializados, en este caso el vectorizador

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')  # Renderiza el formulario HTML

# Ruta de predicción, que recibe el mensaje del formulario
@app.route('/predict', methods=['POST'])  # Solo acepta solicitudes POST
def predict():
    if request.method == 'POST':
        mensaje = request.form['mensaje']  # Obtiene el mensaje enviado desde el formulario
        
        # Se imprime el mensaje recibido para depuración
        print(mensaje)
        
        # El vectorizador transforma el mensaje recibido en el formato adecuado para el modelo
        m = vector.transform([mensaje])  # 'mensaje' se transforma en una representación numérica adecuada para el modelo
        
        # El modelo realiza la predicción sobre el mensaje transformado
        prediction = clf.predict(m)  # Se realiza la predicción utilizando el modelo cargado
        
        # Devuelve la predicción como respuesta JSON
        return jsonify({'prediction': list(prediction)})  # La predicción se convierte en una lista y se devuelve como respuesta JSON

# Esta parte asegura que el código solo se ejecute cuando se ejecuta directamente (no cuando se importa como módulo)
if __name__ == '__main__':
    # Carga del modelo de machine learning desde un archivo pickle
    clf = joblib.load('model01.pkl')  # Se carga el modelo previamente entrenado usando joblib
    
    # Carga del vectorizador (que convierte el texto en vectores numéricos) desde un archivo pickle
    vector = pickle.load(open("vector.pickel", "rb"))  # Se carga el vectorizador previamente guardado con pickle
    
    # Se ejecuta la aplicación Flask en el puerto 8080
    app.run(port=8080)  # Flask inicia la aplicación en el puerto 8080 para que esté disponible para recibir solicitudes
