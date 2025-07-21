from abc import ABC, abstractmethod

#Clase abstracta Entidad
class Entidad(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def descripcion(self):
        pass

#Clase abstracta Jugador
class Jugador(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def tipo_jugador(self):
        pass

#subclase de Entidad
class Heroe(Entidad):
    def __init__(self, nombre, clase, nivel):
        super().__init__(nombre)
        self.clase = clase
        self.nivel = nivel

    def descripcion(self):
        return f"{self.nombre} - Clase: {self.clase}, Nivel: {self.nivel}"


#subclase de Entidad
class Criatura(Entidad):
    def __init__(self, nombre, raza, poder):
        super().__init__(nombre)
        self.raza = raza
        self.poder = poder

    def descripcion(self):
        return f"{self.nombre} - Raza: {self.raza}, Poder: {self.poder}"


#subclase de Jugador
class Humano(Jugador):
    def __init__(self, nombre, alianza):
        super().__init__(nombre)
        self.alianza = alianza

    def tipo_jugador(self):
        return f"Humano - Alianza: {self.alianza}"

#subclase de Jugador
class IA(Jugador):
    def __init__(self, nombre, dificultad):
        super().__init__(nombre)
        self.dificultad = dificultad

    def tipo_jugador(self):
        return f"IA - Dificultad: {self.dificultad}"

class Juego:
    def __init__(self):
        self.entidades=[]  #heroes y criaturas
        self.jugadores=[]  #humanos e IA
    
    def mostrar_entidades(self):
        for entidad in self.entidades:
            print(entidad.descripcion())

    def listar_jugadores(self):
        for jugador in self.jugadores:
            print(f"{jugador.nombre} - {jugador.tipo_jugador()}")


juego = Juego()

heroe1 = Heroe("Atenea", "Guerrera", 10)
criatura1 = Criatura("Minotauro", "Bestia", "Fuerza bruta")

jugador1 = Humano("Genaro", "Luz")
jugador2 = IA("AI-BOSS", "Difícil")

juego.entidades.append(heroe1)
juego.entidades.append(criatura1)

juego.jugadores.append(jugador1)
juego.jugadores.append(jugador2)

juego.mostrar_entidades()
juego.listar_jugadores()
