from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>/')
def user(name='Leonel'):
    #render_template('archivo.html', variablenombreusarenhtml = variablepython)
    age = 21
    my_list=[1,2,3,4]
    return render_template('user.html', nombre=name, edad=age, lista=my_list)

if __name__ == '__main__':
    app.run(debug=True, port=8000)