message = 'Hello World'

withslashhello = 'Let\'s'  #escape sequence
orwithlash_use_doublequotes = "Let's"
withsinlequotes='My "Bingo"'
sentence = """Hello Everybody
This is 3 line sentence
Thank You"""
print(withslashhello)
print(orwithlash_use_doublequotes)
print(withsinlequotes)
print(sentence)
print(len(sentence))
print(sentence.count('is'))

message = message.replace('World', 'Universe') #it will return a new string so need to save that in new variable
#print(message)

greeting= 'Hello'

name = 'Daksh'

message_1= '{}, {}. Welcome!'.format(greeting,name);

#show us all the attributes and methods we can use for the given variable
#print(dir(message_1))

#show the description of attribute/method we can use
#print(help(str))

#show description of particular attribute 
#print(help(str.upper))



