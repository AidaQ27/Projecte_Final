from flask import render_template
from balance import app



@app.route('/')
def inicio():
    llista_moviments = []
    fitxer_mv = open('data/moviments.csv', 'r')

#--------------------------------------------------
    linia = fitxer_mv.readline()
    while linia != '':
        camps = linia.split(',')
        llista_moviments.append(
            {
                'fecha': camps[0],
                'hora': camps[1],
                'from': camps[2],
                'Qfrom': float(camps[3]),
                'to': camps[4],
                'Qto': float(camps[5]),
                'precio': float(camps[6])
            }
        )
        linia = fitxer_mv.readline()
#-------------------------------------------------

    fitxer_mv.close()
    return render_template('principal.html', moviments = llista_moviments)


@app.route('/purchase')
def compra():
    return render_template('purchase.html')





@app.route('/status')
def estado():
    return render_template('status.html')


