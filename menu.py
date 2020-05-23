class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            0:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op, empleado):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(empleado)
        
    def salir(self,empleado):
        print('Salir')

    def opcion1(self,empleado):
         dni= int(input("Ingrese el DNI: "))
         empleado.aumentar_horas(dni)
         
    def opcion2(self,empleado):
         empleado.mostrar_monto_tarea()
         
    def opcion3(self,empleado):
         empleado.ayuda()
         
    def opcion4(self,empleado):
         empleado.mostrar_sueldos()