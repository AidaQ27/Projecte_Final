
from select import select

from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired


class MovimentsFrom(FlaskForm):
    desde = SelectField("Desde", validators=[DataRequired(message="Falta seleccionar la moneda")])
    para = SelectField("Para", validators=[DataRequired(message="Falta seleccionar la moneda")])
    cantidad = FloatField("Cantidad", validators=[DataRequired(message="Debes introducir una cantidad")])

    calcular = SubmitField("Aceptar")