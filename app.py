from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/pagina1/')
def pagina1():
    return render_template("pagina1.html")


@app.route('/pagina2/')
def pagina2():
    return render_template("pagina2.html")

@app.route('/potencia/<int:base>/<exponente>',methods=["GET","POST"])
def potencia(base,exponente):
    exponente=int(exponente)
    if exponente>0:
        res = base**exponente
    elif exponente==0:
        res = 1
    elif exponente<0:
        res = base**exponente
    else:
        abort(404)
    return render_template("potencia.html",base=base,exponente=exponente,resultado=res)
app.run("0.0.0.0",8000,debug=True)