import json
import functions

with open('farmers-protest-tweets-2021-03-5.json') as json_file:
  dataset = json.loads("[" + json_file.read().replace("}\n{", "},\n{") + "]") # https://stackoverflow.com/questions/51919698/cant-parse-json-file-json-decoder-jsondecodeerror-extra-data

# with open('test.json') as json_file:
#   dataset = json.loads("[" + json_file.read().replace("}\n{", "},\n{") + "]")

print('Funciones disponibles:')
print('\t[1] Top 10 retweeted tweets')
print('\t[2] Top 10 users')
print('\t[3] Top 10 days')
print('\t[4] Top 10 hashtags')

target_function = input('Ingrese el número de la función a ejecutar: ')
while target_function not in ['1', '2', '3', '4']:
  print('Error: Favor ingrese un número del 1 al 4')
  print()
  target_function = input('Ingrese el número de la función a ejecutar: ')


if target_function == '1':
  result = functions.top_retweets(dataset)
  print()
  print('Top 10 retweeted tweets:')
  count = 1
  for tweet in result:
    print(f'\t[{count}] {tweet[0]}: {tweet[1]} retweets')
    count += 1
  print()
elif target_function == '2':
  print('Función 2 elegida')
elif target_function == '3':
  print('Función 3 elegida')
elif target_function == '4':
  print('Función 4 elegida')
