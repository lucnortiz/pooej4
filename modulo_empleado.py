
class Empleado(object):
    __DNI= 0
    __nombre= ''
    __direccion= ''
    __telefono= 0
    
    def __init__(self,dni,nom,direc,telef):
        self.__DNI= dni
        self.__nombre= nom
        self.__direccion= direc
        self.__telefono= telef
        
    def mostrar_datos(self):
        print (f"DNI: {self.__DNI}\nNombre: {self.__nombre}\nDireccion: {self.__direccion}\nTelefono: {self.__telefono}")
        
    def get_DNI(self):
        return self.__DNI
    
    def get_nombre(self):
        return self.__nombre
    
    def get_direccion(self):
        return self.__direccion
    
    def get_telefono(self):
        return self.__telefono