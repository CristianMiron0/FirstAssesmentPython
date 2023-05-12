from abc import ABC, abstractmethod

class Deportes(ABC):
    def __init__(self, nombre, jugadores):
        self.nombre = nombre
        self.jugadores = jugadores

    @abstractmethod
    def descripcion(self):
        pass

class Futbol(Deportes):
    def __init__(self, nombre, jugadores, posicion_arquero):
        super().__init__(nombre, jugadores)
        self.posicion_arquero = posicion_arquero

    def descripcion(self):
        return f"El fútbol es un deporte de equipo con {self.jugadores} jugadores, donde el arquero se coloca en la posición {self.posicion_arquero}."

class Baloncesto(Deportes):
    def __init__(self, nombre, jugadores, altura_aro):
        super().__init__(nombre, jugadores)
        self.altura_aro = altura_aro

    def descripcion(self):
        return f"El baloncesto es un deporte de equipo con {self.jugadores} jugadores, donde el aro se encuentra a una altura de {self.altura_aro} metros."

class Beisbol(Deportes):
    def __init__(self, nombre, jugadores, entrada_extra):
        super().__init__(nombre, jugadores)
        self.entrada_extra = entrada_extra

    def descripcion(self):
        return f"El béisbol es un deporte de equipo con {self.jugadores} jugadores, donde en caso de empate se puede jugar una entrada extra, conocida como {self.entrada_extra}."
