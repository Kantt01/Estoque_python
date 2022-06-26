from time import sleep

def menu():
    voltaraomenu = 's'
    while voltaraomenu == 's':


        opcao = input('''
    |==========================================================|
                    PROJETO CONTROLE DE ESTOQUE
                            
     MENU:
        
     [1]CADASTRAR ITEM
     [2]LISTAR ITEM
     [3]DELETAR ITEM
     [4]BUSCAR ITEM 
     [5]ATUALIZAR ITEM
     [6]SAIR
        
    |==========================================================|
    ESCOLHA UMA OPÇÃO ACIMA:
    ''')
        if opcao == '1':
            cadastrarItem()
        elif opcao == '2':
            listarItem()
        elif opcao == '3':
            deletarItem()
        elif opcao == '4':
            buscarItem()
        elif opcao =='5':
            atualizaritem()

        else:
            sair()
        voltaraomenu = input('Deseja voltar ao MENU?  (s/n) ').lower()

# CADASTRO DE ITEM
def cadastrarItem():
   id = input('Digite o código do produto: ')
   nome = input('Digite o nome do produto: ')
   quantidade = input('Digite a quantidade do produto: ')
   preco = input('Digite o preço do produto: ')

   try:
      bancodedados = open('Banco de dados.txt','a')
      dados = f'{id} ; {nome} ; {quantidade} ; {preco} \n'
      bancodedados.write(dados)
      bancodedados.close()
      print(f'Produto gravado com SUCESSO!')

   except:
       print ('ERRO na gravação do produto')

# Listar todos produtos cadastrados
def listarItem():
    bancodedados = open('Banco de dados.txt','r')
    for item in bancodedados:
        print(item)
    bancodedados.close()

# DELETAR ITENS
def deletarItem():
    itemdelete = input('Digite o código que será deletado: ')
    bancodedados = open('Banco de dados.txt','r')
    aux = []
    aux2 = []
    for item in bancodedados:
        aux.append(item)
    for item in range(0, len(aux)):
        if itemdelete not in aux[item]:
            aux2.append(aux[item])
    bancodedados = open('Banco de dados.txt','w')
    for item in aux2:
        bancodedados.write(item)
    print(f'Item deletado com sucesso')
    listarItem()



# BUSCAR ITENS
def buscarItem():
    nome = input(f'Digite o código do produto: ')
    bancodedados = open('Banco de dados.txt', 'r')
    for item in bancodedados:
       if nome in item.split(';')[0]:
           print(item)
    else:
        print('Digite apenas números')

    bancodedados.close()

#Atualizar itens
def atualizaritem():
    itemdelete = input('Digite o código que será atualizado: ')
    bancodedados = open('Banco de dados.txt', 'r')
    aux = []
    aux2 = []
    for item in bancodedados:
        aux.append(item)
    for item in range(0, len(aux)):
        if itemdelete not in aux[item]:
            aux2.append(aux[item])
    bancodedados = open('Banco de dados.txt', 'w')
    for item in aux2:
        bancodedados.write(item)
    id = input('Digite o novo código do produto : ')
    nome = input('Digite o novo nome do produto : ')
    quantidade = input('Digite a nova quantidade do produto : ')
    preco = input('Digite o novo preço do produto: ')

    try:
        bancodedados = open('Banco de dados.txt', 'a')
        dados = f'{id} ; {nome} ; {quantidade} ; {preco} \n'
        bancodedados.write(dados)
        bancodedados.close()
        print(f'Produto ATUALIZADO com SUCESSO!')

    except:
        print('ERRO na gravação do produto')




def sair():
    print('Te vejo em breve!')
    sleep(5)
    exit()



def main():
    menu()

main()