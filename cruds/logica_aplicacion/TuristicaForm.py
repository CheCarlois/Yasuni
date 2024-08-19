from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.fields.simple import StringField, URLField
from wtforms.validators import DataRequired
app = Flask(__name__)
app.secret_key = 'a2b9c8d4e6f1g7h5i3j2k4l6m5n7o8p9'

class TuristicaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    categoria = StringField('Categoría', validators=[DataRequired()])
    descripcion = TextAreaField('Descripción', validators=[DataRequired()])
    imagenURL = URLField('URL de la Imagen', validators=[DataRequired()])
    submit = SubmitField('Guardar')


@app.route('/paginaActividades/infoTuristica', methods=['GET', 'POST'])
def informacion_turistica():
    form = TuristicaForm()
    if form.validate_on_submit():
        # Procesar los datos del formulario
        flash('Información turistica guardada con éxito!')
        return redirect(url_for('informacion_turistica'))
    # Pasar el formulario y cualquier otro dato necesario a la plantilla
    return render_template('gestionarTurismo.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
