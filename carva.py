class Materia:
    def __init__(self, disciplina, vagas=0):
        self.disciplina = disciplina
        self.vagas = vagas
        self.alunos = []
    
    def InscreverAluno(self, aluno):
        if len(self.alunos) < self.vagas and aluno not in self.alunos:
            self.alunos.append(aluno)
        elif aluno in self.alunos:
            print("O aluno ja esta inscrito!")
        else:
            print("Vagas insuficientes!")
    
    def ConsultarVagas(self):
        print("Vagas Totais: {} Vagas Livres {}".format(self.vagas, self.vagas - len(self.alunos)))

    def __str__(self):
        print("A disciplina {} tem {} vagas".format(self.disciplina, self.vagas))

    


MAB243 = Materia("COMP1",10)
print(MAB243)
