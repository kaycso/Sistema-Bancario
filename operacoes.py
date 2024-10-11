from datetime import datetime, time, UTC

def acrescentar_extrato(operacao, valor, saldo, extrato, data):
    extrato += f"""
---------------------
{data.strftime('%d/%m/%Y')} {datetime.now().time().strftime('%H:%M:%S')}
{operacao}: R$ {valor}.
saldo: R$ {saldo}"""
    return extrato


def depositar(saldo, numero_transacoes, extrato, data):
    deposito = float(input('Insira o valor que deseja depostiar: '))
    saldo += deposito
    extrato = acrescentar_extrato("Depósito", deposito, saldo, extrato, data)
    numero_transacoes += 1
    return saldo, numero_transacoes, extrato, f"Realizado depósito de R$ {deposito}."

def sacar(saldo, data, extrato, numero_transacoes, numero_saques, limite):
    saque = float(input('Insira o valor que deseja sacar: '))
    if saldo < saque:
        return saldo, extrato, numero_transacoes, numero_saques, "Saldo insuficiente!"
    elif saque > limite:
        return saldo, extrato, numero_transacoes, numero_saques, "Valor maior que limite permitido!"
    
    numero_transacoes += 1
    numero_saques += 1
    saldo -= saque
    extrato = acrescentar_extrato("Saque", saque, saldo, extrato, data)
    return saldo, extrato, numero_transacoes, numero_saques, f"Realizado saque de R$ {saque}."