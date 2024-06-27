from zoo_func import * 


costo_total = 0
Total_entradas = 0

def entradas (tipos_entrada):
    global costo_total
    global Total_entradas

    entrada = " "

    while entrada != "":
    
        entrada = solicita_edad ()


        if entrada == "":
            break
        else:
            valida_edad = valida_entero(entrada)
            if not valida_edad:
                print("Edad errónea, el valor de edad debe ser númerico, verifique")
            else:
                edad = int(entrada)
                if edad  < 0 or edad > 99:
                    print("Edad errónea, la edad debe ser entre 0 y 99 años, vuelva a intentar")
                    continue

                categoria = procesa_edad(edad,tipos_entrada)

                tipos_entrada [categoria]["CONTADOR"] += 1
                costo_total += tipos_entrada[categoria]["PRECIO"]
                Total_entradas += 1


tipos_entrada = tipos_entrada()
costo_total = 0
Total_entradas = 0

entradas(tipos_entrada)


print(f"total Entradas         : {Total_entradas}")
print(f"Costo total            : {costo_total}")
print(f"Total entradas BEBE    : {tipos_entrada['BEBE']['CONTADOR']}")
print(f"Total entradas NIÑO    : {tipos_entrada['NIÑO']['CONTADOR']}") 
print(f"Total entradas ADULTO  : {tipos_entrada['ADULTO']['CONTADOR']}") 
print(f"Total entradas JUBILADO: {tipos_entrada['JUBILADO']['CONTADOR']}")


