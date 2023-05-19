from pick import pick
import os
import time
from termcolor import colored 
from random import randrange

numeros = []


def number(arr,x,y):
    try:
        while x <y:
            x+=1
            arr.append(x)
    except:
        print("algo deu errado")
number(numeros,0,60)
options = [1,2]

nome = input("Digite o seu nome:").capitalize()
if(nome.isalpha() == False):
    print(colored("BURRO","red"))
    exit()
elif(nome.isnumeric() == True):
    print(colored("CPF INCORRETO","red"))
    exit()
cpf = input("cpf (somente 11 digitos):")
if(cpf.isalnum() == False):
    print(colored("CPF INCORRETO","red"))
    exit()
elif(len(cpf) != 11):
    print(colored("CPF INCORRETO","red"))
    cpf = input("mude o cpf exemplo(85343622038): ")
    if(len(cpf)!= 11):
        print("BURRO")
        exit()

escolhidos = []

deseja = input("deseja escolher os seus numeros?")

if(deseja == "nao" or deseja == "não" or deseja == "n"):
    escolhidos.append(randrange(0,10))


print(escolhidos)
time.sleep(2)

while(len(escolhidos) < 6):
    title = "escolha no minimo 6 numeros e no maximo 15"
    option,index = pick(numeros,title,indicator ="=>")
    if(option in escolhidos):
        print("--------------------")
        print(f" O numero {option} foi removido")
        escolhidos.remove(option)
        print("Esse numero já foi escolhido, esses são os numeros que você já escolheu:")
    else:
        escolhidos.append(option)
        print(len(escolhidos))
numeros.insert(numeros[0] -1,"enviar!")
while(option != "enviar!"):
    title = "------------------ Você já escolheu 6 numeros, já é possivel enviar caso assim deseje ------------------"
    option,index = pick(numeros,title,indicator ="=>")
    if(option in escolhidos):
        print("--------------------")
        print(f" O numero {option} foi removido")
        escolhidos.remove(option)
        print("Esse numero já foi escolhido, esses são os numeros que você já escolheu:")
    else:
        escolhidos.append(option)

escolhidos.remove("enviar!")
numeros.remove("enviar!")
for x in numeros:
    if x in escolhidos:
        numeros[numeros.index(x)] = "XX"


text = colored(f'{nome}-{cpf}', 'red')
print(text)
print(numeros[0:10])
print(numeros[10:20])
print(numeros[20:30])
print(numeros[30:40])
print(numeros[40:50])
print(numeros[50:60])


