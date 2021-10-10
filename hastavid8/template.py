from flask import Flask
from flask import render_template


app = Flask(__name__)


'''
Para especificar carpeta diferente para los templates
poner al inicio en el 
app = Flask(__name__, template_folder = "nombre_carpeta")
'''

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)