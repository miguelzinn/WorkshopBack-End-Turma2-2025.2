'''
numeros = [10, 20, 30]
indice = int(input("Digite um índice para acessar a lista: ")) 

print(numeros[indice])

'''
numeros = [10, 20, 30]
while True:
    try:
        indice = int(input("Digite um índice para acessar a lista: ")) 
        print(numeros[indice])
        break
    except IndexError:
        print(f"digite um número de 0 a {len(numeros)-1}")
    
    