###AULA04 - 08/10/2024###

###ESTRUTURAS DE CONDIÇÃO ###

# IF ELSE   X   SWITCH CASE

#1) IF ELSE 
'''
mes=int(input('Digite um número entre 1 e 12:'))

if mes==1:
    print('janeiro')
elif mes==2:
    print('fevereiro')
elif mes==3:
    print('marco')
elif mes==4:
    print('abril')
elif mes==5:
    print('maio')
elif mes==6:
    print('junho')
elif mes==7:
    print('julho')
elif mes==8:
    print('agosto')
elif mes==9:
    print('setembro')
elif mes==10:
    print('outubro')
elif mes==11:
    print('novembro')
elif mes==12:
    print('dezembro')
else:
    print('Por favor forneça um número válido.')
    mes=int(input('Digite um número entre 1 e 12:'))
'''

#Atividades práticas com if/else e switch/case:

# 1) Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para iluminar um determinado cômodo de uma residência. 
# Dados de entrada: a potência da lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do cômodo. Considere que 
# a potência necessária é de 3 watts por metro quadrado e a cada 3 m² existe um bocal para uma lâmpada;

#  2) Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de 
# caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa 
# de azulejos possui 1,5 m²;

# 3) Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$ 4,87, escreva um 
# programa para ler: a marcação do odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de combustível gasto e o 
# valor total (R$) recebido dos passageiros. Calcular e escrever: a média do consumo em km/L e o lucro (líquido) do dia;

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

# 5) Escreva um programa que leia as notas das duas avaliações normais e a nota da avaliação optativa dos estudantes de uma turma. Caso o estudante não tenha feito a optativa, deve ser fornecido o valor -1. Calcular a média do semestre considerando que a prova optativa substitui a 
# nota mais baixa entre as duas primeiras avaliações. Escrever a média e mensagens que indiquem se o estudante foi aprovado, reprovado ou se 
# está em exame, de acordo com as informações abaixo: 
# Aprovado: média >= 6.0, Reprovado: média < 3.0, Exame: média >= 3.0 e < 6.0;

# 6) Escreva um programa para ler um valor e escrever se é positivo ou negativo. Considere o valor zero como positivo.

