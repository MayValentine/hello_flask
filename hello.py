from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hola") #decorador. Va a hacer la funcion accesible desde el servidor
def primeraentrada():
    return "Hola, mundo"


@app.route("/adios")
def salida():
    return "Hasta luego, Mari Carmen!!!"

"""
@app.route("/romano/<numero>")
def romano(numero):
    return "el numero romano de numero es " + str(numero)
"""

@app.route("/doble/<numero>") #si ponemos int:numero esta restringiendo a numeros int
def doble(numero):
    return str(numero * 2)

@app.route("/primerhtml")
def primerhtml():
    return render_template("hola.html")
