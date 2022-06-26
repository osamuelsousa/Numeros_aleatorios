#OBS: Precisa ser feito o programa da função (inteervalo de nuemros)
#O que fazer? Parei na def intervalo de numeros que ainda está em construção...

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
    for teste in range(1,intervalo):
        lista_de_numeros.append(random.randint(minimo,maximo))
    print (teste)
    print(lista_de_numeros)
    print("\n\n")

i = 0
while i == 0:
    formatacao_de_titulos("SASORO")
    aa = "Esta maquina ira gerar números aleatórios"
    bb = "de acordo com o que o usuário digitar,"
    cc = "e em seguida apresentar alguns dados de probabilidade."
    print(f"{aa:^60}\n{bb:^60}\n{cc:^60}\n\n")
    x = str(input("Digite:\n1 - Intervalo de números.\n2 - Encerrar o programa.\nDigite: "))


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
    else:
        print("Comando invalido, por favor tente novamente")
        break
print("Programa finalizado")
