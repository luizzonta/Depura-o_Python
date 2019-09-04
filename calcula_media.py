import pdb
from media import Media

nome = str(input('Informe o nome do aluno:'))

notas = []

for i in range(1,5):
    notas.append(float(input('Informe a nota {}:'.format(i))))

media = Media(notas)
print('A Media do Aluno {} é: {} ' .format(nome, media.calcula_media()))
pdb.set_trace()
print('O Aluno {} está: {} ' .format(nome, media.resultado()))

