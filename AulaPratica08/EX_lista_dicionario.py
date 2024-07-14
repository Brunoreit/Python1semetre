livros = {}

while True:
    print("\n\tMENU")
    print("1. Cadastrar novo livro")
    print("2. Buscar livro")
    print("3. Mostrar livros acima de R$50")
    print("4. Sair")

    escolha = input("\nEscolha uma opção (1, 2, 3 ou 4): ")

    if escolha == '1':
        print("\n\t>>>CADASTRAR LIVRO<<<")
        cod = int(input("\nDigite o código do livro: "))
        titulo = input("Digite o nome do exemplar: ")
        preco = float(input("Digite o preço do exemplar: "))
        num_autores = int(input("Digite o número de autores: "))

        autores = []
        for i in range(num_autores):
            autor = input(f"Digite o nome do {i+1}° autor: ")
            autores.append(autor)
            
        livros[cod] = {'título': titulo, 'Autores': autores, 'preco': preco}
        print("\nLivro cadastrado com sucesso!!!")

    elif escolha == '2':
        print("\n\t>>>BUSCAR LIVRO<<<")
        buscar_por = input("Deseja buscar por título ou código? (título/código): ")
        if buscar_por == 'título':
            titulo_busca = input("Digite o título do livro que deseja buscar: ")
            for chave, info in livros.items():
                if info['título'] == titulo_busca:
                    print("\nLivro encontrado:")
                    print(f"Código: {chave}")
                    print(f"Título: {info['título']}")
                    print(f"Preço:R${info['preco']}")
                    print("Autores:")
                    for autor in info['Autores']:
                        print("- ", autor)
                    break
                else:
                    print(f"Livro com título {titulo_busca} não encontrado.")

        elif buscar_por == 'código':
            codigo_busca = int(input("Digite o código do livro que deseja buscar: "))
            for chave, info in livros.items():
                if chave == codigo_busca:
                    print("\nLivro encontrado:")
                    print(f"Código: {chave}")
                    print(f"Título: {info['título']}")
                    print(f"Preço: R${info['preco']}")
                    print("Autores:")
                    for autor in info['Autores']:
                        print("- ", autor)

                else:
                    print(f"\nLivro com código {codigo_busca} não foi encontrado.")
            
        else:
            print("Opção inválida!")
        
    elif escolha=='3':
        print("\n\t>>>LIVROS ACIMA DE R$50<<<")
        livros_preco_maior_50 = []
        for chave, info in livros.items():
            if info['preco'] > 50.00:
                livros_preco_maior_50.append([cod, titulo, preco, autores])
                print(f"Código: {chave}")
                print(f"Título: {info['título']}")
                print(f"Preço: R${info['preco']}")  # Formata o preço com duas casas decimais
                print("Autores:")
                for autor in info['Autores']:
                    print("- ", autor)
                    break






    elif escolha == '4':
        print("Saindo do programa...")
        break

    else:
        print(" Por favor, escolha uma opção válida: 1, 2 ou 3.")

