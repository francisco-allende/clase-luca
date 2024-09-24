#from carpeta.nombre_archivo import funciones
from Package_Input.Input import get_float , get_int, get_string

#num = get_int("bnv" ,"error" ,1 , 10, 3)
#print(num)

def pedir_dato():
    msj = input("pone una palabra de 4 letras: ")
    if len(msj) > 4:
        pedir_dato()
    else:
        print("la palabra es corracta!!")

pedir_dato()
