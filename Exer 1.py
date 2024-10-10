#Atividades práticas com if/else e switch/case:

# 1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
# a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada

# Função para calcular o número de lâmpadas necessárias levando em conta um comodo sem janelas
'''def calcular_lampadas(potencia_lampada, largura, comprimento):
    # Calcula a área do cômodo
    area_comodo = largura * comprimento
    
    # Define a potência necessária (3 watts por m²)
    potencia_necessaria = area_comodo * 3
    
    # Calcula o número de bocais (1 bocal a cada 3 m²)
    bocais_necessarios = area_comodo // 3  # // operador de divisão inteira
    
    # Calcula o número de lâmpadas com base na potência de cada lâmpada
    lampadas_necessarias = potencia_necessaria / potencia_lampada
    
    # Se o número de lâmpadas for menor que os bocais, usar o número de bocais
    if lampadas_necessarias < bocais_necessarios:
        lampadas_necessarias = bocais_necessarios
    
    # Arredondar o número de lâmpadas para cima, já que não podemos ter meia lâmpada
    lampadas_necessarias = int(lampadas_necessarias) + (lampadas_necessarias % 1 > 0)
    
    return lampadas_necessarias

# Entrada de dados
potencia_lampada = float(input("Digite a potência da lâmpada (em watts): "))
largura = float(input("Digite a largura do cômodo (em metros): "))
comprimento = float(input("Digite o comprimento do cômodo (em metros): "))

# Calcula e exibe o número de lâmpadas necessárias
lampadas = calcular_lampadas(potencia_lampada, largura, comprimento)
print(f"Você precisará de {lampadas} lâmpada(s) para iluminar o cômodo.")'''

###Testando a formula: potência lampada 5 / largura 4 / comprimento 4 = 10 lampadas ###

#  2) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
# de azulejos possui 1,5 m²

# Função para calcular a quantidade de caixas de azulejos necessárias
'''def calcular_caixas_azulejos(comprimento, largura, altura):
    # Calcula a área das duas paredes com largura x altura
    area_paredes_largura = 2 * (largura * altura)
    
    # Calcula a área das duas paredes com comprimento x altura
    area_paredes_comprimento = 2 * (comprimento * altura)
    
    # Soma as áreas de todas as paredes
    area_total_paredes = area_paredes_largura + area_paredes_comprimento
    
    # Cada caixa cobre 1,5 m²
    area_por_caixa = 1.5
    
    # Calcula o número de caixas necessárias
    caixas_necessarias = area_total_paredes / area_por_caixa
    
    # Arredonda o número de caixas para cima, já que não podemos comprar meia caixa
    caixas_necessarias = int(caixas_necessarias) + (caixas_necessarias % 1 > 0)
    
    return caixas_necessarias

# Entrada de dados
comprimento = float(input("Digite o comprimento da cozinha (em metros): "))
largura = float(input("Digite a largura da cozinha (em metros): "))
altura = float(input("Digite a altura da cozinha (em metros): "))

# Calcula e exibe a quantidade de caixas necessárias
caixas = calcular_caixas_azulejos(comprimento, largura, altura)
print(f"Você precisará de {caixas} caixa(s) de azulejos para cobrir todas as paredes da cozinha.")'''

#Testando a formula: comprimento 5 / largura 5 / altura 4 = 54 caixas 


# 3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
#programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;

# Função para calcular a média de consumo e o lucro líquido
'''def calcular_rendimento(odometro_inicio, odometro_fim, litros_gastos, valor_recebido):
    # Calcula a distância percorrida
    distancia_percorrida = odometro_fim - odometro_inicio
    
    # Calcula a média de consumo (km por litro)
    consumo_medio = distancia_percorrida / litros_gastos
    
    # Preço do combustível
    preco_combustivel = 4.87
    
    # Calcula o custo total com combustível
    custo_combustivel = litros_gastos * preco_combustivel
    
    # Calcula o lucro líquido
    lucro_liquido = valor_recebido - custo_combustivel
    
    return consumo_medio, lucro_liquido

# Entrada de dados
odometro_inicio = float(input("Digite a marcação do odômetro no início do dia (em km): "))
odometro_fim = float(input("Digite a marcação do odômetro no final do dia (em km): "))
litros_gastos = float(input("Digite o número de litros de combustível gasto: "))
valor_recebido = float(input("Digite o valor total recebido dos passageiros (em R$): "))

# Calcula o rendimento e o lucro
consumo_medio, lucro_liquido = calcular_rendimento(odometro_inicio, odometro_fim, litros_gastos, valor_recebido)

# Exibe os resultados
print(f"Média de consumo: {consumo_medio:.2f} km/L")
print(f"Lucro líquido do dia: R$ {lucro_liquido:.2f}")'''

#Testando a formula: odometro inicio 120 / odometro fim dia 210 / litros gastos 15 / valor recebido 80,50 = Média consumo 6,00 km/l / lucro R$ 7,45


# 4) Escreva um programa que leia o código de origem de um produto e imprima na tela a região de sua procedência, conforme a tabela que foi passada:

'''
Código 1 : Região Sul
Código 2: Região Norte
Código 3: Região Leste
Código 4: Região Oeste
Códigos 5 ou 6: Região Nordeste
Códigos 7, 8 ou 9: Região Sudeste
Código 10: Região Centro-oeste 
Código 11: Região Noroeste'''

# Observação: caso o código não seja nenhum dos especificados, o produto deve ser encarado como “Importado”; 


'''codigo_produto = int(input("Digite o código de origem do produto: "))

# Verificação e impressão da região com base no código do produto
if codigo_produto == 1:
    print("A região de procedência do produto é: Região Sul")
elif codigo_produto == 2:
    print("A região de procedência do produto é: Região Norte")
elif codigo_produto == 3:
    print("A região de procedência do produto é: Região Leste")
elif codigo_produto == 4:
    print("A região de procedência do produto é: Região Oeste")
elif codigo_produto in [5, 6]:
    print("A região de procedência do produto é: Região Nordeste")
elif codigo_produto in [7, 8, 9]:
    print("A região de procedência do produto é: Região Sudeste")
elif codigo_produto == 10:
    print("A região de procedência do produto é: Região Centro-oeste")
elif codigo_produto == 11:
    print("A região de procedência do produto é: Região Noroeste")
else:
    print("A região de procedência do produto é: Importado")'''

#5 Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. 
# Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa 
# substitui a nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, 
# reprovado ou se está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;


'''nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota_optativa = float(input("Digite a nota da avaliação optativa (-1 se não fez): "))

# Verifica se a nota optativa foi fornecida
if nota_optativa != -1:
    # Substitui a nota mais baixa entre as duas primeiras avaliações pela nota optativa
    if nota1 < nota2:
        media = (nota2 + nota_optativa) / 2
    else:
        media = (nota1 + nota_optativa) / 2
else:
    # Calcula a média normal
    media = (nota1 + nota2) / 2

# Verifica a situação do estudante
if media >= 6.0:
    situacao = "Aprovado"
elif media < 3.0:
    situacao = "Reprovado"
else:
    situacao = "Exame"

# Exibe a média e a situação
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")'''


# 6) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

valor = float(input("Digite um valor: "))

# Verifica se o valor é positivo ou negativo
if valor >= 0:
    situacao = "positivo"
else:
    situacao = "negativo"

# Exibe a situação do valor
print(f"O valor {valor} é {situacao}.")

