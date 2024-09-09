from operacoes import depositar, sacar, acrescentar_extrato

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = f"saldo inicial: {saldo}"
numero_saques = 0
LIMITES_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato, mensagem = depositar(saldo, extrato)
        print(mensagem)

    elif opcao == "s":
        if numero_saques == 3:
            print("Limite diário excedido")
            continue
        saldo, extrato, numero_saques, mensagem = sacar(saldo, extrato, numero_saques, limite=500)
        print(mensagem)

    elif opcao == "e":
        print("============EXTRATO============")
        print(extrato)
        print("===============================")



    elif opcao == "q":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida! Por favor, selecione novamente a operação desejada.")
