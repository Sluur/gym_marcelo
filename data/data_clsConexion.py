import MySQLdb

# https://askubuntu.com/questions/989965/how-to-connect-to-mysql-db-from-python-3-on-16-04


class clsConexion:        

        def __init__(self, DB_HOST = '127.0.0.1', DB_USER='root', DB_PASS='delphi4PHP', DB_NAME='marceloGym'):
                self.datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
                self.conn = MySQLdb.connect(*self.datos)
                self.cursor = self.conn.cursor()


        def run_query(self,query=''):
                self.cursor.execute(query)
                if query.upper().startswith('SELECT'):
                        data = self.cursor.fetchall()
                        
                else:
                        self.conn.commit()
                        data=None
                return data

        def close(self):
                self.cursor.close()
                self.conn.close()

