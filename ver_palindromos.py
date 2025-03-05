def eh_palindromo(palavra):
    palavra_invertida = palavra[::-1]
    return palavra == palavra_invertida

# Solicita a palavra ao usuário
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# Verifica se a palavra é um palíndromo
if eh_palindromo(palavra):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" não é um palíndromo.')