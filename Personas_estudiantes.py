class Persona:
    def __init__(self, nombre, edad, rut):
        if edad <= 0 or edad >= 120:
            raise ValueError("La edad debe mayor que 0 y menor que 120")
        if not rut:
            raise ValueError("El RUT no puede estar vacío")
        
        self.nombre = nombre
        self._edad = edad
        self.__rut = rut


    def __str__(self):
        return f"Nombre: {self.nombre}, edad: {self._edad}, RUT: {self.__rut}"
    
    def __eq__(self, other):
        if not isinstance(other, Persona):
            return NotImplemented
        return self.__rut == other.__rut
    
    def get_rut(self):
        return self.__rut
    
    def set_rut(self, nuevo_rut):
        if not nuevo_rut:
            raise ValueError("El RUT no puede estar vacío")
        self.__rut = nuevo_rut

        
class Profesor(Persona):

    def __init__(self, nombre, edad, rut, departamento):
        super().__init__(nombre, edad, rut)
        self.departamento = departamento

    def __str__(self):
        return f"{super().__str__()} Departamento: {self.departamento}"



class MiembroDuoc(Persona):
    def __init__(self, nombre, edad, rut, sede, id_duoc):
        super().__init__(nombre, edad, rut)
        self.sede = sede
        self.id_duoc = id_duoc
    
    def __str__(self):
        return f"{super().__str__()} Sede: {self.sede} ID_DUOC: {self.id_duoc}"


class Estudiante(MiembroDuoc):

    def __init__(self, nombre, edad, rut, carrera, sede, id_duoc):
        super().__init__(nombre, edad, rut, sede, id_duoc)
        self.carrera = carrera
    
    def __str__(self):
        return f"{super().__str__()}, carrera: {self.carrera}"
    
    def es_mayor_de_edad(self):
        if self._edad >= 18:
            return True
        else:
            return False


        
p1 = Profesor("Luis", 45, "11222333-4", "Matemáticas")
e1 = Estudiante("Ana", 20, "11222333-4", "Ingeniería")  # mismo RUT

print("¿Profesor y estudiante son la misma persona?", p1 == e1)  # True

p1.set_rut("99887766-5")
print(p1.get_rut())


