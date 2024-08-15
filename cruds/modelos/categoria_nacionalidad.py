class CategoriaNacionalidad:
    def __init__(self, codigo=None, nombre=None):
        self.codigo = codigo
        self.nombre = nombre

    def __str__(self):
        return f'Codigo: {self.codigo}, Nombre: {self.nombre}'
