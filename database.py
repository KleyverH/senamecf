import os
import psycopg2
from dotenv import load_dotenv

# Cargamos las variables del .env
load_dotenv()

def get_db_connection():
    """
    Crea y devuelve una conexión a la base de datos PostgreSQL
    utilizando las credenciales del archivo .env.
    """
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT')
        )
        return conn
    except Exception as e:
        print(f"❌ Error crítico al conectar a la DB: {e}")
        return None

def execute_query(query, params=None, fetch=False):
    """
    Función auxiliar para ejecutar SQL de forma segura.
    """
    conn = get_db_connection()
    if conn is None:
        return None
    
    try:
        cur = conn.cursor()
        cur.execute(query, params)
        
        result = None
        if fetch:
            result = cur.fetchall()
            
        conn.commit()
        cur.close()
        return result
    except Exception as e:
        print(f"❌ Error en la consulta: {e}")
        conn.rollback()
        return None
    finally:
        conn.close()