def cadastro_usuario(lista_usuario):
    nome = input("Digite seu nome: ")
    while True:
        nascimento = input("Digite sua data de nascimento, somente números:")
        if len(nascimento) == 8 and nascimento.isnumeric():
            break
        else:
            print("Data de nascimento incorreta!")
    print("Digite seu endereço: ex: Logradouro, Número, Bairro, cidade/sigla estado")
    logradouro = input("Lougradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    sigla = input("sigla do estado: ")
    estado = input("Estado : ")
    endereco = {"Lograduro:": logradouro, "Número:": numero, "Bairro:": bairro, "Cidade:": cidade, "UF:": sigla, "Estado:": estado}
    while True:
        usuario = input("Digite seu nome de usuário: ")
        conferir_user = False
        conferir_user = conferir_usuario(usuario, lista_usuario, conferir_user)
        if conferir_user == False:
            print(" Nome de usuário já existente!")
        else:
            break
    while True:
        cpf = input("Digite seu CPF: somente números!\n")
        if len(cpf) == 11 and cpf.isnumeric():
            cpf_conferido = False
            cpf_conferido = conferir_cpf(cpf, lista_usuario, cpf_conferido)
            if cpf_conferido == True:
                usuario_novo = {"Nome:": nome,  "Data de Nascimento": nascimento, "Endereço:": endereco, "Usuário:": usuario, "CPF:": cpf}
                lista_usuario.append(usuario_novo)
                print("\n Cadastro de novo usuário realizado com sucesso!\n")
                break
            else:
                print("Usuário com esse CPF já existe, Digite outro CPF")
        else:
            print("CPF inválido")


def conferir_cpf(cpf, lista_usuario, validacao):
    validacao = True
    for dado in lista_usuario:
        C = dado["CPF:"]
        if cpf == C:
            validacao = False
            return validacao
    validacao = True
    return validacao


def conferir_usuario(usuario, lista_usuario, validacao):
    validacao = True
    for dado in lista_usuario:
        C = dado["Usuário:"]
        if usuario == C:
            validacao = False
            return validacao
    return validacao

def filtro_usuario(usuario, cpf, lista_usuario, validacao):
    validacao = False
    for dado in lista_usuario:
        Cliente = dado["Usuário:"]
        cpf2 = dado["CPF:"]
        if usuario == Cliente and cpf == cpf2:
            validacao = True
            return validacao
    return validacao


def cadastro_conta(usuario, conta):
    while True:
        print("\nPara criar uma nova conta insira o Usuário e CPF:")
        while True:
            conferido = True
            user = input("Usuário: ")
            while True:
                cpf = input("CPF: ")
                if len(cpf) == 11 and cpf.isnumeric():
                    break
                else:
                    print("CPF inválido! Digite novamente o CPF, Somente Números!")
            conferido = filtro_usuario(user, cpf, usuario, conferido)
            if conferido == True:
                break
            else:
                print("Usuário ou CPF não encontrado! Programa encerrado!")
                break
        if conferido == False:
            break
        opc = input("""Escolha o tipo de conta: \n[1] Poupança \n[2] Corrente\nopção desejada:""")
        if opc == "1":
            opc = "Conta-Poupança"
            break
        elif opc == "2":
            opc = "Conta-Corrente"
            break
        else:
            print("Opção inválida! digite uma opção válida!")
    while True:
        if conferido == False:
            break
        senha = input("Digite a sua senha númerica de 4 dígitos: ")
        if senha.isdigit() and len(senha) == 4:
            print("\n Conta Criada com Sucesso!")
            registro = {"Usuário": user, "CPF": cpf, "Agência": "0001", "Conta": str(len(conta)+1), "tipo de conta": opc, "Senha": senha, "Financeiro": {"Saldo": 0, "numero_saques": 0, "Extrato": ["\033[32mSaldo: \t\t R$0.00\033[m"]}}
            conta.append(registro)
            print(f" Agência: 0001\n Conta: {len(conta)}\n Tipo de Conta: {opc}")
            break
        else:
            print("Senha inválida! digite outra senha!")


def login(dados, limite, limite_saques):
    print("\n=== Acesso a conta Bancária ===")
    agencia = input("Agencia: ")
    conta = input("Conta: ")
    senha = input("Senha:")
    for dado in dados:
        if agencia == dado["Agência"] and conta == dado["Conta"] and senha == dado["Senha"]:
            tipo_de_conta = dado["tipo de conta"]
            dinheiro = dado["Financeiro"]["Saldo"]
            print(f"\n Acesso realizado com sucesso na sua conta {tipo_de_conta} ")
            print(f" Seu saldo é de: R${dinheiro}\n")
            while True:
                opc = input(" Escolha a operação que deseja realizar:\n [1] - Sacar\n [2] - Depositar\n [3] - Extrato\n [0] - Sair\n Digite uma opção:")
                if opc == "1":
                    saldo = dado["Financeiro"]["Saldo"]
                    numero_saques = dado["Financeiro"]["numero_saques"]
                    retorno = []
                    valor = float(input("\n Digite o valor que deseja resgatar: "))
                    retorno = saque(valor=valor, limite=limite, limite_saques=limite_saques, numero_saques=numero_saques, saldo=saldo, retorno=retorno)
                    dado["Financeiro"]["Saldo"] = retorno[0]
                    dado["Financeiro"]["numero_saques"] = retorno[2]
                    if retorno[1] != "":
                        dado["Financeiro"]["Extrato"].append(retorno[1])
                        dado["Financeiro"]["Extrato"].append(f"\033[32mSaldo: \t\t R${retorno[0]}\033[m")
                elif opc == "2":
                    saldo = dado["Financeiro"]["Saldo"]
                    retorno = []
                    valor = float(input("\n Digite o valor que deseja depositar: "))
                    retorno = deposito(saldo, valor, retorno)
                    if valor > 0:
                        dado["Financeiro"]["Saldo"] = retorno[0]
                        dado["Financeiro"]["Extrato"].append(retorno[1])
                        dado["Financeiro"]["Extrato"].append(f"\033[32mSaldo: \t\t R${retorno[0]}\033[m")
                elif opc == "3":
                    extrato(dado)
                elif opc == "0":
                    print(" Saindo da Conta...")
                    break
    else:
        print("Conta não encontrada, operação encerrada!")


def saque(*, valor,  limite, limite_saques, numero_saques, saldo, retorno):
    extrato = ""
    if valor > saldo:
        print(" Valor de saque maior que o saldo disponível!")
        print(" Operação de saque cancelada! Voltando ao menu anterior!\n")
    elif valor > limite:
        print(" O valor que deseja sacar é maior que o valor permitido! R$500,00")
        print(" Operação de saque cancelada! Voltando ao menu anterior!\n")
    elif numero_saques >= limite_saques:
        print(" Número máximo de saque diário atingido por hoje!")
        print(" Operação de saque cancelada! Voltando ao menu anterior!\n")
    else:
        print(f" Você retirou R${valor}\n")
        saldo -= valor
        extrato = f"\033[31mSaque de\tR${valor}\033[m"
        numero_saques += 1
    return saldo, extrato, numero_saques


def deposito(saldo, valor, retorno, /):
    saldo += valor
    extrato = f"\033[34mDepósito de\t R${valor}\033[m"
    print(" Depósito realizado com sucesso!\n")
    return saldo, extrato



def extrato(dados):
    extrato = dados["Financeiro"]["Extrato"]
    for demonstrativo in extrato:
        print(demonstrativo)
    print("\n")



limite = 500
limite_saques = 3

usuario = []
conta = []
opcao1 = """
 Escolha uma opção: 
 [1] Criar novo Usuário
 [2] Criar nova conta bancária
 [3] Acessa sua conta bancária
 [0] Sair
 digite uma opção: """
print(" Bem vindo ao Banco Dio")

while True:

    opcao = input(str(opcao1))
    if opcao == "1":
        print("\nTela de Cadastro de Usuário")
        cadastro_usuario(usuario)
    elif opcao == "2":
        cadastro_conta(usuario, conta)
    elif opcao == "3":
        login(conta, limite, limite_saques)
    elif opcao == "0":
        print(" Muito obrigado pela preferencia! Volte Sempre!")
        break
    else:
        print(" Opção Inválida!, Escolha outra opção no menu!")

