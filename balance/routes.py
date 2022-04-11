import sqlite3
from flask import redirect, render_template, request, url_for, flash
from balance import app
from criptos.models import ProcesaDades, CriptoValorModel
from balance.forms import MovimentsFrom




@app.route('/')
def inicio():

    data_manager = ProcesaDades()
    
    try:
        dades = data_manager.recupera_dades_moviments()
        return render_template('principal.html', moviments=dades)
    except sqlite3.Error as e:
        flash('Existe un error en la base de datos. Intentalo de nuevo más tarde')
        return render_template('principal.html', moviments=[])




@app.route('/purchase', methods=['GET', 'POST'])
def compra():

    """
    form = MovimentsFrom()
    return render_template("purchase.html", formulario=form)
    """


    if request.method == 'GET':
        return render_template('purchase.html')
    else:
        desde = request.form.get('from')
        para = request.form.get('to')
        quantitat_from = request.form.get('cantidadf')
        calcular = request.form['calcular']


        return redirect(url_for('inicio'))


#demana_api= CriptoValorModel
#quantitat_convertida = demana_api.obtenir_quantitat(quantitat_from)








@app.route('/status')
def estado():
    return render_template('status.html')


