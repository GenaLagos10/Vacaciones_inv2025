
class Cancion:
    def __init__(self, titulo, artista, duracion):
        if duracion <=0:
            raise ValueError("La duracion debe ser mayor a 0 segundos")
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        return f"🎵 {self.titulo} - {self.artista} ({self.duracion} segundos)"
    
    def __len__(self):
        return self.duracion

    
try:
    c1 = Cancion("Imagine", "John Lennon", 183)
    print(c1)
    print(len(c1))
except ValueError as e:
    print(f"Error: {e}")

try:
    c2 = Cancion("Canción rara", "Alguien", -50)
    print(c2)
    print(len(c2))
except ValueError as e:
    print(f"Error: {e}")

