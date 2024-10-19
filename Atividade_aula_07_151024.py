'''Crie um código que seja capaz de ler (usuario vai dar a informação) e armazenar uma sequência de 20 números
pares e 20 números ímpares.
 Obs: utilize estruturas de repetição para fechar esse conjunto de números. Utilizar input pois os usuarios 
que vao indicar os números'''

pares = []
impares = []

while len(pares) < 20 or len(impares) < 20:
    try:
        numero = int(input("Por favor, digite um número: "))
        
       
        if numero % 2 == 0:
            if len(pares) < 20:  
                pares.append(numero)
            else:
                print("Você já inseriu 20 números pares.")
        else:
            if len(impares) < 20:  
                impares.append(numero)
            else:
                print("Você já inseriu 20 números ímpares.")
    except ValueError:
        print("Por favor, digite um número válido.")

print("\nNúmeros pares:", pares)
print("Números ímpares:", impares)