class Curso():
    def __init__(self):
        self.curso= None
        self.disciplina= []
        self.escolhaCurso()
        print(self.curso)


    def escolhaCurso(self):
        print('Cursos')
        print('1- Sistemas de informação')
        print('2- Economia')
        print('3- Administração')
        escolha= int(input('Escolha por numero:'))
        if(escolha==1):
            self.curso= 'Sistemas de informação'
        elif(escolha==2):
            self.curso=  'Economia'
        elif(escolha==3):
            self.curso=  'Administração'
        else:
            print('Escolha invalida, tente novamente!')
            self.escolhaCurso()

curso= Curso()
        