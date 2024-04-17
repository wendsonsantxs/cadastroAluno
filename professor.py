from endereco import Endereco
class Professor(Endereco):
    def __init__(self, cpf, nome, materia, rua, numero, bairro, cep):
       self.__cpf= cpf
       self.materia= materia
       self.nome=nome
       super().__init__(rua, numero, bairro, cep )



    def adicionarProfessor(self):
            cpf=input('Cpf:')
            materia= int(input('Materia:'))
            nome= input('Nome:')
            self.setCpf(cpf)
            self.setMateria(materia)
            self.setNome(nome)

    def getCpf(self):
        return self.__cpf
    
    def setCpf(self, cpf):
        self.__cpf= cpf

    def getMateria(self):
        return self.materia
    
    def setMateria(self, materia):
        self.materia= materia
    
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome= nome
    
    def getIdade(self):
        return self.idade
    
    def setIdade(self, idade):
        self.idade= idade

    def __str__(self):
        return f'CPF: {self.getCpf()} \nmateria: {self.getMateria()} \nNome: {self.getNome()}'
    

professor= Professor('111.111.111-11', 'Marcos Antonio', 'IP', 'Luiz Augusto', '25', 'Cagep', '54600000')
print(professor)