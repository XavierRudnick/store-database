import mysql.connector

__cnx = None

def get_sql_connection():
    """
        Connects mysql app to vscode interface
        :return: connection variable
        """
    global __cnx
    if __cnx == None:
        __cnx = mysql.connector.connect(user='root', password='Quailn!2',
                                host='127.0.0.1',
                                database='app')
    return __cnx
        