class Contato():
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        return '{},{}'.format(self.nome, self.telefone)

    def __str__(self):
        return self.__repr__()

    def salve_se(self, arquivo):
        arquivo.write("{}\n".format(self))

    @staticmethod
    def abra_se(line):
        pedacos = line.split(',')
        contato = Contato(pedacos[0],pedacos[1])
        return contato

class Agenda():
    def __init__(self, arquivoPadrao="agendaoo.txt"):
        self.listaDeContatos = []
        self._arquivoPadrao = ""
        self.arquivoPadrao = arquivoPadrao
        try:
            self.abrir_agenda()
        except Exception:
            pass
    @property
    def arquivoPadrao(self):
        return self._arquivoPadrao

    @arquivoPadrao.setter
    def arquivoPadrao(self, arquivo):
        arq, ext = arquivo.split('.')
        if ext != "xml":
            print("Somente extensões xml são aceitas!")
            return
        self._arquivoPadrao = arquivo

    def salvar_agenda(self):
        arquivo = self.arquivoPadrao
        f = open(arquivo, 'w')
        if f.writable():
            for contato in self.listaDeContatos:
                f.write(contato.__repr__())
            print("Agenda salva com sucesso!")
        f.close()

    def novo_contato(self):
        nome = input("Entre com o nome: ")
        telefone = input("Entre com o telefone: ")
        self.listaDeContatos.append(Contato(nome, telefone))
        print("Contato adicionado com sucesso!")

    def abrir_agenda(self):
        arquivo = self.arquivoPadrao
        print(arquivo)
        try:
            f = open(arquivo, 'r')
            if f.readable():
                nContatos = 0
                for line in f.readlines():
                    self.listaDeContatos.append(Contato.abra_se(line.rstrip('\n')))
                    nContatos += 1
                print ("{} contato(s) aberto(s) do disco.".format(nContatos))
                f.close()
        except FileNotFoundError as e:
            print("O arquivo não foi encontrado. {} realmente existe?".format(arquivo))

    def __repr__(self):
        if len(self.listaDeContatos)==0:
            return("Sem contatos adicionados.")
        str = "Lista de Contatos: "
        str+="\n--------------------------------------"
        for contato in self.listaDeContatos:
            str+='\n'+contato.__str__()
        str+="\n--------------------------------------\n"
        return str

def menu():
    print("1- Adicionar \n2- Mostrar \n3- Salvar \n0 - Sair")
    return int(input("Entre com a opção: "))

if __name__ == '__main__':
    minhaAgenda = Agenda()
    opcao = -10
    while opcao != 0:
        opcao = menu()
        if opcao == 1:
            minhaAgenda.novo_contato()
        elif opcao == 2:
            print(minhaAgenda)
        elif opcao == 3 or opcao == 0:
            minhaAgenda.salvar_agenda()