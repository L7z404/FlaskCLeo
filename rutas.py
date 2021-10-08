from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo'

@app.route('/params')
def params():
    param = request.args.get('params1', 'no conteine este parametro')
    param2 = request.args.get('params2', 'no conteine param 2')
    return 'El parametro es: {}\nEl otro es: {}'.format(param, param2)


if __name__ == '__main__':
    app.run(debug=True, port=8000)


#Vas en el video 5 del curso Leo...