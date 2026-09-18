def linha():
    print("-" * 30)
    print("MENU PRINCIPAL".center(30))
    print("-" * 30)
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar pessoa")
    print("3 - Sair do sistema")
    print("-" * 30)

def cadastrar():
    while True:
        linha()
        try:
            numero = int(input("Informe sua opção: "))
        except:
            print("Voce digitou um numero invaálido")
            continue    
        if numero == 1:         #mostrar lista de cadastrados
            print("-" * 30)
            print("NOMES CADASTRADOS".center(30))
            print("-" * 30)
            with open("arquivo/pessoas.txt", "r") as arquivo:
                for linhas in arquivo:
                    print(linhas.strip())
        elif numero == 2:       #fazer cadastro de pessoa
            cadastrar_p = str(input("Informe nome para cadastro: "))
            cadastro_id = int(input("Informe a idade: "))
            with open("arquivo/pessoas.txt", "a") as arquivo:
                arquivo.write(f"{cadastrar_p} - {cadastro_id} anos\n") 
                print(f"O Usuario {cadastrar_p} foi cadastrado!")
        elif numero == 3:       #sair do sistema
            print("-" * 30)
            print("Saindo do sistema!")
            print("-" * 30)
            break
        else:
            print("Voce digitou uma opção errada") 