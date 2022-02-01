
name = input('what is your name? ')
# print('Hi '+ name) # this is concatination

color = input('What is your favourite color? ')

print(name + ' Likes color ' + color)

# Year
 


birth_year = input('Enter the year that you were born: ')
age = 2022 - int(birth_year)
print(age)

print(type(birth_year))



# converting weight to kilograms

pounds = input('Enter the weight in pounds: ')

kg = float(pounds)/20
kg = str(kg)
print( kg + ' kilograms')




# this is on strings

course = 'python Course for beginners' 
# strings used esp in emails


course = '''
Hi Desmond,
this is our first mail to you
Thank you for being a valued member
'''
print(course)


name = 'Jennifer'
print(name[1:-1])


### formatted string

first = 'Desmond'
last = 'Onam'

message = first + '[' + last + '] is a coder'
# print(message)

# simple one by formatted string

msg = f'{first} [{last}] is a coder'
print(msg)