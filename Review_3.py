#Input Function & Loops 
x = 0 
while x <= 5:
  print('Hello world!')
  x = x+1 
#Don't hit backspace on that "x" and hit run :)

#If/Else review
prompt = 'how old are you?'
age = input(prompt)
if int(age) >=21:
  print('legal drinking age')
else:
  print('underage')

#Concatenation with +=
prompt = 'Welcome!'
prompt += "\nWhat is your first name?"
print(prompt)

#While Loop
x = 0 
while x <= 5:
  print('Hello world!')
  x = x+1 
#Will continue while x<=5 is true! 

#While Loop
stopping_pt = input('Enter a number:')
x = 0
while x<= int(stopping_pt):
  print('Hi')
  x=x+1

#For Loop
for x in range (1,10,2):
  print(x)

#List Pratice
regions = ['W','C','S','E']
for region in regions:
  print(region)

#While, If, Else 
active = True
while active:
  message = input(prompt)
  if message == 'quit':
    active = False
  else:
    print(message)

#While Loop
sum = 0
i = 1
while i<=50:
  sum += i #or, sum = sum+i
  i+=1
print(sum)

#For Loop
sum = 0 
for i in range(1,51):
  sum +=i #or, sum=sum+i
print(sum)