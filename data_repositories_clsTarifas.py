import data_clsConexion

from datetime import datetime

class clsMembresiasRepository: 

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
        def insert(self, tarifanueva, fechaalta):                
                
                query = "INSERT INTO tarifa (Precio, FechaAlta) VALUES ('%d','%s');"%(tarifanueva, fechaalta)
                self.bd.run_query(query)

        def getActive(self):
            query = "SELECT s.Id,s.Precio FROM tarifa s WHERE s.FechaBaja IS NULL;"
            result = self.bd.run_query(query)
            print(result[0][0])
            if(len(result)==0):
                    return None
            else:
                    return result
        def delete(self, ID):
                query = "DELETE FROM socio WHERE id= " + str(ID) + ";"
                self.bd.run_query(query)

        def update(self, fechabaja, ID):

                query = "UPDATE tarifa SET FechaBaja='%s' WHERE id = '%s';"%(fechabaja, ID)  
                self.bd.run_query(query)
        
        def get(self, ID):
                query = "SELECT s.Id, s.Apellido, s.Nombre, s.Dni, s.Telefono, s.FechaNac, s.Sexo, s.Observaciones, s.Baneado, s.Rutina_Id FROM socio where  id =" + str(ID) + ";"
        