# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO ESCOLHER SE QUER CADASTRAR UMA NOVA IDADE
# OU SE QUER SAIR DO PROGRAMA SE ELE QUISER CADASTRAR NOVA IDADE PEÇA PARA ELE DIGITAR A IDADE E GUARDE ELA EM UMA LISTA.
# QUANDO ELE DECIDIR QUE QUER SAIR DO PROGRAMA, PERCORRA A LISTA DAS IDADES CADASTRADAS E:


# INFORME QUAL A IDADE DA PESSOA MAIS VELHA
# INFORME QUAL A IDADE DA PESSOA MAIS NOVA
# INFORME A MÉDIA DAS IDADES.

idades = []

while True:
    print("\n\nMENU")
    print("1 - Cadastrar nova idade")
    print("2 - Vericar idades cadastradas")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        idade = int(input("Digite a idade: "))
        if idade >= 0:
            idades.append(idade)
            print("Idade caastrada com sucesso!")
        else:
            print("Valor inválido")

    elif opcao == "2":

        if idades:
            mais_velho = idades[0]
            mais_novo = idades[0]
            soma_total = 0

            for idade_da_vez in idades:
                soma_total += idade_da_vez

                if idade_da_vez > mais_velho:
                    mais_velho = idade_da_vez
    
                if idade_da_vez < mais_novo:
                    mais_novo = idade_da_vez

            media = soma_total / len(idades)


            print("\n\nResultados:")
            print(f"Idades cadastradas: {idades}")
            print(f"Idade do mais velho é: {mais_velho}")
            print(f"Idade do mais novo é: {mais_novo}")
            print(f"Média das idades é: {media:.2f}")
        else:
            print("Nenhuma idade cadastrada!")
    
    elif opcao == "3":
            print("Encerrar o programa")
            break
    else:
        print("Valor inválido. Por favor escolha uma das opções de 1 a 3")

