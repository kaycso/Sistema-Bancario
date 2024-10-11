from datetime import datetime, date, time, timedelta

transactions = {}
current_date = datetime.now().date()
account_balance = 0

DAILY_TRANSACTION_LIMIT = 10
DAILY_WITHDRAWAL_LIMIT = 3
WITHDRAWAL_VALUE_LIMIT = 500

number_withdrawal = 0
number_transactions = 0

MENU_DISPLAY = """
Menu

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

[data] avançar um dia

=> """

def add_transaction(current_date, transaction, value_transaction, transaction_time, account_balance):
    if current_date not in transactions:
        transactions[current_date] = []

    new_transaction = {
        "transacao": transaction,
        "valor_transacao": value_transaction,
        "horario_transacao": transaction_time,
        "saldo": account_balance
    }

    transactions[current_date].append(new_transaction)

def view_statement():
    statement = ["\n-------------------------"]

    for date_key, transactions_list in transactions.items():
        for transaction in transactions_list:
            transaction_hour = transaction["horario_transacao"].strftime("%H:%M:%S")
            transaction_type = transaction["transacao"]
            transaction_value = transaction["valor_transacao"]
            ballance = transaction["saldo"]
            
            # Formatar a data e hora como 'dd/mm/yyyy hh:mm:ss'
            data_hora_transacao = f"{date_key.strftime("%d/%m/%Y")} {transaction_hour}"
            
            # Criar a mensagem para a transação no formato desejado
            statement.append(f"{data_hora_transacao}")
            statement.append(f"\nTransação: {transaction_type}")
            statement.append(f"Valor: R$ {transaction_value:.2f}\n")
            statement.append(f"Saldo: R$ {ballance:.2f}")
            statement.append("-------------------------")
    
    print("\n".join(statement))

def deposit():
    global current_date, account_balance, number_transactions

    if number_transactions == DAILY_TRANSACTION_LIMIT:
        return print('\nLimite de transações diárias excedido!\nPor favor, retorne amanhã.')

    deposit_value = float(input('\nInsira o valor que deseja depostiar: '))

    account_balance += deposit_value
    number_transactions += 1
    transaction_time = datetime.now().time()

    add_transaction(current_date=current_date, transaction="Depósito", value_transaction=deposit_value, transaction_time=transaction_time, account_balance=account_balance)

def withdrawal():
    global current_date, account_balance, number_withdrawal, number_transactions

    if number_transactions == DAILY_TRANSACTION_LIMIT:
        return print('\nLimite de transações diárias excedido!\nPor favor, retorne amanhã.')
    elif number_withdrawal == DAILY_WITHDRAWAL_LIMIT:
        return print('\nLimite de saques diário excedido!')

    withdrawal_value = float(input('\nInsira o valor que deseja sacar: '))

    if withdrawal_value > WITHDRAWAL_VALUE_LIMIT:
        return print('\nValor excede limite estabelecido!')
    elif withdrawal_value > account_balance:
        return print('\nSaldo Insuficiente!')

    account_balance -= withdrawal_value
    number_withdrawal += 1
    number_transactions += 1
    transaction_time = datetime.now().time()

    add_transaction(current_date=current_date, transaction="Saque", value_transaction=withdrawal_value, transaction_time=transaction_time, account_balance=account_balance)


options = {
    "s": withdrawal,
    "d": deposit,
    "e": view_statement
}

def main():
    global number_withdrawal, number_transactions, current_date

    while True:
        option = input(MENU_DISPLAY)

        if option == 'q':
            print("Saindo...")
            break
        elif option == 'data':
            current_date = current_date + timedelta(days=1)
            number_withdrawal = 0
            number_transactions = 0
            continue
        elif option not in options:
            print("Opção inválida! Por favor, selecione novamente a operação desejada.")
            continue

        options[option]()


main()