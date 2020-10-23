print('Enter your number:')
x = input()
x = int(x)

for y in range(1, x):
  print(y)
  
str = [1, 5, 4, 16, 0, 52, 17]

chetni = 0, nechetni = 0

for x in str:
    if (str[x] % 2) == 0:
        ++chetni
    else:
        ++nechetni
    
    
  print('Chetni:', chetni)
  print('neChetni:', nechetni)

#izvinete che ne gi napisah vsichkite no imah problemi s git i dokato zapochna da pisha chasa beshe svurshil