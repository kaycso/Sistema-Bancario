from datetime import datetime, date, time, timedelta

users = []
accounts = []

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
[nu] Criar novo usuário
[nc] Criar nova conta
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

def user_exists(user_cpf, users):
    return any(user["CPF"] == user_cpf for user in users)

def create_user():
    global users

    user_cpf = input("Digite o CPF do usuário apenas com números: ")
    user_name = input("\nDigite o nome completo do usuário: ").title()

    user_born_day = int(input("\nDigite o dia do nascimento do usuário: "))
    user_born_month = int(input("\nDigite o mês do nascimento do usuário (1 a 12): "))
    user_born_year = int(input("\nDigite o ano do nascimento do usuário: "))
    birth_date = date(user_born_year, user_born_month, user_born_day).strftime('%d/%m/%Y')

    print("\nDados para endereço do usuário:")
    user_address_street = input("Digite apenas o logradouro: ").title()
    user_address_number = input("Digite o número: ")
    user_address_neighborhood = input("Digite o bairro: ")
    user_address_city = input("Digite a cidade: ")
    user_address_state = input("Digite o estado (sigla): ").upper()
    user_address = f'{user_address_street}, {user_address_number} - {user_address_neighborhood} - {user_address_city}/{user_address_state}'

    if user_exists(user_cpf, users):
        return print("Usuário já cadastrado!")
    
    new_user = { "nome": user_name, "data_nascimento": birth_date, "CPF": user_cpf, "Endereço":  user_address }

    print("\nRevise os dados do usuário:")
    print(f"Nome: {new_user["nome"]}\nData de Nascimento: {new_user["data_nascimento"]}\nCPF: {new_user['CPF']}\nEndereço: {new_user['Endereço']}")
    confirm_new_user = input("\nOs dados conferem? (S/N)").lower()
    if confirm_new_user != 's':
        print("\nOperação cancelada!")
        return
    
    users.append(new_user)

def find_user_by_cpf(user_cpf, users):
    for user in users:
        if user["CPF"] == user_cpf:
            return user
    return None

def create_account():
    global users, accounts

    user_cpf = input("\nDigite o CPF do usuário para o qual deseja criar uma conta: ")
    if not user_exists(user_cpf, users):
        print("Usuário não cadastrado")
        return

    if not accounts:
        account_number = 1
    else:
        account_number = accounts[-1]["numero_da_conta"] + 1

    account_agency = "0001"

    new_account = { "numero_da_conta": account_number, "agencia": account_agency, "cpf_usuario": user_cpf }

    user = find_user_by_cpf(user_cpf, users)
    print(f"\nEstá sendo criado uma conta para o usuário {user["nome"]}, CPF {user["CPF"]}")
    print(f"\nRevise os dados:\nNúmero da Conta: {account_number}\nAgência: {account_agency}")

    confirm_new_account = input("\nConfirmar criação de conta? (S/N)").lower()
    if confirm_new_account != 's':
        print("Operação Cancelada")
        return 
    
    accounts.append(new_account)

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

options = {
    "s": withdrawal,
    "d": deposit,
    "e": view_statement,
    "nu": create_user,
    "nc": create_account
}

main()