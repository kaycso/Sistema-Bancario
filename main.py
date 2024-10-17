import textwrap
from abc import ABC, abstractmethod


class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor


class Historico:
    def adicionar_transacao(self, transacao):
        pass


class Conta(ABC):
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(cliente, numero)

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

class Cliente(ABC):
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    @property
    def contas(self):
        return self._contas

    @property
    def endereco(self):
        return self._endereco

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    def __str__(self):
        mensagem = f"\nCliente:\t\t{self.nome}\nCPF:\t\t\t{self.cpf}\nData de Nascimento:\t{self.data_nascimento}\nEndereço:\t\t{self.endereco}\nContas:\t\t\t{len(self.contas)}\n"
        return mensagem

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento


def menu():
    menu = """
    ================= MENU =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [lu]\tListar Usuários
    [q]\tSair

    =>"""
    return input(textwrap.dedent(menu))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = PessoaFisica(cpf, nome, data_nascimento, endereco)

    usuarios.append(usuario)
    
    print("=== Usuário criado com sucesso! ===")
    

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_usuarios(usuarios):
    print("========== Usuários Cadastrados ==========")
    for usuario in usuarios:
        print(usuario)
    print("==========================================")


def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    numero = len(contas) + 1

    if usuario:
        nova_conta = ContaCorrente(numero, usuario)
        contas.append(nova_conta)

        usuario.adicionar_conta(nova_conta)

        print("\n=== Conta criada com sucesso! ===")
        return

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def mostrar_conta(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def listar_contas(contas, usuarios):
    opcao = input("\nDeseja filtrar por Cliente? (S/N)\n").lower()

    if opcao == "s":
        cpf = input("\nInsira o CPF do usuário: ")
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            mostrar_conta(usuario.contas)
        else:
            print("@@@ Usuário não Encontrado! @@@")
    else:
        mostrar_conta(contas)


def main():
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        if opcao == "nc":
            criar_conta(contas, usuarios)

        elif opcao == "lc":
            listar_contas(contas, usuarios)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "lu":
            listar_usuarios(usuarios)
            
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada!")


main()