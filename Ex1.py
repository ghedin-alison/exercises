import datetime
name = input('What\'s your name?\n')
idade = int(input('How old are you?\n'))
repeat = int(input('How many times you want to repeat the answer?\n'))

x = datetime.datetime.now()

birth_date = x.year - idade
hundred_years = int(birth_date + 100)
answer = f'{name}, you\'ll be 100 years old in {hundred_years}.'

for i in range(repeat):
    print(answer)