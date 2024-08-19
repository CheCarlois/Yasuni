from flask import Flask, render_template, jsonify, request, flash, redirect, url_for
from crudNacionalidades import get_nacionalidades, add_nacionalidad, update_nacionalidad, delete_nacionalidad
from cruds.logica_aplicacion.NacionalidadForm import NacionalidadForm
from cruds.modelos.nacionalidad import Nacionalidad
from cruds.dao_acces.nacionalidad_dao import NacionalidadDAO
from cruds.modelos.Turisticas import Turisticas
from cruds.dao_acces.turistica_dao import TuristicaDAO
from cruds.logica_aplicacion.TuristicaForm import TuristicaForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a2b9c8d4e6f1g7h5i3j2k4l6m5n7o8p9'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienesSomos')
def quienesSomos():
    return render_template('quienesSomos.html')

@app.route('/masInformacion')
def masInformacion():
    return render_template('masInformacion.html')

@app.route('/paginaActividades')
def pagina_actividades():
    return render_template('paginaActividades.html')


@app.route('/login')
def login():
    return render_template('login.html')

# Integración de la lógica CRUD de NACIONALIDADES
@app.route('/api/nacionalidades', methods=['GET'])
def api_get_nacionalidades():
    nacionalidades = get_nacionalidades()
    print(f"api_get_nacionalidades: {nacionalidades}")  # Verificar lo que devuelve
    return jsonify(nacionalidades)


@app.route('/api/nacionalidades', methods=['POST'])
def api_add_nacionalidad():
    data = request.get_json()
    result = add_nacionalidad(data)
    return jsonify(result), 201

@app.route('/api/nacionalidades/<int:id>', methods=['PUT'])
def api_update_nacionalidad(id):
    data = request.get_json()
    result = update_nacionalidad(id, data)
    return jsonify(result)

@app.route('/api/nacionalidades/<int:id>', methods=['DELETE'])
def api_delete_nacionalidad(id):
    result = delete_nacionalidad(id)
    return jsonify(result)

@app.route('/paginaActividades/infoNacionalidad', methods=['GET', 'POST'])
def informacion_nacionalidad():
    form = NacionalidadForm()
    if form.validate_on_submit():
        # Lógica para procesar los datos del formulario
        nueva_nacionalidad = Nacionalidad(
            categoria_codigo=form.categoria.data,
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            url_imagen=form.imagenURL.data,
            fecha_creacion='2024-08-15'  # O la fecha actual
        )
        NacionalidadDAO.insertar(nueva_nacionalidad)
        flash('Información de la nacionalidad guardada con éxito!')
        return redirect(url_for('informacion_nacionalidad'))
    else:
        # Obtener las nacionalidades existentes para mostrarlas en la tabla
        nacionalidades = NacionalidadDAO.seleccionar()
        return render_template('gestionarNacionalidad.html', form=form, nacionalidades=nacionalidades)


@app.route('/paginaActividades/infoTuristica', methods=['GET', 'POST'])
def informacion_turismo():
    form = NacionalidadForm()
    if form.validate_on_submit():
        # Lógica para procesar los datos del formulario
        nueva_turistico = Turisticas(
            categoria_codigo=form.categoria.data,
            titulo=form.titulo.data,
            descripcion=form.descripcion.data,
            url_imagen=form.imagenURL.data,
            fecha_creacion='2024-08-15'  # O la fecha actual
        )
        TuristicaDAO.insertar(nueva_turistico)
        flash('Información de turismo guardada con éxito!')
        return redirect(url_for('informacion_turismo'))
    else:
        # Obtener las nacionalidades existentes para mostrarlas en la tabla
        turisticos = TuristicaDAO.seleccionar()
        return render_template('gestionarTurismo.html', form=form, turisticos=turisticos)


if __name__ == '__main__':
    app.run(debug=True)
