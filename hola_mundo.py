from flask import Flask

app = Flask(__name__) #Crear instancia

@app.route('/') #la ruta
def index():
    return 'Hola Mundo'
    
app.run() #Ejecutar el servidor