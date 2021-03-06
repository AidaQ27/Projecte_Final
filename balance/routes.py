import sqlite3
from flask import redirect, render_template, request, url_for, flash
import requests
from balance import app
from criptos.models import ProcesaDades
from criptos.config import API_KEY
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

            try:
                resposta = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey={}".format(para,desde, API_KEY))
                
                rate = resposta.json()['rate']  
                rate = "{:.6f}".format(rate)
                cantidad_total = float(rate) * float(cantidadf)
                return render_template('purchase.html', exchangerate=rate, from_coin=desde, to=para, cantidadt=cantidad_total, missatge=None)
            except:
                return render_template('purchase.html', exchangerate=None, from_coin='EUR', to='EUR', cantidadf=None, cantidadt=0, missatge="Error al conectar con la API")
        
        elif request.form['action'] == 'Borrar':
            return render_template('purchase.html', exchangerate=None, from_coin='EUR', to='EUR', cantidadf=None, cantidadt=0, missatge=None)
        elif request.form['action'] == 'Guardar':
            # Asegura que hi han suficients monedes per comprar
            from_coin = request.form.get('from_coin')

            if from_coin != "EUR" and ProcesaDades.get_cantidad_monedas(from_coin)[0] < float(cantidadf):
                return render_template('purchase.html', exchangerate=None, from_coin='EUR', to='EUR', cantidadf=None, cantidadt=0, missatge="No hay suficientes fondos de la moneda elegida")
            elif desde == para:
                return render_template('purchase.html', exchangerate=None, from_coin=desde, to=para, cantidadf=None, cantidadt=0, missatge="No se puede comprar la misma moneda")

            else:
                now = datetime.now()
                dt_date = now.strftime("%d-%m-%Y")
                dt_time = now.strftime("%H:%M:%S")
                try:
                    resposta = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/{}?apikey={}".format(para,desde,API_KEY))   
                    rate = resposta.json()['rate'] 
                except:
                    return render_template('purchase.html', exchangerate=None, from_coin='EUR', to='EUR', cantidadf=None, cantidadt=0, missatge="Error al conectar con la API")

                rate = "{:.6f}".format(rate)
                cantidad_total = float(rate) * float(cantidadf)

                con = sqlite3.connect('data/movimientos.db')
                con.execute(
                    'insert into moviments (fecha,hora,moneda_from,cantidad_from,moneda_to,cantidad_to,precio) values (?,?,?,?,?,?,?)',
                    (
                        dt_date,
                        dt_time,
                        request.form.get('from_coin', type=str),
                        cantidad_total,
                        request.form.get('to', type=str), 
                        request.form.get('cantidadf', type=float),
                        rate,
                    )
                )
                con.commit()  

                ProcesaDades.comprar_moneda(cantidadf, request.form.get('to'))
                if request.form.get('from_coin') == "EUR":
                    ProcesaDades.comprar_moneda(round(cantidad_total, 2), "Total Euros")
                else: 
                    ProcesaDades.comprar_moneda(-cantidad_total, request.form.get('from_coin'))
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



