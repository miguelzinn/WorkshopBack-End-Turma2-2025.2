
dados = {
    "nome": "Isaac ",
    "idade": 25,
    "cidade": "São Paulo"
}
while True:
    try:
        chave = input("Digite a chave que deseja acessar: ")
        print(f"O valor da chave '{chave}' é: {dados[chave]}")
        break
    except KeyError:
        print("A chave digitada não existe.")