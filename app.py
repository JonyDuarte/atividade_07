'''Crie um programa que possa:
- Inserir o nome do usuário em uma lista
- exibir a lista de nomes
- Ordenar nomes
- Alterar um nome da lista
- Excluir um nome da lista
- Sair do programa
O programa deverá exibir um menu, e o usuário iré escolher a opção desejada do menu.'''

# lista
nomes = []
import time

while True:
    try:
        print('''
        [1] Inserir o nome do usuário em uma lista
        [2] Exibir a lista de nomes 
        [3] Alterar um nome da lista
        [4] Excluir um nome da lista
        [5] Sair do programa \n''')

        opcao = int(input("Digite sua opção: "))
                
        if opcao == 1:
            novo_nome = input("Informe um novo nome para lista: ")
            nomes.append(novo_nome)
            time.sleep(0.3)
            print(f"{novo_nome} foi adicionado.")
            continue

        elif opcao == 2:
             for i in range(len(nomes)):
                print(f"{i}: {nomes[i]}")
                continue
        
        elif opcao == 3:
            indice = int(input("Informe o número  nome que deseja alterar: "))
            confirmacao = input(f"Deseja alterar o nome {nomes[i]}? Se sim digite 'ok': ")
            if confirmacao == "ok":
                novo_nome = input("Informe o novo nome: ")
                nomes[indice] = novo_nome
                time.sleep(0.3)
                print(f"{novo_nome} foi adicionado com sucesso.")
                continue
        
        elif opcao == 4:
            indice = int(input("Informe o número do nome que deseja excluir: "))
            confirmacao = input(f"Deseja excluir o nome {nomes[i]}? Se sim digite 'ok': ")
            if confirmacao == "ok":
                del(nomes[indice])
                time.sleep(0.3)
                print("Nome deletado com sucesso.")
                continue
        
        elif opcao == 5:
            print("Saindo do programa....")
            time.sleep(0.5)
            break

        else:
            ...        

    except Exception as e:
        print("Não foi possível adicionar um novo nome. Tente novamente. {e}.")

print("Fim do programa!")



