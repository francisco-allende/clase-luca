from Package_Input.Validate import *

def get_int(mensaje:str, mensaje_error:str, minimo: int, maximo: int, reintentos:int) -> int | None:
    print(mensaje)   

    for i in range(0, reintentos):
        numero = input("Ingrese un número: ")
        if validate_number(numero, mensaje_error, minimo, maximo):
            return numero
       
    return None

def get_float(mensaje:str, mensaje_error:str, minimo: int, maximo: int, reintentos:int) -> float | None:
    print(mensaje) 

    for i in range(0, reintentos):
        try:
            numero = float(input("Ingrese un número: "))
            
            if numero < minimo or numero > maximo:
                print(mensaje_error)
                    
            else:
                return numero
            
        except ValueError:
            print(mensaje_error)
    
    ## fin del for, no hay mas reintentos ##    
    return None


def get_string(longitud: int) -> str | None:
    mensaje = input("Ingresa mensaje: ")
    
    if len(mensaje) <= longitud:
        return mensaje
    else:
        return None
    
