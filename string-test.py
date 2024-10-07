alphabets = 'abcdefghijklmnopqrstuvwxyz'
code =  'xznlwebgjhqdyvtkfuompciasr'

secret_message = input('Enter a text: ')
secret_message = secret_message.lower()
for c in secret_message:
    if c.isalpha():
        print(alphabets[code.index(c)],end='')
    else:
        print(c, end='')
