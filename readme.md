## Tecnologias Utilizadas para esta App
- Python
- Flask 2.1.1
- Jinja
- Flask - WTF 1.0.1 
- Sqlite - BBDD
- Bulma


# App Web - Registro de movimientos de criptomonedas

En la App hacemos un registro de compra/venta de criptos, para jugar con los valores para ver si podemos hacer crecer nuestra inversión.

## Páginas

**1) Principal** - Se muestra la tabla con los movimientos (compras y conversiones de criptomonedas) realizadas por el usuario.
Si no hay movimientos resgistrados se mostrará un mensaje, que no existen movimientos.

**2) Purchase** - Nos muestra un formulario en que podemos realizar una compra, venta o intercambio de monedas. Previamente a la compra, se hara una llamada a la API para saber el valor de la conversión en el  momento actual.

**3) Status** - Muestra por pantalla el estado actual de la inversión, y el valor actual del total de las criptomonedas que existen en el
stock del usuario. Al final se muestra el total de euros invertidos, desde el inicio.


# Intrucciones a seguir al descargar el proyecto
### **Crea tu entorno virtual**

```
python -m venv venv
```

### Activa tu entorno virtual

```
venv\Scripts\activate
```
### Instala las dependencias

```
pip install -r requeriments.txt
```

## **ApiKey**

Debes pedir una ApiKey a la página [coinApi.io](https://www.coinapi.io/)
Y debes:

### Copiar el fichero
```
criptos/configtemplate.py
```

### Introducir tu APIKEY en el nuevo fichero.
```
API_KEY = "Tu ApiKey aqui"
```

### Renombrar el fichero a 'config.py'

## Para arrancar la App, ejecuta en el terminal:
```
flask run
```


**Este proyecto ha sido realizado por:**
[Aida Queralt](https://github.com/AidaQ27)
