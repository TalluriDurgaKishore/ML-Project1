from introduction import introduction,greeting
from data import input_data

def bot():
    name = input('Enter your name here : ')
    greeting(name)
    introduction()
    input_data()
    print()
    print('Do you want to know about something else..','1.YES','2.NO',sep='\n')
    choice = int(input('Enter your choice : '))   
    while choice == 1:
        print()
        input_data()
        print()
        print('Do you want to know about something else..','1.YES','2.NO',sep='\n')
        choice = int(input('Enter your choice : '))   
    if choice == 2:
        print()
        print('Hope this is useful','Thankyou for coming here ..🤗🤗',sep='\n') 
bot()
