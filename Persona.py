class Persona:

    def __init__(self, nombre, apellido, email, edad): #A través de init INICIALIZAMOS nuestra instancia. SELF incluye toda la información sobre el objeto individual
        #nombre = "Juana", apellido = "De Arco", email = "juana@codingdojo.com", edad = 20
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad
        self.lineas_codigo = 0

    def cumpleaños(self): #self = elena
        self.edad += 1 #elena.edad = 31
        print("¡Muchas felicidades!")

    def codificar(self, abc):
        #self = elena, cantidad_lineas = 45
        self.lineas_codigo += abc
