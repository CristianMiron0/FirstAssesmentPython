from flask import Flask, request, render_template
from abc import ABC, abstractmethod
from clases.deporte import Deportes, Futbol, Baloncesto, Beisbol

app = Flask(__name__, template_folder='html')
@app.route("/")
def start():
    return render_template('start_deportes.html')

@app.route('/deportes', methods=['POST'])
def mostrar_deportes():
    # Obtener el deporte seleccionado por el usuario
    deporte_seleccionado = request.form['deporte']
    print(deporte_seleccionado)

    # Crear una instancia del deporte seleccionado
    if deporte_seleccionado == 'Futbol':
        deporte = Futbol('Futbol', request.form['jugadores'], request.form['posicion_portero'])
    elif deporte_seleccionado == 'Baloncesto':
        deporte = Baloncesto('Baloncesto', request.form['jugadores'], request.form['altura_aro'])
    elif deporte_seleccionado == 'Beisbol':
        deporte = Beisbol('Beisbol',request.form['jugadores'], request.form['entrada_extra'])
    else:
        # Si el deporte seleccionado no es válido, mostrar mensaje de error
        return render_template('start_deportes.html', error=True)

    # Mostrar la plantilla con la información del deporte seleccionado
    return render_template('deportes.html', deporte=deporte)

if __name__ == '__main__':
    app.run(debug=True)
