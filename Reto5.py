def tipodefigurita(figuritas):
    #resultado = []
    #resultado.append(str(figuritas[0]))
    for i in figuritas:
        if str(i) in resultado:
            pass
        else:
            resultado.append(str(i))
    return resultado

def mefaltandeltipodefigurita(indices, figuritas, figurita_a_verificar):
    resultado = []
    for i in indices:
        if figuritas[int(i)] == figurita_a_verificar:
            resultado.append(int(i))
    return resultado

def notengo(figuritas_1, figuritas_2):
    resultado = []
    for i in figuritas_1:
        if i in figuritas_2:
            pass
        else:
            resultado.append(int(i))
    return resultado
    
def puedocambiar(figuritas_1, figuritas_2):
    resultado = 0
    resultado_2 = 0
    for i in figuritas_1:
        if i in figuritas_2:
            pass
        else:
            resultado +=1
    for i in figuritas_2:
        if i in figuritas_1:
            pass
        else:
            resultado_2 +=1
    if resultado > resultado_2:
        resultado = resultado_2
    return resultado

#Resultado función tipodefigurita 
"listado_clases = input(" ")"
"listado_clases = listado_clases.split(",")"
"clases = tipodefigurita(listado_clases)"
"print(" ")"
"print(clases)"

#Resultado función mefaltandeltipodefigurita 
"indices_jugador1 = input(" ")"
"indices_jugador1 = indices_jugador1.split(",")"

"listado_clases_amigo = input(" ")"
"listado_clases_amigo = listado_clases_amigo.split(",")"
"clase_de_figurita = input(" ")"
"notengo = mefaltandeltipodefigurita(indices_jugador1,listado_clases_amigo,clase_de_figurita)"
"print(" ")"
"print(notengo)"

#Resultado función puedocambiar
figuritas_amigo = input(" ")
figuritas_amigo = figuritas_amigo.split(",")

figuritas_jugador = input(" ")
figuritas_jugador = figuritas_jugador.split(",")
figuritas_cambiar = puedocambiar(figuritas_amigo,figuritas_jugador)
print(" ")
print(figuritas_cambiar)

