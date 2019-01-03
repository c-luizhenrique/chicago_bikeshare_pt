# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

for index,sample in zip(range(20), data_list[:20]):
  print("Linha {}: {}".format(index, sample))

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

for index,sample in zip(range(20), data_list[:20]):
  if sample[6].title()=='':
    print("O genenero da linha {} é: Não informado".format(index))
  else:
    print("O genenero da linha {} é: {}".format(index, sample[6].title()))

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
  """
  Função que adiciona os itens de uma columa a uma nova lista, na mesma ordem..
  Argumentos:
    data: Lista a ser lida.
    index: Coluna que deverá originar a nova lista.
  Retorna:
    Uma lista que compreende todos os valores da coluna representada por index.

  """
  column_list = []
  # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
  for item in data:
    column_list.append(item[index])
  return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0

for data in data_list:
  if data[-2]=='Male':
    male+=1
  elif data[-2]=='Female':
    female+=1 


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
  """
  Função que conta a quantidade de ocorrências dos gêneros Masculino e Feminino de uma determinada lista.
  Argumentos:
    data_list: Lista a ser lida.
  Retorna:
    Uma lista com o somatório de ocorrências 'Male' na posição 0 e o somatório de ocorrências 'Female' na posição 1.

  """

  male = 0
  female = 0

  for data in data_list:
    if data[-2]=='Male':
      male+=1
    elif data[-2]=='Female':
      female+=1 

  return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.
def most_popular_gender(data_list):
  """
  Função que determina se e qual gênero (Male e Female) aparece mais vezes em uma determinada lista.
  Argumentos:
    data_list: Lista a ser lida.
  Retorna:
    Um string contendo o gênero que mais apareceu ('Male' ou 'Female') ou 'Equal', em caso de empate.

  """
  [male, female] = count_gender(data_list)
  if male > female:
    answer = "Male"
  elif male < female:
    answer = "Female"
  else:
    answer = "Equal"
  return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_type(data_list):
  """
  Função que conta a quantidade de ocorrências dos tipos de cliente ('Subscriber' e 'Costumer') de uma determinada lista.
  Argumentos:
    data_list: Lista a ser lida.
  Retorna:
    Uma lista com o somatório de ocorrências 'Subscriber' na posição 0 e o somatório de ocorrências 'Costumer' na posição 1.

  """
  subscriber = 0
  customer = 0
  dependent = 0

  for data in data_list:
    if data[-3] == 'Subscriber':
      subscriber+=1
    elif data[-3] == 'Customer':
      customer+=1 
    elif data[-3] == 'Dependent':
      dependent+=1

  return [subscriber, customer, dependent]

type_list = column_to_list(data_list, -3)
types = ["Subscriber", "Customer", 'Dependent']
quantity = count_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Cliente')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Cliente')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Por que nem todas as linhas retornam valores \'Male\' ou \'Female\', existem casos onde nenhum valor é retornado para a coluna \'Gender\'."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
total_trip = 0.
num_trip = 0

for index, item in enumerate(trip_duration_list):
  trip_duration_list[index] = float(item)

trip_duration_list.sort()

for row in trip_duration_list:
  total_trip += row
  num_trip += 1
  if row < min_trip or min_trip == 0:
    min_trip = row
  if row > max_trip:
    max_trip = row

mean_trip = total_trip / num_trip

if num_trip % 2 == 0:
  median_trip = (trip_duration_list[num_trip/2] + trip_duration_list[num_trip/2 + 1]) / 2
else:
  median_trip = trip_duration_list[num_trip //2]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
Função de exemplo com anotações.
Argumentos:
    param1: O primeiro parâmetro.
    param2: O segundo parâmetro.
Retorna:
    Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
  """
  Função que determina quais são os elementos de uma lista bem como a quantidade de ocorrências de cada um desses elementos.
  Argumentos:
    data_list: Lista a ser lida.
  Retorna:
    Uma lista com todos os elementos encontrados e uma lista com o somatório de ocorrências dos elementos, ambas na mesma ordem.

  """
  item_types = []
  item_types.extend(list(set(column_list)))

  count_items = []
  for item in item_types:
    count_items.append(column_list.count(item))
  return item_types, count_items

#Como sugerido, verifiquei a quantidade de tipos de cliente, optei por fazer aqui para não precisar mover a função.
column_list = column_to_list(data_list, -3)
types, counts = count_items(column_list)
print("Tipos:", types, "Counts:", counts)

if answer == "yes":
  # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
  column_list = column_to_list(data_list, -2)
  types, counts = count_items(column_list)
  print("\nTAREFA 12: Imprimindo resultados para count_items()")
  print("Tipos:", types, "Counts:", counts)
  assert len(types) == 3, "TAREFA 12: Há 3 tipos de gênero!"
  assert sum(counts) == 1551505, "TAREFA 12: Resultado de retorno incorreto!"
  # -----------------------------------------------------
