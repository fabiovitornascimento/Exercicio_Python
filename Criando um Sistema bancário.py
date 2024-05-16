menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=>"""

saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3
extrato.append(f"Saldo: R${saldo}")

while True:

    opcao = str(input(menu))

    if opcao == "1":
        print("\n Depósito")
        valor = float(input("Qual valor você deseja depositar hoje? R$"))
        if valor <= 0:
            print("\nValores negativos não são aceito!")
        else:
            saldo += valor
            extrato.append(f"Deposito: R${valor}")
            extrato.append(f"Saldo R${saldo}")
        print(f"\nVocê depositou R${valor}")

    elif opcao == "2":
        print("\n Saque")
        print("Limite de R$500 reais por saque, e só é permitido 3 saques por dia")
        saque = float(input("Qual valor você deseja sacar? R$"))
        if saque <= saldo and saque <= 500:
            if limite_saques != numero_saques:
                numero_saques += 1
                saldo -= saque
                extrato.append(f"Você sacou -R${saque} reais")
                extrato.append(f"Saldo R${saldo}")
                print(f"\nVocê sacou R${saque} reais, e agora seu saldo ficou R${saldo} reais")
            else:
                print("\nNúmero de Saque diario atingido!, volte novamente amanhã")
        elif saque > saldo:
            print(f"\n valor do saque maior que o valor do saldo R${saldo}")
        elif saque > 500:
            print("\n Operação cancelada, saque maior que o valor permitido")

    elif opcao == "3":
        print("\n Extrato")
        for desmontrativo in extrato:
            print(desmontrativo)

    elif opcao == "0":
        print("\n Muito Obrigado por utilizar nossos serviços!")
        break
    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")