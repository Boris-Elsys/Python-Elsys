#1
a = str(input('Enter a sentence: ' ))
vowels = ('a''e''i''o''u''A''E''I''O''U')

for vowel in vowels:
    a = a.replace(vowel, vowel * 4)
    
print(a)

#2

a = input('Enter something: ')
count = 0
  
for i in a: 
    count += 1
        
print(count)

#3

import math

num = int(input('Enter a number: '))
num_cop = num
count = 0

while num >= 2:
    num = math.sqrt(num)
    count += 1
    
print(num_cop, '-->', count)

#4

num = int(input("Enter number : "))
sums = 0;

for i in range(0, num + 1):
   if i > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           sums += i;

print(sums)


