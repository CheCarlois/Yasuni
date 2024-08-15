class Nacionalidad:
    def __init__(self, codigo=None, categoria_codigo=None, titulo=None, descripcion=None, url_imagen=None, fecha_creacion=None):
        self.codigo = codigo
        self.categoria_codigo = categoria_codigo
        self.titulo = titulo
        self.descripcion = descripcion
        self.url_imagen = url_imagen
        self.fecha_creacion = fecha_creacion

    def __str__(self):
        return (f'Codigo: {self.codigo}, Categoria Codigo: {self.categoria_codigo}, '
                f'Titulo: {self.titulo}, Descripcion: {self.descripcion}, '
                f'URL Imagen: {self.url_imagen}, Fecha Creacion: {self.fecha_creacion}')
