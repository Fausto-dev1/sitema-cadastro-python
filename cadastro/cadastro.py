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
                linhas = arquivo.readlines()
                if not linhas:
                    print("Nenhum usuário foi cadastrado!")
                else:
                    for pessoa in linhas:
                        print(pessoa.strip())
        elif numero == 2:
            while True:       #fazer cadastro de pessoa
                cadastrar_p = (input("Informe nome para cadastro: "))
                if cadastrar_p == "":
                    print("\033[31mINSIRA UM NOME PARA CADASTRO\033[0m")
                    continue
                else:
                    print("O nome foi inserido corretamente! ")
                    break
            while True:
                    try:
                        cadastro_id = int(input("Informe a idade: "))
                        if cadastro_id > 0 and cadastro_id <= 120:
                            print("Idade inserida corretamente! ")
                            break
                        else:
                            print("\033[31mINSIRA UMA IDADE VÁLIDA\033[0m")
                    except:
                        print("\033[31mVOCE NÃO INSERIU UM NÚMERO\033[0m")
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