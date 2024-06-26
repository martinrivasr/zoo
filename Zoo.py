'''
este rpograma
'''
costo_total = 0
Total_entradas = 0
entrada = " "
while entrada != "":
    entrada = input('Digite la Edad de la persona ,  ["" Para salir]')
    if entrada == "":
        break
    
    try:
        edad = int(entrada)

        if edad  < 0 or edad > 99:
            print("Edad errónea, la edad debe ser entre 0 y 99 años, vuelva a intentar")
            
            continue

        if  edad  < tipos_entrada ["BEBE"]["EDAD"]:
            tipos_entrada["BEBE"]["CONTADOR"] += 1
        
        elif edad  < tipos_entrada ["NIÑO"]["EDAD"]:
            tipos_entrada ["NIÑO"]["CONTADOR"] += 1
            costo_total += tipos_entrada["NIÑO"]["PRECIO"]
    
        elif edad < tipos_entrada ["ADULTO"]["EDAD"]:
            tipos_entrada ["ADULTO"]["CONTADOR"] += 1
            costo_total += tipos_entrada["ADULTO"]["PRECIO"]
        
        else:
            tipos_entrada ["JUBILADO"]["CONTADOR"] += 1
            costo_total += tipos_entrada["JUBILADO"]["PRECIO"]
        
    
        Total_entradas += 1

    except ValueError:
        print("Edad Errónea, la edad debe ser entre 0 y 99 años, vuelva a intentar")
    
print(f"total Entradas         : {Total_entradas}")
print(f"Costo total            : {costo_total}")
print(f"Total entradas BEBE    : {tipos_entrada['BEBE']['CONTADOR']}")
print(f"Total entradas NIÑO    : {tipos_entrada['NIÑO']['CONTADOR']}") 
print(f"Total entradas ADULTO  : {tipos_entrada['ADULTO']['CONTADOR']}") 
print(f"Total entradas JUBILADO: {tipos_entrada['JUBILADO']['CONTADOR']}")