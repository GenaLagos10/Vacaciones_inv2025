class Usuario:
    contador_usuarios=0
    def __init__(self, nombre, mail, clave):
        self.nombre = nombre
        self.mail = mail
        self._clave = clave
        self.__class__.contador_usuarios += 1


    def verificar_clave(self, clave):
        return self._clave == clave

    def cambiar_clave(self, clave_antigua, clave_nueva):
        if clave_antigua == self._clave and len(clave_nueva) > 7:
            tiene_mayus=False
            tiene_num=False

            for char in clave_nueva:
                if char.isupper():
                    tiene_mayus = True
                elif char.isdigit():
                    tiene_num = True
            
            if not tiene_mayus or not tiene_num:
                return "la clave debe contener al menos una mayúsculas y un número"
            else:
                self._clave = clave_nueva
                return True, "Contraseña válida"
                
        else:
            return False, "la clave antigua es incorrecta o la clave nueva tiene menos de 8 carácteres"
                          

    def __str__(self):
        return f"Usuario: {self.nombre} Mail: {self.mail}"
    
    @property
    def clave(self):
        return self._clave
    
    @clave.setter
    def clave(self, clave_nueva):
        raise AttributeError("No puedes cambiar la clave directamente. Usa cambiar_clave().")

class Empleado(Usuario):
    def __init__(self, nombre, mail, clave, cargo, sueldo):
        super().__init__(nombre, mail, clave)
        self.cargo = cargo
        self.sueldo = sueldo


    def trabajar(self):
        return f"{self.nombre} esta trabajando como {self.cargo}"
    
    def __str__(self):
        base = super().__str__()
        return f"{base} Cargo: {self.cargo} Sueldo: {self.sueldo}"


def describir_usuario(usuario):
    print("Información del usuario:")
    print(usuario)  # Esto ya llama automáticamente al __str__ correspondiente




usuario1 = Usuario("Ana", "ana@mail.com", "abcdE1234")
empleado1 = Empleado("Luis", "luis@empresa.com", "Nomejodas76543", "Analista", 850000)

describir_usuario(usuario1)
print()
describir_usuario(empleado1)
