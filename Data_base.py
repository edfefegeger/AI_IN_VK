import psycopg2
from Variables import dbname, user, password, host, port

def insert_into_table(val1, val2, val3):
    conn = psycopg2.connect(
        dbname = dbname,
        user = user,
        password=password,
        host=host,  
        port=port 
    )


    cursor = conn.cursor()


    insert_query = """
    INSERT INTO vk VALUES (%s, %s, %s) 
    """

    cursor.execute(insert_query, (val1, val2, val3))
    conn.commit()
    cursor.close()
    conn.close()



