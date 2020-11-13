#1

number = input ("enter a num : ")
count = input("enter the count : ")

for x in range(1, int(count) + 1, 1):
    print(int(number) * x)

#2

string = input("Enter a string:")
vowels = 0

for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels++
            
print("Number of vowels are:")
print(vowels)

#3

items = ["my", 1, "turtle", "explain", 3.14]

new_items = [item for item in items if not item.isdigit()]

print(new_items)

#4

num = int(input("Enter a number:"))
temp = num
rev = 0

while(num > 0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
    
if(temp == rev):
    print("The number is palindrome")
    
else:
    print("Not a palindrome")