import psycopg2
from psycopg2 import pool, OperationalError

class Conexion:
    DATABASE = 'yasuniDB'
    USERNAME = 'postgres'
    PASSWORD = 'admin'
    DB_PORT = '5432'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # Se crea el objeto pool
            try:
                cls.pool = pool.SimpleConnectionPool(
                    1,  # Min connections in the pool
                    cls.POOL_SIZE,  # Max connections in the pool
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE
                )
                print(f'Pool creado exitosamente: {cls.POOL_NAME}')
                return cls.pool
            except OperationalError as e:
                print(f'Ocurrió un error al obtener el pool: {e}')
                return None
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        pool = cls.obtener_pool()
        if pool:
            return pool.getconn()
        else:
            raise Exception("No se pudo obtener una conexión del pool")

    @classmethod
    def liberar_conexion(cls, conexion):
        pool = cls.obtener_pool()
        if pool:
            pool.putconn(conexion)

    @classmethod
    def cerrar_pool(cls):
        pool = cls.obtener_pool()
        if pool:
            pool.closeall()

if __name__ == '__main__':
    # Creación del objeto pool y obtención de una conexión
    cnx1 = Conexion.obtener_conexion()
    print(cnx1)
    Conexion.liberar_conexion(cnx1)
    Conexion.cerrar_pool()
