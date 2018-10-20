# while, break, continue 


spam = 0
while spam < 5:
    print('Hello World')
    spam = spam + 1


name = ''
while name != 'Jashan':
    print('Enter your name: ')
    name = input()
print('Thank You')


name = ''
while True:
    print('Enter your name: ')
    name = input()
    if name == 'Jashan':
        break
print('Thank You')


spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is '+ str(spam))
