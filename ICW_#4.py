#Positional vs Keyword
def describe_pet(animal_type, pet_name):
  print("My"+ animal_type + "is named"+pet_name.title()+".")

#Positonal 
describe_pet('hamster','harry')

#Keyword
describe_pet(animal_type='hamster',pet_name='harry')

def describe_pet(animal_type, pet_name):
  print("My "+ animal_type + " is named "+pet_name.title()+".")

describe_pet('Harry', 'hamster')

describe_pet(animal_type='hamster',pet_name='harry')

#Exercises 
#1
def describe_pet(pet_name, animal_type='dog'):
  print()

def make_shirt(size,text):
  print('The size of the shirt is ' + size.title() + ', and the text on it says ' + text+".")

make_shirt('M', '110A is cool!')

#2
def InviteGuests (guest1, guest2, guest3):
  print('Hey ' + guest1 +", " + guest2 + ", " + guest3 + ', are you  all available on the 19th?')
InviteGuests('Sally', 'Bob', 'Jerry')

#3
def CalcSalary (HourlyWage, HoursWorked):
  print('I get paid ' + HourlyWage + " to work " + HoursWorked + " hours a day.")
CalcSalary ('$18', '8')

#4
def HelloWorld (Planet, Moon):
  print('I come from the planet ' + Planet + " which has the moon " + Moon + " orbiting it.")
HelloWorld('Jupiter', 'Ganymede')

#5
def SQNum (Num1, Num2):
  SquaredNum = SQNum(Num1)
  print(SquaredNum)

#6
def Menu(Apps, Entree):
  print('Can I order a ' + Apps + ' and ' + Entree + ' to go please?')

#7
def GetUserInfo(Greeting):
     UserInfo = input(Greeting)
     return(UserInfo)
GetUserInfo('')