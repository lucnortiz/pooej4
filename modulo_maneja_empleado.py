from modulo_empleado import Empleado
from modulo_empPlanta import EmpleadoPlanta
from modulo_empContratado import EmpleadoContratado
from modulo_empExterno import EmpleadoExterno
import csv

class ManejaEmpleado:
    __empleados= None
    
    def __init__(self):
        self.__empleados= []
    
    def carga_empleados_planta(self):
        archivo_emp_planta = open('Planta.csv')
        reader= csv.reader(archivo_emp_planta,delimiter=',')
        
        for fila in reader:
            emp= EmpleadoPlanta(int(fila[0]), fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]))
            self.__empleados.append(emp)
        archivo_emp_planta.close()  
            
    def carga_empleados_contratados(self):
        archivo_emp_contratados = open('Contratados.csv')
        reader= csv.reader(archivo_emp_contratados,delimiter=',')
        
        for fila in reader:
            emp= EmpleadoContratado(int(fila[0]), fila[1], fila[2], int(fila[3]), fila[4], fila[5], int(fila[6]), int(fila[7]))
            self.__empleados.append(emp)
        archivo_emp_contratados.close() 
        
    def carga_empleados_externos(self):
        archivo_emp_externos = open('Externos.csv')
        reader= csv.reader(archivo_emp_externos,delimiter=',')
        
        for fila in reader:
            emp= EmpleadoExterno(int(fila[0]), fila[1], fila[2], int(fila[3]), fila[4], fila[5], fila[6], int(fila[7]), int(fila[8]), int(fila[9]))
            self.__empleados.append(emp)
        archivo_emp_externos.close() 
    
    def mostrarDatos(self):
        for i in range(len(self.__empleados)):
            self.__empleados[i].mostrar_datos()
    
    def aumentar_horas(self,dni):
        band= False
        i= 0
        while (i < len(self.__empleados) and band == False):
            if type(self.__empleados[i]) == EmpleadoContratado:
                if (dni == self.__empleados[i].get_DNI()):
                    h= int(input("Ingrese la cantidad de horas trabajadas: "))
                    if (h > 0):
                        self.__empleados[i].aumentar_cant_horas_trabajadas(h)
                        band = True
                    else:
                        print ("Dato Incorrecto")
            i+=1
                    
        if (band == False):
            print ("DNI no encontrado entre los empleados Contratados")
        else:
            print ("Cantidad de Horas Aumentada")
            
    def mostrar_monto_tarea(self):        
        band= False
        i= 0
        tarea= input("Ingrese tarea a buscar: ")
        while (i < len(self.__empleados) and band == False):
            if type(self.__empleados[i]) == EmpleadoExterno:
                if tarea == self.__empleados[i].get_tarea():
                    print (f"Monto de obra para {self.__empleados[i].get_tarea()}: {self.__empleados[i].get_costo_obra()}")
                    band= True
            i+=1
    
        if (band == True):
            pass
        else:
            print ("Tarea no encontrada")
    
    def ayuda(self):
        print (">>> Empleados que necesitan ayuda\n")
        for i in range(len(self.__empleados)):
            
            if type(self.__empleados[i]) == EmpleadoPlanta:
                sueldo= self.calcula_sueldo_planta(i)
                
            elif type(self.__empleados[i]) == EmpleadoContratado:
                sueldo= self.calcula_sueldo_contratados(i)
                
            elif type(self.__empleados[i]) == EmpleadoExterno:
                sueldo= self.calcula_sueldo_externos(i)
                
            if (sueldo < 25000):
                print (f"${sueldo}")
                print (f"Nombre: {self.__empleados[i].get_nombre()}")
                print (f"DNI: {self.__empleados[i].get_DNI()}")
                print (f"Direccion: {self.__empleados[i].get_direccion()}")
                print ("\n")
                
    def mostrar_sueldos(self):
        for i in range(len(self.__empleados)):
            if type(self.__empleados[i]) == EmpleadoPlanta:
                    sueldo= self.calcula_sueldo_planta(i)
                    
            elif type(self.__empleados[i]) == EmpleadoContratado:
                    sueldo= self.calcula_sueldo_contratados(i)
                    
            elif type(self.__empleados[i]) == EmpleadoExterno:
                    sueldo= self.calcula_sueldo_externos(i)
                
            print (f"Sueldo: ${sueldo}")
            print (f"Nombre: {self.__empleados[i].get_nombre()}")
            print (f"Telefono: {self.__empleados[i].get_telefono()}")
            print ("\n")
            
            
    def calcula_sueldo_planta(self,i):
        sueldo_basico= self.__empleados[i].get_sueldobasico()
        antiguedad= self.__empleados[i].get_antiguedad()
        sueldo_total= float(sueldo_basico + (sueldo_basico*antiguedad*1/100))
        return sueldo_total
    
    def calcula_sueldo_contratados(self,i):
        cantidad_horas_trabajadas= self.__empleados[i].get_cant_horas_trabajadas()
        valor_hora= self.__empleados[i].get_valor_hora()
        sueldo= float(cantidad_horas_trabajadas * valor_hora)
        return sueldo
        
    def calcula_sueldo_externos(self,i):
        costo_obra= self.__empleados[i].get_costo_obra()
        viatico= self.__empleados[i].get_monto_viatico()
        seguro= self.__empleados[i].get_monto_seguro()
        sueldo= int(costo_obra - viatico - seguro)
        return sueldo


        # Sueldo = costo de la obra - viático- monto del seguro de vida




        
        
        