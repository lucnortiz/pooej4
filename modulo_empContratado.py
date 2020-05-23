from modulo_empleado import Empleado

class EmpleadoContratado(Empleado):
    __fecha_inicio= ''
    __fecha_fin= ''
    __cant_horas_trabajadas= 0
    __valor_por_hora= 0
    
    def __init__ (self,dni,nom,direc,telef,fecha_ini,fecha_fin,cant_horas_tr,valor_hora):
        super().__init__(dni,nom,direc,telef)
        self.__fecha_inicio= fecha_ini
        self.__fecha_fin= fecha_fin
        self.__cant_horas_trabajadas= cant_horas_tr
        self.__valor_por_hora= valor_hora
        
    def mostrar_datos(self):
        print (">>> EMPLEADO CONTRATADO <<<")
        super().mostrar_datos()
        print(f"Fecha Inicio: {self.__fecha_inicio}\nFecha Fin: {self.__fecha_fin}\nCantidad de Horas Trabajadas: {self.__cant_horas_trabajadas}\nValor por Hora: {self.__valor_por_hora}\n")
        
    def aumentar_cant_horas_trabajadas(self,h):
        self.__cant_horas_trabajadas += h
        
    def get_cant_horas_trabajadas(self):
        return self.__cant_horas_trabajadas
    
    def get_valor_hora(self):
        return self.__valor_por_hora