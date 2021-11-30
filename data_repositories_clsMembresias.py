import data_clsConexion

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