x = 5
print('hello')


def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


print('Yo')
print_lyrics()
x = x + 2
print(x)
print_lyrics()


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


greet('en')

print(greet('en'), 'there')

print(greet('es'), 'there')

print(greet('fr'), 'there')