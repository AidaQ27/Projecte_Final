import sqlite3
from flask import redirect, render_template, request, url_for, flash
import requests
from balance import app
from criptos.models import ProcesaDades
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

    if request.method == 'GET':
        return render_template('purchase.html')
    else:
        desde = request.form.get('from_coin')
        para = request.form.get('to')
        cantidadf = request.form.get('cantidadf')
        print(request.form['action'])
        if request.form['action'] == 'Calcular':
            # PRIMERO CONSULTAR BD PARA SABER SI HAY SUFICIENTE DE ESE TOKEN

            try:
                resposta = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey={}".format(desde,para,"05BF565B-CA92-421A-AF57-699C95894ACE"))
                # https://rest.coinapi.io/v1/exchangerate/EUR/BTC?time={}apikey=05BF565B-CA92-421A-AF57-699C95894ACE
                # print((resposta.json()['rate']))
                # return render_template('purchase.html', exchangerate=resposta.json()['rate'], from_coin=desde, to=para)
                print('desde', desde, 'para', para)
                return render_template('purchase.html', exchangerate=resposta, from_coin=desde, to=para, cantidadf=cantidadf)
            except:
                print("Error")
        elif request.form['action'] == 'Borrar':
            return render_template('purchase.html', exchangerate=None, from_coin='EUR', to='EUR', cantidadf=None)
        elif request.form['action'] == 'Guardar':
            print('saving')
            now = datetime.now()
            dt_date = now.strftime("%d-%m-%Y")
            dt_time = now.strftime("%H:%M:%S")
            print(dt_date, dt_time)
            con = sqlite3.connect('data/movimientos.db')
            con.execute(
                'insert into moviments (fecha,hora,moneda_from,cantidad_from,moneda_to,cantidad_to,precio) values (?,?,?,?,?,?,?)',
                (
                    dt_date,
                    dt_time,
                    request.form.get('from_coin', type=str),
                    request.form.get('cantidadf', type=float),
                    request.form.get('to', type=str),
                    request.form.get('cantidadf', type=float),
                    request.form.get('0.04', type=str),
                )
            )
            con.commit()  # IMPRESCINDIBLE HACER COMMIT DESPUES DE INSERTAR

        return redirect(url_for('inicio'))








@app.route('/status')
def estado():

    data_manager = ProcesaDades()
    
    try:
        dades = data_manager.lee_movimientos()
        return render_template('status.html', coins=dades)
    except sqlite3.Error as e:
        flash('Existe un error en la base de datos. Intentalo de nuevo más tarde')
        return render_template('status.html', coins=[])



#@app.route('/creartabla')
#def crear_tabla():
    #ProcesaDades.crear_tabla()

@app.route('/kevin')
def kevin():
    ProcesaDades.insertar_monedas()