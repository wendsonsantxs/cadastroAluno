class Endereco():
    def __init__(self, rua, numero, bairro, cep):
        self.rua= rua
        self.__numero= numero
        self.bairro=bairro
        self.cep= cep


    def adicionarEndereco(self):
        rua=input('Rua:')
        numero= int(input('Numero:'))
        bairro= input('Bairro:')
        cep= input('Cep:')
        self.setRua(rua)
        self.setNumero(numero)
        self.setBairro(bairro)
        self.setCep(cep)



    def getNumero(self):
        return self.__numero
    
    def setNumero(self, numero):
        self.__numero= numero

    def getRua(self):
        return self.rua
    
    def setRua(self, rua):
        self.rua=rua
    
    def getBairro(self):
        return self.bairro
    
    def setBairro(self, bairro):
        self.bairro=bairro

    def getCep(self):
        return self.cep
    
    def setCep(self, cep):
        self.cep= cep

    def __str__(self):
        return f'Rua :{self.getRua()} \nNumero:{self.getNumero()} \nBairro: {self.getBairro()} \nCep: {self.getCep()}'

endereco= Endereco('Luiz Augusto', '25', 'Cagep', '54600000')
print(endereco)
    

