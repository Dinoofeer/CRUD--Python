import pyodbc

DB_CONFIG = {
    'server': 'SQL5106.site4now.net',
    'database': 'db_a34a77_capecac',
    'username': 'db_a34a77_capecac_admin',
    'password': 'qwer7410',
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
