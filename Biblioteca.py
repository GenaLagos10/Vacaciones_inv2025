class Biblioteca:
    def __init__(self):
        self._materiales=[]

    def agregar_material(self, material):
        self._materiales.append(material)

    def mostrar_materiales(self):
        for mat in self._materiales:
            print(mat.descripcion())

class Material():
    def __init__(self, titulo, autor):
        self._titulo=titulo
        self._autor=autor

    def descripcion(self):
        return f"{self._titulo}, por {self._autor}"
    
# Subclase Libro
class Libro(Material):
    def __init__(self, titulo, autor, paginas):
        super().__init__(titulo, autor)
        self._paginas = paginas

    def descripcion(self):
        return f"Libro: {super().descripcion()} - {self._paginas} páginas"

# Subclase Revista
class Revista(Material):
    def __init__(self, titulo, autor, edicion):
        super().__init__(titulo, autor)
        self._edicion = edicion

    def descripcion(self):
        return f"Revista: {super().descripcion()} - Edición {self._edicion}"



libro1 = Libro("1984", "George Orwell", 328)
revista1 = Revista("National Geographic", "Varios", "Julio 2025")

biblio = Biblioteca()
biblio.agregar_material(libro1)
biblio.agregar_material(revista1)

biblio.mostrar_materiales()
