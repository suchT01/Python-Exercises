class Alumno():
    def datos(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
    def imprimir(self):
        print("Alumno:{}\nNota: {}".format(self.nombre,self.nota))
        if self.nota > 5:
            print("Has aprobado")
        else:
            print("Has reprobado")
alu1=Alumno()
alu1.datos("Jose",30)
alu1.imprimir()
