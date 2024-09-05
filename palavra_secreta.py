print("Bem vindo ao jogo palavra secreta")

import os
palavra_secreta = ''
letra_escrita = ''
letras_certas = ''  
numero_tentativas = 0

while True:
    letra_escrita = input("Digite uma letra")
    if len(letra_escrita)>1:
        print("Digite apenas uma letra")
    continue
 
        