# If Else Statements

name = 'Jashan'
if name == 'Jashan':       # Block begins
    print('Hi Jashan')     
print('Done')


print('Enter a name.')
name = input()
if name:
    print('Thanks for entering a name')
else:
    print('You did not enter a name')




password = 'Jashan'
if password == 'JashanBansal':
    print('Access granted')
else:
    print('Access Denied')







###########              Order of elif atatements mattered                #######
name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, Kiddo')
elif age > 3000:
    print('You are a vampire, i think so')
elif age > 100:
    print('You are not Alice, grannie.')
