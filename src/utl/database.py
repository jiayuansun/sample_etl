import os

class DataBase:
    def __init__(self):
        pass
    def get_db_conn(self):
        pass
    def exec_sql(self, sql, conn):
        sql_str = ""
        with open(os.path.dirname(__file__) + f'/../sql/{sql}.sql') as f:
            sql_str = f.readlines()
        
        rec = conn.execute(sql_str)
        return rec