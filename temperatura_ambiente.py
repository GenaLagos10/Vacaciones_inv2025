class TemperaturaAmbiente:
    def __init__(self, ubicacion, temperatura_actual):
        self.ubicacion = ubicacion
        self.__temperatura_actual = temperatura_actual

    def get_temperatura(self):
        return self.__temperatura_actual
    
    def set_temperatura(self, nueva_temp):
        if nueva_temp >= -50 and nueva_temp <= 60:
            self.__temperatura_actual = nueva_temp
            print(f"la temperatura actual es de: {self.__temperatura_actual}")
    
    def mostrar_info(self):
        print(f"ubicación: {self.ubicacion} -> temperatura actual: {self.__temperatura_actual} °C")

    

def main():


    ubicacion=input("ingrese la ciudad: ")
    nueva_temperatura=float(input("Ingrese su temperatura actual: "))
    temperatura_ambiente1 = TemperaturaAmbiente(ubicacion, nueva_temperatura) # se crea una variable donde se llama a la clase junto con las variables de los datos pedidos-atributos-
    temperatura_ambiente1.mostrar_info()

    # Ahora actualizamos la temperatura con set
    nueva_temp2 = float(input("Ingrese una nueva temperatura para actualizar: "))
    temperatura_ambiente1.set_temperatura(nueva_temp2)

    # Mostramos la temperatura actualizada
    temperatura_ambiente1.mostrar_info()




main()