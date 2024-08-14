import psycopg2
from psycopg2 import sql, extras
from psycopg2 import OperationalError, Error

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="yasuniDB",
            user="postgres",
            password="admin",
            host="localhost"
        )
        return conn
    except OperationalError as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def get_nacionalidades():
    conn = connect_db()
    if conn is None:
        return []

    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT NACCODIGO, CATXNACCODIGO, NACTITULO, NACDESCRIPCION, NACURLIMAGEN, NACFECHACREACION
                FROM NACIONALIDADES
            """)
            rows = cur.fetchall()
            print(f"Datos recuperados de la base de datos: {rows}")
    except Exception as e:
        print(f"Error al obtener nacionalidades: {e}")
        return []
    finally:
        conn.close()

    nacionalidades = []
    for row in rows:
        nacionalidades.append({
            'id': row[0],
            'categoria_id': row[1],
            'titulo': row[2],
            'descripcion': row[3],
            'imagen_url': row[4],
            'fecha_creacion': row[5].strftime('%Y-%m-%d')
        })

    print(f"Nacionalidades formateadas: {nacionalidades}")
    return nacionalidades


def add_nacionalidad(data):
    conn = connect_db()
    if conn is None:
        return {'message': 'Error al conectar con la base de datos'}

    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO NACIONALIDADES (CATXNACCODIGO, NACTITULO, NACDESCRIPCION, NACURLIMAGEN, NACFECHACREACION)
                VALUES (%s, %s, %s, %s, %s)
            """, (data['categoria_id'], data['titulo'], data['descripcion'], data['imagen_url'], data['fecha_creacion']))
            conn.commit()
    except Error as e:
        conn.rollback()
        print(f"Error al añadir nacionalidad: {e}")
        return {'message': 'Error al añadir nacionalidad'}
    finally:
        conn.close()

    return {'message': 'Nacionalidad añadida correctamente'}

def update_nacionalidad(id, data):
    conn = connect_db()
    if conn is None:
        return {'message': 'Error al conectar con la base de datos'}

    try:
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE NACIONALIDADES
                SET CATXNACCODIGO = %s, NACTITULO = %s, NACDESCRIPCION = %s, NACURLIMAGEN = %s, NACFECHACREACION = %s
                WHERE NACCODIGO = %s
            """, (data['categoria_id'], data['titulo'], data['descripcion'], data['imagen_url'], data['fecha_creacion'], id))
            conn.commit()
    except Error as e:
        conn.rollback()
        print(f"Error al actualizar nacionalidad: {e}")
        return {'message': 'Error al actualizar nacionalidad'}
    finally:
        conn.close()

    return {'message': 'Nacionalidad actualizada correctamente'}

def delete_nacionalidad(id):
    conn = connect_db()
    if conn is None:
        return {'message': 'Error al conectar con la base de datos'}

    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM NACIONALIDADES WHERE NACCODIGO = %s", (id,))
            conn.commit()
    except Error as e:
        conn.rollback()
        print(f"Error al eliminar nacionalidad: {e}")
        return {'message': 'Error al eliminar nacionalidad'}
    finally:
        conn.close()

    return {'message': 'Nacionalidad eliminada correctamente'}
if __name__ == "__main__":
    nacionalidades = get_nacionalidades()
    print(nacionalidades)
