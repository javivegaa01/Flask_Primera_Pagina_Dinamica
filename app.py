from flask import Flask, render_template,abort
app = Flask(__name__)
from lxml import etree


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
def calcular_potencia(base,exponente):
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

@app.route('/cuenta/<palabra>/<letras>',methods=["GET","POST"])
def cuenta_letra(palabra,letras):
    if len(letras)!=1:
        abort(404)
    else:
        num_veces=palabra.count(letras)
    return render_template("palabras.html",palabra=palabra,letras=letras,num_veces=num_veces)

@app.route('/libro/<int:codigo>',methods=["GET","POST"])
def buscar_codigo(codigo):
    doc=etree.parse("libros.xml")
    if str(codigo) in doc.xpath('/biblioteca/libro/codigo/text()'):
        titulo = doc.xpath('/biblioteca/libro[codigo/text()=''%s'']/titulo/text()' % codigo)[0]
        autor = doc.xpath('/biblioteca/libro[codigo/text()=''%s'']/autor/text()' % codigo)[0]
    else:
        abort(404)
    return render_template("biblioteca.html",titulo=titulo,autor=autor)
app.run(debug=True)