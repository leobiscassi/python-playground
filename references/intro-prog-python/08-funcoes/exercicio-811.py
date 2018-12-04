'''
    Exercício 8.11 - Escreva uma função para validar uma variável string. Essa função recebe
    como parâmetro a string, o número mínimo e máximo de caracteres. Retorne verdadeiro se o
    tamanho da string estiver entre os valores de máximo e mínimo, e falso em caso contrário.
'''
def valida_string(string, minimo, maximo):
    if len(string) < minimo or len(string) > maximo:
        return False
    else:
        return True

print(valida_string("Validação", 3, 5))
print(valida_string("Validação", 3, 10))
print(valida_string("Teste", 6, 10))

