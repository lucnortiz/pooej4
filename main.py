from modulo_maneja_empleado import ManejaEmpleado
from menu import Menu

if __name__=='__main__':
    
    empleado= ManejaEmpleado()
    
    empleado.carga_empleados_planta()
    empleado.carga_empleados_contratados()
    empleado.carga_empleados_externos()
    
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Incrementar horas trabajadas de un empleado")
        print("2. Mostrar el monto a pagar de un  obra\n3. Listar empleados que necesitan ayuda economica")
        print("4. Mostrar sueldos de todos los empleados\n0. Salir")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, empleado)
        salir = op == 0
    print(salir)