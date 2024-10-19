'''Leia três pares de números inteiros fornecidos pelo usuário, calcule e imprima a soma de cada par separadamente.
Utilize tratamento de erros para garantir que os valores inseridos sejam válidos e, se o número for ÍMPAR,
ter uma exceção personalizada.'''

class NumeroImparError(Exception):
    
    def __init__(self, numero):
        super().__init__(f"Erro: O número {numero} é ímpar. Somente números pares são permitidos.")

def ler_par_inteiro():
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            if numero % 2 != 0:
                raise NumeroImparError(numero)
            return numero
        except NumeroImparError as e:
            print(e)
        except ValueError:
            print("Erro: Você não digitou um número inteiro válido. Tente novamente.")

def somar_pares():
    for i in range(1, 4):
        print(f"\nPar {i}:")
        num1 = ler_par_inteiro()
        num2 = ler_par_inteiro()
        soma = num1 + num2
        print(f"A soma do par {i} é: {soma}")

# Chama a função principal
somar_pares()
