from tkinter import messagebox, simpledialog

# Inicializando a lista de pedidos
pedidos = [None] * 10

#função incluir pedidos
def incluir_pedido():
    global pedidos
    for i in range(len(pedidos)):
        if pedidos[i] is None:
            pedido = simpledialog.askstring("Incluir Pedido", "Digite o número do pedido:")
            if pedido:
                pedidos[i] = pedido
                messagebox.showinfo("Sucesso", f"Pedido {pedido} incluído na posição {i+1}")
                break
    else:
        messagebox.showwarning("Fila Cheia", "Não é possível incluir mais pedidos. A fila está cheia.")

#função atender pedidos
def atender_pedido():
    global pedidos
    if not any(pedido for pedido in pedidos if pedido is not None):
        messagebox.showwarning("Lista Vazia", "Não existem pedidos para serem atendidos.")
    
    atendido = False
    pedido_atendido = simpledialog.askstring("Atender Pedido", "Digite o número do pedido a ser atendido:")
    for i in range(len(pedidos)):
        if pedidos[i] == pedido_atendido:
            pedidos[i] = None
            messagebox.showinfo("Pedido Atendido", f"Pedido {pedido_atendido} foi atendido.")
            atendido = True
            break
        
    if not atendido:
        print(f"Pedido {pedido_atendido} não encontrado na lista.")

#função listar pedido
def listar_pedidos():
    global pedidos
    if any(pedidos):
        pedidos_text = "\n".join(filter(None, pedidos))
        messagebox.showinfo("Lista de Pedidos", f"Pedidos:\n{pedidos_text}")
    else:
        messagebox.showwarning("Lista Vazia", "Não existem pedidos registrados.")

#função pesquisar pedidos
def pesquisar_pedido():
    global pedidos
    pedido_pesquisado = simpledialog.askstring("Pesquisar Pedido", "Digite o número do pedido:")
    if pedido_pesquisado in pedidos:
        messagebox.showinfo("Pedido Encontrado", f"Pedido {pedido_pesquisado} está na lista.")
    else:
        messagebox.showinfo("Pedido Não Encontrado", f"Pedido {pedido_pesquisado} não está na lista.")

#função encerrar pedidos
def encerrar():
    global pedidos
    if any(pedidos):
        messagebox.showwarning("Pedidos Pendentes", "Atenção, ainda existem pedidos pendentes. \nAtenda todos os pedidos antes de encerrar.")
    else:
        pedidos.destroy()

# Funções do Menu
menu_options = {
    1: incluir_pedido,
    2: atender_pedido,
    3: listar_pedidos,
    4: pesquisar_pedido,
    5: encerrar
}

while True:
    opcao = simpledialog.askinteger("Lanchonete Lanchocat", "Olá, seja bem-vindo(a)!. Escolha uma opção: \n \n1 – INCLUIR PEDIDO \n2 - ATENDER PEDIDO \n3 - LISTAR PEDIDOS \n4 – PESQUISAR PEDIDO \n5 – ENCERRAR \n \nDigite o número da operação desejada:")
    
    if opcao in menu_options:
        menu_options[opcao]()
    else:
        messagebox.showwarning("Opção Inválida", "Você escolheu uma opção inválida. \nPor favor, escolha uma opção válida (1 a 5).")
