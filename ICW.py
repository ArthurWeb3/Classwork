#1, With while function and loop breaks
print('Where would you like to go?')
print('1 for Product Page')
print('2 for Customer Page')
print('3 for Registration Page')
while(True):
  UserInput = int(input())
  if UserInput == 1:
    print("You will now be directed to the product page")
    break
  elif UserInput == 2:
    print("You will now be directed to the customer page")
    break
  elif UserInput == 3:
    print("You will now be directed to the registration page")
    break
  else:
    print("Please select 1, 2, or 3")

#2, #Deciding on computer parts to invest in
print('Is it absolutely necessary? Yes, No, or Maybe?')
part = str(input())
if part == 'Yes':
    print('Do research first, then decide')
elif part == 'Maybe':
    print("Wait three days, then reconsider")
else: 
    print("Save money and don't buy it!")

#3, Logical Error
income = 35000
if income <=10000:
  tax = .05
elif income <=20000:
  tax = .10
elif income >=50000:
  tax = .15
else:
  tax = .20
print(tax)