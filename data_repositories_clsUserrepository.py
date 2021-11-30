
import data_clsConexion

class clsUserRepository: 

        def __init__(self):
                self.bd= data_clsConexion.clsConexion()

        def getAll(self):
                query = "SELECT ID, nombre, Password, email  FROM usuario;"
               # query = "SELECT iris.id, iris.sepalLength, iris.sepalWidth, iris.petalLength, iris.petalWidth, iris.idType, iristype.description FROM iris INNER JOIN iristype ON iris.idType=iristype.id;"
                result = self.bd.run_query(query)

                if (len(result)==0):
                        return None
                else:
                        return result
        def getFiltered(self, texto):
                texto = "%"+texto.upper()+"%"
                query = "SELECT ID, nombre, Password, email from usuario where UCASE(nombre) like '%s' or UCASE(email) like '%s';"%(texto,texto)
                result = self.bd.run_query(query)
                if (len(result)==0):
                        return None
                else:
                        return result
        
        def validate(self, user, psw):
                query = "SELECT nombre FROM usuario WHERE Email = '%s' AND password ='%s';"%(user,psw)
                result = self.bd.run_query(query)                                
                if (len(result)==0):
                        return False
                else:
                        return True
                        
                
        def insert(self, sepalL, sepalW, petalL, petalW, idT):
                query = "INSERT INTO usuario (sepalLength, sepalWidth, petalLength, petalWidth, idType) VALUES ('%s','%s','%s','%s','%d');"%(sepalL, sepalW, petalL, petalW, idT)          
                self.bd.run_query(query)


        def delete(self, ID):
                query = "DELETE FROM usuario WHERE id= " + str(ID) + ";"
                self.bd.run_query(query)

        def update(self, ID, sepalL, sepalW, petalL, petalW, idT):
                query = "UPDATE usuario SET sepalLength ='%s', sepalWidth='%s', petalLength='%s', petalWidth='%s', idType='%d' WHERE id = '%d';"%(sepalL, sepalW, petalL, petalW, idT, ID)  
                self.bd.run_query(query)
        
        def get(self, ID):
                query = "SELECT * FROM usuario where  id =" + str(ID) + ";"
        