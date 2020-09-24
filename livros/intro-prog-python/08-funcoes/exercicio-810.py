'''
    Exercício 8.10 - Reescreva a função para cálculo da sequência de Fibonacci, sem utilizar recursão.
'''
def fibonacci(n):
    fibo = None
    anterior = None
    atual = None
    x = 1
    while x <= n:
        if x == 0:
            fibo = 0
        elif x == 1:
            anterior = 0
            fibo = 1
        elif x == 2:
            anterior = 1
            fibo = 1
        else:
            atual = fibo
            fibo = atual + anterior
            anterior = atual
            atual = fibo
        x += 1

    return fibo

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))

