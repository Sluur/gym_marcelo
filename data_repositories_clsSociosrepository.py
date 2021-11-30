import data_clsConexion

from datetime import datetime

class clsSocioRepository: 

        def __init__(self):
                self.bd= data_clsConexion.clsConexion()

        def getAll(self):
                query = "SELECT s.Id, s.Apellido, s.Nombre, s.Dni, s.Telefono, s.FechaNac, s.Sexo, s.Observaciones, s.Baneado, s.Rutina_Id FROM SOCIO s ;"
               # query = "SELECT iris.id, iris.sepalLength, iris.sepalWidth, iris.petalLength, iris.petalWidth, iris.idType, iristype.description FROM iris INNER JOIN iristype ON iris.idType=iristype.id;"
                result = self.bd.run_query(query)

                if (len(result)==0):
                        return None
                else:
                        return result
        def getFiltered(self, texto):
                texto = "%"+texto.upper()+"%"
                query = "SELECT s.Id, s.Apellido, s.Nombre, s.Dni, s.Telefono, s.FechaNac, s.Sexo, s.Observaciones, s.Baneado, s.Rutina_Id FROM SOCIO s where UCASE(s.Apellido) like '%s' or UCASE(s.Nombre) like '%s' or UCASE(s.Dni) like '%s';"%(texto,texto,texto)
                result = self.bd.run_query(query)
                if (len(result)==0):
                        return None
                else:
                        return result      
        def getDNI(self, dni):
                query = "SELECT s.Id, s.Apellido, s.Nombre, s.Dni, s.Telefono, s.FechaNac, s.Sexo, s.Observaciones, s.Baneado, s.Rutina_Id FROM SOCIO s WHERE s.Dni like '%s';"%(dni)
                result = self.bd.run_query(query)
                if(len(result)==0):
                        return None
                else:
                        return result
        def insert(self, apellido, nombre, dni, telefono, fechanac, sexo, observaciones, baneado, rutinaid):                
                
                #query = 'INSERT INTO socio (Apellido,Nombre,Dni,Telefono, FechaNac, Sexo, Observaciones, Baneado, rutina_Id) VALUES ('%s','%s', '%d', '%d', '%s', '%d', '%s', '%d', '%d');"%(apellido, nombre, dni, telefono, fechanac, sexo, observaciones, baneado, rutinaid)
                
                query = "INSERT INTO socio (Apellido,Nombre,Dni,Telefono, FechaNac, Sexo, Observaciones, Baneado, rutina_Id) VALUES ('%s','%s', '%d', '%d', '%s', '%s', '%s', '%d', '%d');"%(apellido, nombre, dni, telefono, fechanac, sexo, observaciones, baneado, rutinaid)
                self.bd.run_query(query)


        def delete(self, ID):
                query = "DELETE FROM socio WHERE id= " + str(ID) + ";"
                self.bd.run_query(query)

        def update(self, ID, apellido, nombre, dni, telefono, fechanac, sexo, observaciones, baneado, rutinaid):
                from datetime import datetime

                formatted_date = fechanac.strftime('%Y-%m-%d %H:%M:%S')
                query = "UPDATE socio SET Apellido ='%s', Nombre='%s', Dni='%d', Telefono='%d', Fechanac ='%s', Sexo ='%d', Observaciones ='%s'petalWidth='%s', Baneado ='%d', rutinaid='%d' WHERE id = '%d';"%(apellido, nombre, dni, telefono, datetime.now(), sexo, observaciones, baneado, rutinaid, ID)  
                self.bd.run_query(query)
        
        def get(self, ID):
                query = "SELECT s.Id, s.Apellido, s.Nombre, s.Dni, s.Telefono, s.FechaNac, s.Sexo, s.Observaciones, s.Baneado, s.Rutina_Id FROM socio where  id =" + str(ID) + ";"
        