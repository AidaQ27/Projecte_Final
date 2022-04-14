import sqlite3
from flask import redirect, render_template, request, url_for, flash
import requests
from balance import app
from criptos.models import ProcesaDades, CriptoValorModel
from balance.forms import MovimentsFrom
from datetime import datetime

now = datetime.now()




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
        desde = request.form.get('from_coin')
        para = request.form.get('to')
         
        try:
            resposta = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey={}".format(desde,para,"05BF565B-CA92-421A-AF57-699C95894ACE"))
            # https://rest.coinapi.io/v1/exchangerate/EUR/BTC?time={}apikey=05BF565B-CA92-421A-AF57-699C95894ACE
            print((resposta.json()['rate']))
            return render_template('purchase.html', exchangerate=resposta.json()['rate'], from_coin=desde, to=para)
        except:
            print("Error")


        return redirect(url_for('inicio'))


#demana_api= CriptoValorModel
#quantitat_convertida = demana_api.obtenir_quantitat(quantitat_from)








@app.route('/status')
def estado():
    return render_template('status.html')


