class Veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir_informacoes(self):
        return f"{self.marca} {self.modelo} - Placa: {self.placa}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, tipo="Carro"):
        super().__init__(marca, modelo, placa)
        self.tipo = tipo


class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, tipo="Moto"):
        super().__init__(marca, modelo, placa)
        self.tipo = tipo


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.veiculos = []  

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def remover_veiculo(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                self.veiculos.remove(veiculo)
                return True
        return False

    def exibir_informacoes(self):
        informacoes = f"Cliente: {self.nome}, Telefone: {self.telefone}\nVeículos:\n"
        if self.veiculos:
            for veiculo in self.veiculos:
                informacoes += f"  - {veiculo.exibir_informacoes()}\n"
        else:
            informacoes += "  Nenhum veículo cadastrado.\n"
        return informacoes


clientes = []
veiculos = []


def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone do cliente: ")
    cliente = Cliente(nome, telefone)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso!")


def cadastrar_veiculo():
    tipo = input("Tipo de veículo (Carro/Moto): ").strip().lower()
    marca = input("Marca do veículo: ")
    modelo = input("Modelo do veículo: ")
    placa = input("Placa do veículo: ")

    if tipo == "carro":
        veiculo = Carro(marca, modelo, placa)
    elif tipo == "moto":
        veiculo = Moto(marca, modelo, placa)
    else:
        print("Tipo de veículo inválido!")
        return

    veiculos.append(veiculo)
    print("Veículo cadastrado com sucesso!")

    associar_cliente(veiculo)


def associar_cliente(veiculo):
    print("\nAssociar veículo a um cliente:")
    for i, cliente in enumerate(clientes):
        print(f"{i + 1}. {cliente.nome}")
    
    escolha = int(input("Escolha um cliente pelo número: ")) - 1
    if 0 <= escolha < len(clientes):
        clientes[escolha].adicionar_veiculo(veiculo)
        print(f"Veículo associado ao cliente {clientes[escolha].nome}.")
    else:
        print("Opção inválida!")


def deletar_cliente():
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    nome = input("Nome do cliente que deseja deletar: ").strip().lower()
    cliente_encontrado = None


    for cliente in clientes:
        if cliente.nome.lower() == nome:
            cliente_encontrado = cliente
            break

    if cliente_encontrado:
       
        clientes.remove(cliente_encontrado)
        for veiculo in cliente_encontrado.veiculos:
            veiculos.remove(veiculo)
        print(f"Cliente '{cliente_encontrado.nome}' e seus veículos foram deletados.")
    else:
        print("Cliente não encontrado.")



def deletar_veiculo():
    listar_veiculos()
    if not veiculos:
        return

    placa = input("Placa do veículo que deseja deletar: ")
    veiculo_encontrado = None

    for veiculo in veiculos:
        if veiculo.placa == placa:
            veiculo_encontrado = veiculo
            break

    if veiculo_encontrado:
        veiculos.remove(veiculo_encontrado)
        
        for cliente in clientes:
            cliente.remover_veiculo(placa)

        print(f"Veículo com placa {placa} foi deletado.")
    else:
        print("Veículo não encontrado.")


def listar_clientes():
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(cliente.exibir_informacoes())


def listar_veiculos():
    if not veiculos:
        print("Nenhum veículo cadastrado.")
    else:
        for veiculo in veiculos:
            print(veiculo.exibir_informacoes())


def menu():
    while True:
        print("\n--- Sistema de Controle de Lava Jato ---")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Veículo")
        print("3. Listar Clientes")
        print("4. Listar Veículos")
        print("5. Deletar Cliente")
        print("6. Deletar Veículo")
        print("7. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            cadastrar_cliente()
        elif escolha == "2":
            cadastrar_veiculo()
        elif escolha == "3":
            listar_clientes()
        elif escolha == "4":
            listar_veiculos()
        elif escolha == "5":
            deletar_cliente()
        elif escolha == "6":
            deletar_veiculo()
        elif escolha == "7":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")


menu()
