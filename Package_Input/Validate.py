def validate_number(numero: int, mensaje_error:str, minimo: int, maximo: int):
    if numero.isdigit():
        
        if int(numero) < minimo or int(numero) > maximo:
            print(mensaje_error)
            
        else:
            return True
            
    else:
        print(mensaje_error)
