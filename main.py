from operacoes import depositar, sacar
from datetime import datetime, timedelta, UTC, date

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

[data] avançar um dia

=> """

data = datetime.now().date()
saldo = 0
limite_saque = 500
extrato = f"saldo inicial: {saldo}"
numero_saques = 0
LIMITE_TRANSACOES_SAQUES = 3
LIMITE_TRANSACOES = 10
numero_transacoes = 0

transacoes = {} # formato: { "data": [{ "tipo_transação": "valor_transacao", "horário_transacao": "valor_horário" }] }

while True:
    opcao = input(menu)

    if opcao == "d":
        if numero_transacoes == LIMITE_TRANSACOES:
            print('Limite de transações diários excedido!')
            continue

        saldo, numero_transacoes, extrato, mensagem = depositar(saldo, numero_transacoes, extrato, data)
        print(mensagem)

    elif opcao == "s":
        if numero_saques == LIMITE_TRANSACOES_SAQUES:
            print("Limite diário excedido")
            continue

        if numero_transacoes == LIMITE_TRANSACOES:
            print('Limite de transações diários excedido!')
            continue

        saldo, extrato, numero_transacoes, numero_saques, mensagem = sacar(saldo, data, extrato, numero_transacoes, numero_saques, limite=limite_saque)
        print(mensagem)

    elif opcao == "e":
        print("============EXTRATO============")
        print(extrato)
        print("===============================")



    elif opcao == "data":
        data = data + timedelta(days=1)
        numero_saques = 0
        numero_transacoes = 0

    elif opcao == "q":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida! Por favor, selecione novamente a operação desejada.")
