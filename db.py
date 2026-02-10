import pyodbc

# Configuracion del usuario RESTRINGIDO (no es admin)
DB_CONFIG = {
    'server': 'localhost',
    'database': 'crud_examen',
    'username': 'app_crud_login',
    'password': 'CrudApp2026!',
}


def get_connection():
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']};"
    )
    return pyodbc.connect(conn_str)
