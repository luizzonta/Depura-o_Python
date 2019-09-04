class Media:
        media_aluno = 0.0
        notas = None
        
        def __init__(self, notas):
                self.notas = notas

        def calcula_media(self):
                for i in range(0,4):
                        self.media_aluno += self.notas[i]
                self.media_aluno = self.media_aluno / 4
                return self.media_aluno

        def resultado(self):
                if (self.media_aluno >= 7):
                        return "Aprovado"
                elif (7 > self.media_aluno >= 4):
                        return "Em Exame"
                elif (self.media_aluno < 4):
                        return "Reprovado"
