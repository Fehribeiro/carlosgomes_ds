print("Bem vindo ao jogo palavra secreta\n")
correta = ["p", "e", "d", "r", "o"]
errada = ["#", "#", "#", "#", "#"]

def jogo():

    for j in range(10):

        letter = input("Digite uma letra:")

        for i in range(len(correta)):
            if letter == correta[i]:
                errada[i] = correta[i]

                print(errada)


    if errada == correta:
        print(correta)                
        print("Parabens você ganhou o jogo")
    
    else:
        print("Você so tinha 10 tentativas tente novamente!!")
        jogo()

jogo()    