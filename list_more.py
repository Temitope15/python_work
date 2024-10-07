from string import punctuation
text = input('Describe your day \n')

sum = 0
for c in punctuation:
    text = text.replace(c, '')



for c in text:
    if c != ' ':
        sum+=1
print(f'characters count: {sum}')
print(f'Word count: {len(text.split())}')