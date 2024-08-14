from cruds.conexion import Conexion
from cruds.nacionalidad import Nacionalidad

class NacionalidadDAO:
    SELECCIONAR = 'SELECT * FROM NACIONALIDADES'
    INSERTAR = 'INSERT INTO NACIONALIDADES (NACCODIGO, CATXNACCODIGO, NACTITULO, NACDESCRIPCION, NACURLIMAGEN, NACFECHACREACION) VALUES (%s, %s, %s, %s, %s, %s)'
    ACTUALIZAR = 'UPDATE NACIONALIDADES SET CATXNACCODIGO=%s, NACTITULO=%s, NACDESCRIPCION=%s, NACURLIMAGEN=%s, NACFECHACREACION=%s WHERE NACCODIGO=%s'
    ELIMINAR = 'DELETE FROM NACIONALIDADES WHERE NACCODIGO=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            nacionalidades = []
            for registro in registros:
                nacionalidad = Nacionalidad(
                    registro[0], registro[1], registro[2],
                    registro[3], registro[4], registro[5]
                )
                nacionalidades.append(nacionalidad)
            return nacionalidades
        except Exception as e:
            print(f'Ocurrió un error al seleccionar nacionalidades: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, nacionalidad):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (
                nacionalidad.codigo, nacionalidad.categoria_codigo,
                nacionalidad.titulo, nacionalidad.descripcion,
                nacionalidad.url_imagen, nacionalidad.fecha_creacion
            )
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
    def actualizar(cls, nacionalidad):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (
                nacionalidad.categoria_codigo, nacionalidad.titulo,
                nacionalidad.descripcion, nacionalidad.url_imagen,
                nacionalidad.fecha_creacion, nacionalidad.codigo
            )
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar nacionalidad: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, nacionalidad):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (nacionalidad.codigo,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar nacionalidad: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
