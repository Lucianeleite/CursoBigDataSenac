''' Atividade 1
Um pescador precisa pagar uma multa caso o peso dos peixes exceda 100 quilos. 
Crie uma função para calcular a multa, se aplicável'''


# def calcular_multa():
#     peso_peixes = float(input("Digite o peso dos peixes em quilos: "))
#     peso_maximo = 100  
#     valor_multa_por_quilo = 10  
    
#     if peso_peixes > peso_maximo:
#         excesso = peso_peixes - peso_maximo
#         multa = excesso * valor_multa_por_quilo
#         print(f"O pescador deve pagar uma multa de R$ {multa:.2f}.")
#     else:
#         print("O pescador não precisa pagar multa.")

# calcular_multa()



'''Atividade 2
Crie um programa que faça a leitura da altura e do peso de N pessoas para o cálculo do IMC, 
mostrando ao final a classificação de acordo com a tabela de IMC.'''


# def calcular_imc(peso, altura):
#     return peso / (altura ** 2)

# def classificar_imc(imc):
#     if imc < 18.5:
#         return "Abaixo do peso"
#     elif 18.5 <= imc < 24.9:
#         return "Peso normal"
#     elif 25 <= imc < 29.9:
#         return "Sobrepeso"
#     elif 30 <= imc < 34.9:
#         return "Obesidade grau 1"
#     elif 35 <= imc < 39.9:
#         return "Obesidade grau 2"
#     else:
#         return "Obesidade grau 3"

# def main():
#     N = int(input("Quantas pessoas serão analisadas? "))
    
#     for i in range(N):
#         print(f"\nPessoa {i+1}:")
#         peso = float(input("Digite o peso em kg: "))
#         altura = float(input("Digite a altura em metros: "))
        
#         imc = calcular_imc(peso, altura)
#         classificacao = classificar_imc(imc)
        
#         print(f"IMC: {imc:.2f}")
#         print(f"Classificação: {classificacao}")

# if __name__ == "__main__":
#     main()


'''Atividade3
Crie funções que mostrem um cardápio de um restaurante (pelo menos 4 itens) e que permitam realizar pedidos 
e fechar a conta.'''

# def mostrar_cardapio():
#     cardapio = {
#         1: ("Hamburguer", 45.00),
#         2: ("Fritas", 30.00),
#         3: ("Salada", 20.00),
#         4: ("Sorvete", 10.00)
#     }

#     print("\nCardápio:")
#     for codigo, (item, preco) in cardapio.items():
#         print(f"{codigo} - {item}: R$ {preco:.2f}")

#     return cardapio


# def realizar_pedido(cardapio):
#     total = 0
#     pedidos = []

#     while True:
#         opcao = int(input("\nDigite o número do item que deseja pedir (ou 0 para fechar o pedido): "))
        
#         if opcao == 0:
#             break
#         elif opcao in cardapio:
#             item, preco = cardapio[opcao]
#             pedidos.append((item, preco))
#             total += preco
#             print(f"{item} adicionado ao pedido. Total parcial: R$ {total:.2f}")
#         else:
#             print("Opção inválida. Tente novamente.")
    
#     return pedidos, total

# def fechar_conta(pedidos, total):
#     print("\n--- Detalhes do pedido ---")
#     for item, preco in pedidos:
#         print(f"{item}: R$ {preco:.2f}")
    
#     print(f"\nTotal a pagar: R$ {total:.2f}")
#     print("Obrigado pela preferência!")

# def main():
#     cardapio = mostrar_cardapio()
#     pedidos, total = realizar_pedido(cardapio)
#     fechar_conta(pedidos, total)

# if __name__ == "__main__":
#     main()


