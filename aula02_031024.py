'''
Aula 01 - 01/10/24 Aprendemos a lógica da programação e tiramos as diversas dúvidas da turma sobre Big Data
Aula 02 - 03/10/24 Fizemos um texto para praticar a lógica da programação, vimos o sites da linguagem Python (https://www.python.org/
https://python.org.br/) e aprendemos sobre a ferramenta de desenvolvimento VSCode (https://code.visualstudio.com/)
Aula 03 - 04/10/24 Aprendemos sobre a concdicional IF (https://docs.python.org/pt-br/3/tutorial/controlflow.html#if-statements) e 
sobre o GITHUB (https://github.com/)
'''

###ASSUNTO1###
#print('string')
#Comando para exibir meu conteúdo no terminal
'''
Dentro dos tipos de arquivo em Python,
temos os tipo texto que são conhecidos
como STRINGS; no exemplo acima, eu utilizei
o comando PRINT para exibir uma string no meu
terminal Python
'''
#Sempre que coloco a # no inicio da frase tudo que for digitado não será lido pelo código, usamos para incluir informação, 
# o mesmo acontece quando colocamos ''' no inicio e no final de um texto, também não será lido pelo código e é usados para textos maiores

#Agora vou textar alguns comando para ver como aparece no terminal, depois vou colocar # no inicio de cada frase para continuar 
# testando os próximos.

#print('morango','banana') #exibiu uma informaçãp em texto, sempre escrever texto dentro de aspas' '
#print(123) # exibiu uma informação de número inteiro - No PY Numero Inteiro é INT
#print(37438,23534) # exibiu 2 núm inteiros 
#print(2963.44) #Exibiu um número decimal - No PY Numero decimal é FLOAT
#print(True) # No PY True e False é conhecido como BOOLEAN (Verdadeiro ou falso)  ATENÇÃO: No meu teste fez diferença ter a 
# primeira letra maiuscula do True e do False
#print(False) #Boolean
#print(None) #none
#print(['string']) #lista
#print(('string')) #tupla 
#print({'string':'texto}'}) #dicionário

###CONDICIONAIS E IDENTAÇÃO###  04/10/2024

#temperatura1=36  #Cada VARIAVEL armazena apenas 1 INFORMAÇÃO por vez. Se o nome da variavel for o mesmo, o PY ira SOBRESCREVER essa informação.
#temperatura2=37,5  #Por isso cada temperatura ao lado está com nome diferente
#temperatura3=39,6
#print(temperatura1,temperatura2,temperatura3)

#If temperatura1<37.5:
#    print('Você não está com febre')
#elif temperatura1==37.5:
#    print('Você está febril')
#else:
#    print('Você está com febre')

#### VER PQ O CÓDIGO NÃO FUNCIONOU LINHA 40 A 45 e depois apagar essas linhas, vou deixar a explicação abaixo###
###Agora a explicação###

#if temperatura1<37.5: #Nosso primeiro teste lógico. Sempre termino com ':'
#   print("Você não está com febre.") #Aqui temos uma regra de IDENTAÇÃO: toda resposta à minha condição deve estar DENTRO do meu if 
# (lembrem-se da tecla TAB para corrigir a identação)
#elif temperatura1==37.5: #Nosso segundo teste lógico. Sempre termino com ':'
#    print("Você está febril.")
#else: #Última opção condicional. É requisitada quando todas as condições anteriores deram FALSE. Haverão momentos em que o 'else' não 
# precisará ser escrito (quando eu não desejo dar resposta ao 'else')
#    print("Você está febre.")

##Exemplo com idades##
#idade=13

#if idade<16:
#     print("Menor de Idade")
#elif idade>=16 or idade<=18:
#     print("aguarde")
#else: 
#     print("Maior de idade")

#_________________________________________
###COMPARATIVOS NO PRINT###

#fruta1='jambo'
#fruta2='maçã'
#fruta3='uva'
#fruta4='maçã'
#num1=67
#num2=12
#num3=12.0
#num4=67.1

#print(fruta1==fruta3)  #resposta False
#fruta1=fruta3
#print(fruta1)           #resposta Uva

#print(fruta1==fruta4)   #resposta False
#print(fruta2==fruta4)   #resposta True
#print(fruta3==fruta4)   #resposta False
#print(num1==num2)       #resposta False
#print(num1!=num2)       #resposta True
#print(num1>num2)        #resposta True
#print(num1<num2)        #resposta False
#print(num2==num3)       #resposta True
#print(num1!=num4)       #resposta True

'''Informações Importantes sobre CONECTIVOS DE CONDIÇÕES
<= MENOR OU IGUAL
>= MAIOR OU IGUAL
== IGUAL
!= DIFERENTE 

QUANDO USA = SOZINHO ESTÁ AVISANDO AO PY QUE ALGO É IGUAL 
EX: X=Y  A PARTIR DE AGORA O VALOR DE X É IGUAL AO DE Y veja exemplo linha 80

_______Foi dito na aula, não lembro pra que serve________________________________
https://www.w3schools.com/python/
https://coddy.tech/
https://www.codingame.com/start/
https://www.hackerrank.com/
____________________________________________________________'''

