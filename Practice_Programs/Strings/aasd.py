s1 = input('Enter: ')

s2 = input('Enter: ')

index = 0

letter = ''

instance = 0

for char in s2:

 if char in s1:

   if char == letter:

     instance = s1.find(char, instance+1)

   elif char != letter:

     instance = s1.find(char)

     instance = int(instance)

   if instance > index:

     index = instance

     valid = True

     letter = char

   else:

     valid = False

 else:

   valid = False

 

if valid == True:

 print('true')

else:

 print('not true')