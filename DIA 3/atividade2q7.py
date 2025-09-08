def validar_idade(idade):
    if idade < 0 or idade > 120:
        raise ValueError("A idade deve estar entre 0 e 120 anos!")
    return f"Idade válida: {idade}"

while True:
    try:
        idade = int(input("Digite sua idade: "))
        print(validar_idade(idade))
        break  
    except ValueError as e:
        print(f"Entrada inválida. {e} Por favor, tente novamente.")