'''import random
secret_no = random.randint(1,5)
for i in range(1,10):
    choice = input('Enter the choice :')
    choice = int(choice)
    res = 'Your choice is too high' if choice > secret_no else 'your choice is too low'
    print(res)
    if choice == secret_no:
        print('Your choice is correct',str(i) ,'attempts')
        break
else:
     print('your choice is wrong and your attempts is')
'''


import random
secret_no = random.randint(1,20)

for i in range(1,6):
      choice = int(input('Enter the Number :'))
      if choice > secret_no :
            print('Your choice is too high')
      elif  choice < secret_no:
            print('your choice is too low')
      elif choice == secret_no:
            print('Your choice is correct',i ,'attempts')
            break
      else:
            print('your choice is wrong and your attempts is',i)
            print('Your choice is correct',str(i) ,'attempts')
            break
else:
            print('your choice is wrong and your attempts is',str(i))
