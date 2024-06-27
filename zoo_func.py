
def tipos_entrada():
    tipos_entrada_dic = {
        "BEBE": {"EDAD": 3, "PRECIO": 0, "CONTADOR": 0},
        "NIÑO": {"EDAD": 13, "PRECIO": 14, "CONTADOR": 0},
        "ADULTO": {"EDAD": 65, "PRECIO": 23, "CONTADOR": 0},
        "JUBILADO": {"EDAD": float('inf'), "PRECIO": 18, "CONTADOR": 0}
    }
    

    return tipos_entrada_dic 

def solicita_edad():
    entrada = input('Digite la Edad de la persona ,  ["" Para salir]')

    return entrada


def valida_entero(n: str) -> bool:
    try:
        int(n)
        valida_entero = True
    
    except ValueError:
        valida_entero = False

    
    return valida_entero


def procesa_edad(edad, tipos_entrada):
    if edad < 0 or edad > 99:
        procesa_edad = "Edad Erronea"
    
    else:
        for categoria, datos in tipos_entrada.items():
            if edad < datos["EDAD"]:
                return categoria
    
    
    return procesa_edad



        

