import random

numerodigitado = int(input("Qual numero deve ser encontrado: "))
numerototal = int(input("Dentre um total de quantos numeros: "))

comeco = int(0)
listadosnaoachados =[]
listadosachados = []
while comeco < numerototal:
    z = random.randint(0,numerototal)
    if numerodigitado != z:
        print(z)
        listadosnaoachados.append(z)
        comeco += 1
    else:
        listadosachados.append(numerodigitado)
        print("achou")
        comeco += 1
print(f"Foi achado um total de {len(listadosachados)} numeros, em um total de {numerototal} tentativas...")