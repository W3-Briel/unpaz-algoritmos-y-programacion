## factorial de forma iterativa.

def factorial_iterativo(num):
    acumulador = 1
    if num == 0 or num == 1:
        return print(1)
    for i in range(1,num+1):
        acumulador *= i
    return acumulador

factorial_iterativo(6)

## factorial de forma recursiva.

def factorial_recursivo(num):
    if num in (1,0): return num ## caso base
    return num * factorial_recursivo(num-1) ## caso recursivo

print(factorial_recursivo(6))
# print(factorial_recursivo(6))