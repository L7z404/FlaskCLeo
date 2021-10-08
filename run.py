from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo'

'''
Poner debug como True para ver cambios sin volver a ejecutar el archivo
'''
if __name__ == '__main__':
    app.run(debug=True, port=8000) 
