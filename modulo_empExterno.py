from modulo_empleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea= ''
    __fecha_ini= ''
    __fecha_fin= ''
    __monto_viatico= 0
    __costo_obra= 0
    __monto_seguro= 0
    
    def __init__(self,dni,nom,direc,telef,tarea,fechaIni,fechaFin,montoViatico,costoObra,montoSeguro):
        super().__init__(dni,nom,direc,telef)
        self.__tarea= tarea
        self.__fecha_inicio= fechaIni
        self.__fecha_fin= fechaFin
        self.__monto_viatico= montoViatico
        self.__costo_obra= costoObra
        self.__monto_seguro= montoSeguro
        
    def get_monto_viatico(self):
        return self.__monto_viatico
    
    def get_costo_obra(self):
        return self.__costo_obra
    
    def get_monto_seguro(self):
        return self.__monto_seguro
    
    def get_tarea(self):
        return self.__tarea