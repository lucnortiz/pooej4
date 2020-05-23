from modulo_empleado import Empleado

class EmpleadoPlanta(Empleado):
    __sueldo_basico= 0
    __antiguedad= 0
    
    def __init__(self,dni,nom,direc,telef,sueldo,antig):
        super().__init__(dni,nom,direc,telef)
        self.__sueldo_basico= sueldo
        self.__antiguedad= antig
        
    def mostrar_datos(self):
        print (">>> EMPLEADO DE PLANTA <<<")
        super().mostrar_datos()
        print(f"Sueldo: {self.__sueldo_basico}\nAntiguedad (años): {self.__antiguedad}\n")
        
    def get_sueldobasico(self):
        return self.__sueldo_basico
    
    def get_antiguedad(self):
        return self.__antiguedad