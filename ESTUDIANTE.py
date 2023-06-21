from Persona import Persona


class Estudiante(Persona):
    contador_estudiante = 0

    def __init__(self, cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera, id_estudiante, nivel):
        super().__init__(cedula, nombre, apellido, email, telefono, direccion, numero_libros, activo, carrera)
        self.id_estudiante = id_estudiante
        self.nivel = nivel
        Estudiante.contador_estudiante += 1

    def get_id_estudiante(self):
        return self.id_estudiante

    def set_id_estudiante(self, id_estudiante):
        self.id_estudiante = id_estudiante

    def get_nivel(self):
        return self.nivel

    def set_nivel(self, nivel):
        self.nivel = nivel

    def pedir_libro(self):
        return True

    def devolver_libro(self):
        return True