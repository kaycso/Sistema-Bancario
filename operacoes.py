
def acrescentar_extrato(operacao, valor, saldo, extrato):
    extrato += f"""
---------------------
{operacao}: R$ {valor}.
saldo: R$ {saldo}"""
    return extrato


def depositar(saldo, extrato):
    deposito = float(input('Insira o valor que deseja depostiar: '))
    saldo += deposito
    extrato = acrescentar_extrato("Depósito", deposito, saldo, extrato)
    return saldo, extrato, f"Realizado depósito de R$ {deposito}."

def sacar(saldo, extrato, numero_saques, limite):
    saque = float(input('Insira o valor que deseja sacar: '))
    if saldo < saque:
        return saldo, extrato, numero_saques, "Saldo insuficiente!"
    elif saque > limite:
        return saldo, extrato, numero_saques, "Valor maior que limite permitido!"
    
    numero_saques += 1
    saldo -= saque
    extrato = acrescentar_extrato("Saque", saque, saldo, extrato)
    return saldo, extrato, numero_saques, f"Realizado saque de R$ {saque}."