Lista = []

def lista_adicionar():
    nome = input('Entre com o nome: ')
    telefone = input('Entre com o telefone: ')
    
    novoMembro = {'nome':nome, 'telefone': telefone}
    Lista.append(novoMembro)
    
def lista_salvar(nomearquivo='agenda.xml'):
    arq = open(nomearquivo, 'a')
    # Testar se o arquivo foi aberto
    for item in Lista:
        arq.write('<contato>\n<nome>{}</nome>\n<telefone>{}</telefone>\n</contato>'.format(item['nome'], item['telefone']))
    arq.close()


def lista_abrir(nomearquivo='agenda.xml'):
    arq = open(nomearquivo)
    # Testar se o arquivo foi aberto
    for line in arq.readlines():
        dados = line.split(',')
        novoMembro = {'nome':dados[0], 'telefone': dados[1].rstrip('\n')}
        Lista.append(novoMembro)

def lista_mostrar():
    print(Lista)

def print_menu():
    print('1 - Adicionar\n 2 - Mostrar \n 3 - Salvar\n 4 - Abrir \n 0 - Sair')
    opcao = int(input('Sua escolha: '))
    
    return opcao
    
    
if __name__ == '__main__':
    while True:
        opcao = print_menu()
        if(opcao == 1):
            lista_adicionar()
        elif(opcao == 2):
            lista_mostrar()
        elif (opcao == 3):
            lista_salvar(input('Entre com o nome do arquivo: '))
        elif (opcao == 4):
            lista_abrir(input('Abrir: Entre com o nome do arquivo: '))
        elif (opcao == 0):
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')