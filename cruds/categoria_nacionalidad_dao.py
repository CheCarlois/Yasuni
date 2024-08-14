from cruds.conexion import Conexion
from cruds.categoria_nacionalidad import CategoriaNacionalidad

class CategoriaNacionalidadDAO:
    SELECCIONAR = 'SELECT * FROM CATEGORIASNACIONALIDADES'
    INSERTAR = 'INSERT INTO CATEGORIASNACIONALIDADES (CATXNACCODIGO, CATXNACNOMBRE) VALUES (%s, %s)'
    ACTUALIZAR = 'UPDATE CATEGORIASNACIONALIDADES SET CATXNACNOMBRE=%s WHERE CATXNACCODIGO=%s'
    ELIMINAR = 'DELETE FROM CATEGORIASNACIONALIDADES WHERE CATXNACCODIGO=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            categorias = []
            for registro in registros:
                categoria = CategoriaNacionalidad(registro[0], registro[1])
                categorias.append(categoria)
            return categorias
        except Exception as e:
            print(f'Ocurrió un error al seleccionar categorías: {e}')
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
