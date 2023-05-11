class Universidad():
    def __init__(self,nombreu):
        self.nombreu=nombreu
    def __str__(self):
        return """
        Universidad\t{}
        """.format(self.nombreu)
class Carrera():
    def carrera(self,especialidad):
        self.especialidad=especialidad
    def __str__(self):
        return """
        Universidad\t{}
        Carrera:\t{}
        """.format(self.nombreu,self.especialidad)

class Estudiande(Universidad,Carrera):
    def estudiante(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def __str__(self):
        return """
        Universidad\t{}
        Carrera:\t{}
        Nombre E.\t{}
        Edad"\t\t{}
        """.format(self.nombreu,self.especialidad,self.nombre,self.edad)
        
persona=Estudiande("Gran Mariscal")
persona.carrera("Ingenieria en Informatica")
persona.estudiante("Jose",19)
print(persona)