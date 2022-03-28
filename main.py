import json
import functions

with open('farmers-protest-tweets-2021-03-5.json') as json_file:
  dataset = json.loads("[" + json_file.read().replace("}\n{", "},\n{") + "]") # https://stackoverflow.com/questions/51919698/cant-parse-json-file-json-decoder-jsondecodeerror-extra-data

while True:
  print('Funciones disponibles:')
  print('\t[1] Top 10 tweets retweeteados')
  print('\t[2] Top 10 usuarios por cantidad de tweets')
  print('\t[3] Top 10 dias por cantidad de tweets')
  print('\t[4] Top 10 hashtags')
  print('\t[5] Salir')

  target_function = input('Ingrese el número de la función a ejecutar: ')
  while target_function not in ['1', '2', '3', '4', '5']:
    print('Error: Favor ingrese un número del 1 al 5')
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
    result = functions.top_users(dataset)
    print()
    print('Top 10 usuarios por cantidad de tweets:')
    count = 1
    for tweet in result:
      print(f'\t[{count}] {tweet[0]}: {tweet[1]} tweets')
      count += 1
    print()
  elif target_function == '3':
    result = functions.top_days(dataset)
    print()
    print('Top 10 dias por cantidad de tweets:')
    count = 1
    for tweet in result:
      print(f'\t[{count}] {tweet[0]}: {tweet[1]} tweets')
      count += 1
    print()
  elif target_function == '4':
    result = functions.top_hashtags(dataset)
    print()
    print('Top 10 hashtags:')
    count = 1
    for tweet in result:
      print(f'\t[{count}] {tweet[0]}: {tweet[1]} tweets')
      count += 1
    print()
  elif target_function == '5':
    print()
    print('Finalizando el programa...')
    print()
    break
