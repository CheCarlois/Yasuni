from cruds.dao_acces.conexion import Conexion
from cruds.modelos.Turisticas import Turisticas

class TuristicaDAO:
    SELECCIONAR = 'SELECT * FROM TURISTICAS'
    INSERTAR = 'INSERT INTO TURISTICAS (CATXTURCODIGO, TURTITULO, TURDESCRIPCION, TURURLIMAGEN, TURFECHACREACION) VALUES (%s, %s, %s, %s, %s)'
    ACTUALIZAR = 'UPDATE TURISTICAS SET CATXTURCODIGO=%s, TURTITULO=%s, TURDESCRIPCION=%s, TURURLIMAGEN=%s, TURFECHACREACION=%s WHERE TURCODIGO=%s'
    ELIMINAR = 'DELETE FROM TURISTICAS WHERE TURCODIGO=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            turisticos = []
            for registro in registros:
                turistico = Turisticas(
                    registro[0], registro[1], registro[2],
                    registro[3], registro[4], registro[5]
                )
                turisticos.append(turistico)
            return turisticos
        except Exception as e:
            print(f'Ocurrió un error al seleccionar turisticos: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, turistico):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (
                turistico.categoria_codigo,
                turistico.titulo, turistico.descripcion,
                turistico.url_imagen, turistico.fecha_creacion
            )
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al insertar turisticos: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, turistico):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (
                turistico.categoria_codigo, turistico.titulo,
                turistico.descripcion, turistico.url_imagen,
                turistico.fecha_creacion, turistico.codigo
            )
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al actualizar turistico: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, turistico):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (turistico.codigo,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrió un error al eliminar turistico: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
