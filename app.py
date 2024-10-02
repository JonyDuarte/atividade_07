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

while True:
    try:
        novo_nome = input("Informe um novo nome ou 'Enter' exibir a lista de nomes: ")

        if novo_nome:
            nomes.append(novo_nome)
            print(f"{novo_nome} foi adicionado.")
            continue

        else:
            ...

        for i in range(len(nomes)):
            print(f"Índice {i}: {nomes[i]}")

        indice = int(input("Informe o número do índice do nome que deseja alterar: "))
        confirmacao = input(f"Deseja alterar o nome {nomes[i]}? Se sim digite 'ok': ")

        if confirmacao == "ok":
            novo_nome = input("Informe o novo nome: ")
            nomes[indice] = novo_nome
        else: 
            ...
        indice = int(input("Informe o número do índice do nome que deseja excluir: "))
        confirmacao = input(f"Deseja excluir o nome {nomes[i]}? Se sim digite 'ok': ")

        if confirmacao == "ok":
            del(nomes[indice])
            print("Nome deletado com sucesso.")
        else:
            ...

    except Exception as e:
        print("Não foi possível adicionar um novo nome. {e}.")

    print("Deseja alterar sair do programa? ")
    if "sim":
        break
    else:
        continue



