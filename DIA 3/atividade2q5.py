'''
    # 1 os possiveis erros no código abaixo são: TypeError, ValueError e ZerodivisionError
 
    def dividir(a, b):
    return a / b

num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

resultado = dividir(int(num1), int(num2))
print(f"Resultado: {resultado}")

    # 2:
'''
def dividir(a, b):
    return a / b

while True:
    try:
        num1 = input("Digite o primeiro número: ")
        num2 = input("Digite o segundo número: ")

        resultado = dividir(int(num1), int(num2))
        print(f"Resultado: {resultado}")
        break

    except ValueError:
        print("Entrada inválida, digite apenas números inteiros.")

    except ZeroDivisionError:
        print("Divisão por zero não é permitida.")

    except TypeError:
        print("Entrada inválida, digite apenas números")
    

    
    


