class Disciplinas():
    def __init__(self):
        self.disciplina= None
        self.professor= []
        self.alunos=[]
        self.disciplinas()
        print(self.disciplina)


    def disciplinas(self):
        print('Disciplinas')
        print('1- Calculo')
        print('2- Psicologia')
        print('3- Introdução a Administração')
        print('4- Metodologia do Trabalho Cientifico')
        escolha= int(input('Escolha por numero:'))
        if(escolha==1):
            self.disciplina= 'Calculo'
        elif(escolha==2):
            self.disciplina=  'Psicologia'
        elif(escolha==3):
            self.disciplina=  'Introdução a Administração'
        elif(escolha==4):
            self.disciplina=  'Metodologia do Trabalho Cientifico'
        else:
            print('Escolha invalida, tente novamente!')
            self.disciplinas()


disci= Disciplinas()

        