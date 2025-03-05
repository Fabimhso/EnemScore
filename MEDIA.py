# Receber dois numeros do usuario
numero1 = float(input("Escreva aqui sua nota em Linguagens e Codigos:"))
numero2 = float(input("Escreva aqui sua nota em Matematica:"))
numero3 = float(input("Escreva aqui sua nota em Ciencias da Natureza:"))
numero4 = float(input("Escreva aqui sua nota em Ciencias Humanas:"))
numero5 = float(input("Escreva aqui sua nota em Redacao:"))

# Calcular media dos numeros
media = (numero1 + numero2 + numero3 + numero4 + numero5) / 5

# Imprimir media na tela
print(f"Sua media no ENEM foi: {media}")

# Fechar programa
input("Pressine ENTER para fechar...")
