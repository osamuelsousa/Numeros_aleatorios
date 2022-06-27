#OBS: Precisa ser feito o programa da função (inteervalo de nuemros)
#O que fazer? Maquina onde vi encontrar um numero no meio de um monte de numermo para saber qual a ahcence disso acontecer

import random

def formatacao_de_titulos(a):
    print("-"*60)
    print(f'{a:^60}'.upper())
    print("-"*60)

def intervalo_de_numeros():
    print("\n")
    lista_de_numeros = []
    minimo = int(input("Qual numero iniciar? "))
    maximo = int(input("Qual numero terminar? "))
    intervalo = int(input("Em um intervalo de quantos numeros? "))
    for teste in range(1,intervalo + 1):
        lista_de_numeros.append(random.randint(minimo,maximo))
    somadosnumeros1 = []
    somadosnumeros2 = []
    for x in lista_de_numeros:
        if x == 1 or x == 3 or x == 4:
            somadosnumeros1.append(x)
        elif x == 2:
            somadosnumeros2.append(x)
        else:
            ("Erro desconhecido...")
    print(f"\n\nO total de numero igual a 1 foi {len(somadosnumeros1)} e o total de numeros iguais a 2 foi de {len(somadosnumeros2)}")

def maquina_da_impossibilidade():
    print("\n\n")
    numerodigitado = int(input("Qual numero deve ser encontrado: "))
    numerototal = int(input("Dentre um total de quantos numeros: "))

    comeco = int(0)
    listadosnaoachados =[]
    listadosachados = []
    while comeco < numerototal:
        z = random.randint(0,numerototal)
        if numerodigitado != z:
            listadosnaoachados.append(z)
            comeco += 1
        else:
            listadosachados.append(numerodigitado)
            comeco += 1
    print(f"\nFoi achado um total de {len(listadosachados)} numeros, em um total de {numerototal} tentativas...\n")


i = 0
while i == 0:
    formatacao_de_titulos("SASORO")
    aa = "Esta maquina ira gerar números aleatórios"
    bb = "de acordo com o que o usuário digitar,"
    cc = "e em seguida apresentar alguns dados de probabilidade."
    print(f"{aa:^60}\n{bb:^60}\n{cc:^60}\n\n")
    x = str(input("Digite:\n1 - Intervalo de números.\n2 - Encerrar o programa.\n3 - Maquina da impossibilidade...\nDigite: "))


    if x == str(1):
        t = 0
        while t == 0:
            intervalo_de_numeros()
            sim = str(input("1 - Fazer novamente!\n2 - Sair do programa.\nDigite: "))
            if sim == str(1):
                print("tentarndo novamente")
                continue
            elif sim == str(2):
                print("Saindo do programa...")
                break
            else:
                print("Erro não definidio...")
                break
    elif x == str(2):
        print("\n\nEncerrando...")
        i = 1
        break
    elif x == str(3):
        t = 0
        while t == 0:
            maquina_da_impossibilidade()
            sim = str(input("1 - Fazer novamente!\n2 - Sair do programa.\nDigite: "))
            if sim == str(1):
                print("\nTentarndo novamente...")
                continue
            elif sim == str(2):
                print("Saindo do programa...")
                break
            else:
                print("Erro não definidio...")
                break
    else:
        print("Comando invalido, por favor tente novamente")
        break
print("Programa finalizado")
