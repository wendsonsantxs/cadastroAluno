class Sala():
    def __init__(self, nome, capacidade):
        self.nome= nome
        self.__capacidade= capacidade


    def adicionarSala(self):
        nome = input('Sala:')
        capac = int(input('Capacidade'))
        self.setNome(nome)
        self.setCapacidade(capac)



    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome= nome

    def getCapacidade(self):
        return self.__capacidade
    
    def setCapacidade(self, capacidade):
        self.__capacidade= capacidade

    def __str__(self):
        return f'Sala:{self.getNome()} \nCapacidade: {self.getCapacidade()}'

sala= Sala('sala 1', 20)
print(sala)


    
    


    
