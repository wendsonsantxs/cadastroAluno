from endereco import *
class Aluno(Endereco):

    def __init__(self, cpf, matricula, nome, idade, rua, numero, bairro, cep):
       self.__cpf= cpf
       self.matricula= matricula
       self.nome=nome
       self.idade= idade
       super().__init__(rua, numero, bairro, cep)
       self.alunos=[]



    def adicionarAluno(self):
        cpf=input('Cpf:')
        matricula= int(input('Matricula:'))
        nome= input('Nome:')
        idade= int(input('Idade:'))
        self.setCpf(cpf)
        self.setMatricula(matricula)
        self.setNome(nome)
        self.setIdade(idade)
        self.alunos.append([cpf, matricula, nome, idade])



    def getCpf(self):
        return self.__cpf
    
    def setCpf(self, cpf):
        self.__cpf= cpf

    def getMatricula(self):
        return self.matricula
    
    def setMatricula(self, matricula):
        self.matricula= matricula
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome= nome
    
    def getIdade(self):
        return self.idade
    
    def setIdade(self, idade):
        self.idade= idade

    def __str__(self):
        return f'CPF: {self.getCpf()} \nMatricula: {self.getMatricula()} \nNome: {self.getNome()} \nIdade: {self.getIdade()}'
    

aluno= Aluno('111.111.111-11', '1234567', 'Marcos Antonio', '24', 'Luiz Augusto', '25', 'Cagep', '54600000')
print(aluno)
    







        

    