from flask import Flask, request, render_template
from abc import ABC, abstractmethod
from clases.deporte import Deportes, Futbol, Baloncesto, Beisbol

app = Flask(__name__, template_folder='html')
@app.route("/")
def Deportes():
    return render_template('start_deportes.html')

@app.route('/deportes', methods=['GET', 'POST'])
def mostrar_deportes():
    if request.method == 'POST':
        # Obtener el deporte seleccionado por el usuario
        deporte_seleccionado = request.form['deporte']

        # Crear una instancia del deporte seleccionado
        if deporte_seleccionado == 'futbol':
            deporte = Futbol('Fútbol', 11, request.form['jugadores'], request.form['posicion_portero'])
        elif deporte_seleccionado == 'baloncesto':
            deporte = Baloncesto('Baloncesto', 5, request.form['jugadores'], request.form['altura_aro'])
        elif deporte_seleccionado == 'beisbol':
            deporte = Beisbol('Béisbol', 9, request.form['jugadores'], request.form['entrada_extra'])
        else:
            # Si el deporte seleccionado no es válido, mostrar mensaje de error
            return render_template('start_deportes.html', error=True)

        # Mostrar la plantilla con la información del deporte seleccionado
        return render_template('deportes.html', deporte=deporte)

if __name__ == '__main__':
    app.run(debug=True)