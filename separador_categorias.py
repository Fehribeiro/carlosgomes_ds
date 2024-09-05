print("Bem vindo jogador!")
print("Para se cadastrar na peneira precisamos saber apenas seu nome e idade.")
print("De acordo com sua idade, você será encaminhado para diferentes categorias.")

nome = input("Insira seu nome por gentileza:\n")
idade = int(input("Agora insira sua idade:\n"))  

if idade >= 20:
    print(f"{nome}, você irá participar da peneira da base sub-21.")
elif idade >= 18:
    print(f"{nome}, você irá participar da peneira da base sub-19.")
elif idade >= 17:
    print(f"{nome}, você irá participar da peneira da base sub-17.")
else:
    print(f"{nome}, sua idade não permite que você participe de nenhuma peneira.")