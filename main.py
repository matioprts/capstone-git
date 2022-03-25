print('Funciones disponibles:')
print('\t[1] Top 10 retweeted tweets')
print('\t[2] Top 10 users')
print('\t[3] Top 10 days')
print('\t[4] Top 10 hashtags')

target_function = 'aux'
while target_function not in ['1', '2', '3', '4']:
  target_function = input('Ingrese el número de la función a ejecutar: ')
  print('Error: Favor ingrese un número del 1 al 4')
  print()

if target_function == '1':
  print('Función 1 elegida')
elif target_function == '2':
  print('Función 2 elegida')
elif target_function == '3':
  print('Función 3 elegida')
elif target_function == '4':
  print('Función 4 elegida')
