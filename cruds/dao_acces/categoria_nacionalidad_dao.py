from cruds.dao_acces.conexion import Conexion


class CategoriaNacionalidadDAO:
    SELECCIONAR = 'SELECT * FROM CATEGORIASNACIONALIDADES'
    INSERTAR = 'INSERT INTO NACIONALIDADES (CATXNACCODIGO, NACTITULO, NACDESCRIPCION, NACURLIMAGEN, NACFECHACREACION) VALUES (%s, %s, %s, %s, %s)'
    ACTUALIZAR = 'UPDATE CATEGORIASNACIONALIDADES SET CATXNACNOMBRE=%s WHERE CATXNACCODIGO=%s'
    ELIMINAR = 'DELETE FROM CATEGORIASNACIONALIDADES WHERE CATXNACCODIGO=%s'

    @classmethod
    def insertar(cls, nacionalidad):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (nacionalidad.categoria, nacionalidad.titulo, nacionalidad.descripcion,
                       nacionalidad.url_imagen, nacionalidad.fecha_creacion)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar nacionalidad: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, categoria):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (categoria.codigo, categoria.nombre)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar categoría: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, categoria):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (categoria.nombre, categoria.codigo)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar categoría: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, categoria):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (categoria.codigo,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar categoría: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
