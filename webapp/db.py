import os
import psycopg2

DATABASE_URL = os.environ.get('DATABASE_URL')

def create_tables():
    pass
    # conn = None
    # cur = None
    
    # try:
    #     conn = psycopg2.connect(DATABASE_URL)
    #     cur = conn.cursor()
    #     conn.commit()

    # except Exception as e:
    #         if conn is not None:
    #             conn.rollback()
    #         return f"Database error: {e}"

    # finally:
    #     if cur is not None:
    #         cur.close()
    #     if conn is not None:
    #         conn.close()