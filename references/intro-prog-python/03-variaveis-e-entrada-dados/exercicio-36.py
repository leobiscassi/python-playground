'''
    Exercício 3.6 - Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
    Para ser aprovado, todas as médias do aluno devem ser maior que 7. Considere que o aluno cursa apenas
    três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: materia1, materia2 e materia3.
'''
materia1, materia2, materia3 = 10, 8, 9
aprovado = materia1 > 7 and materia2 > 7 and materia3 > 7
print("O aluno foi aprovado? {}".format(aprovado))