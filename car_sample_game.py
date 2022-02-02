from distutils import command


comand = " "
while comand != 'quit':
    comand = input("> ").lower()
    if comand == "start":
        print('Car started ...')

    elif comand == "stop":
        print('Car stopped ...')

    elif comand == "help":
        print('''
        start - to start the car
        stop - to stop the car
        quit - to quit
        ''')
    else:
        print('Sorry I do not understand that!')

