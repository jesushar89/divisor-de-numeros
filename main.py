class DivisorCalculator:
    def __init__(self):
        self.numero = None

    def leer_numero(self):
        while True:
            try:
                # Leer el número desde la entrada del usuario
                entrada = input("Por favor, ingrese un número natural: ")

                # Intentamos convertirlo a entero
                numero = int(entrada)

                # Verificamos si es un número natural
                if numero <= 0:
                    raise ValueError("Debe ingresar un número natural positivo.")

                # Si todo es correcto, guardamos el número y salimos del bucle
                self.numero = numero
                break
            except ValueError as e:
                # Capturamos cualquier error de conversión o validación
                print(f"Error: {e}. Inténtelo nuevamente.")

    def calcular_divisores(self):
        # Si no hay un número definido, no podemos calcular divisores
        if self.numero is None:
            raise Exception("No se ha ingresado ningún número.")

        # Generar la lista de divisores
        divisores = [i for i in range(1, self.numero + 1) if self.numero % i == 0]
        return divisores

    def mostrar_divisores(self):
        # Calculamos y mostramos los divisores
        divisores = self.calcular_divisores()
        print(f"Los divisores de {self.numero} son: {divisores}")


# Crear una instancia de la clase y ejecutar la aplicación
if __name__ == "__main__":
    # Instanciamos el objeto DivisorCalculator
    calculadora = DivisorCalculator()

    # Leemos un número natural
    calculadora.leer_numero()

    # Mostramos los divisores del número
    calculadora.mostrar_divisores()
