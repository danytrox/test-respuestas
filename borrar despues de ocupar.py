respuestas =[]

for x in range (1,11):
    
    print("seleccione resp de la pregunta ",x)
    resp = input()
    print(x,". ",resp)
    agrega = str(x) + ". "+ resp.upper()
    respuestas.append(agrega)

print(respuestas)