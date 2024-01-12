print('Welcome to the Elite101 Chatbox!')

name = input('What is your name?')
print(f'Its nice to meet you {name}! ')

age = input('How old are you?')
print(f'{age} is a great age to be! How can I help you today?\n')


print('Please choose from the following options:')
options = ['option 1', 'option 2', 'option 3', 'Exit the conversation']
for option in options:
  print(option)

while options != 'Exit the conversation':
  option_choice = input('\nChoose an option: ')
  
  if option_choice == 'option 1':
    print('you chose option 1')
    
  elif option_choice == 'option 2':
    print('you chose option 2')
    
  elif option_choice == 'option 3':
    print('you chose option 3')
    
  elif option_choice == 'Exit the conversation':
    print(f'Goodbye {name}, have a great day!')
    quit()
    
  else:
    print('Invalid option')
    






