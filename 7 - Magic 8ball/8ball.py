import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'


def sayHello(name):
    print('Hello, ' + name + '! I am the magic 8 ball\n')


r = random.randint(1, 9)
answer = getAnswer(r)

name = input('What is your name? ')
sayHello(name)
if input('Do you have a question for me? ').lower().startswith('y'):
    input('What is your question? ')
    print('\n' + answer + '\n')
else:
    input('Goodbye!\nEnter any key to quit.')
    exit()

while input('Do you have another question for me? ').lower().startswith('y'):
    input('What is your question? ')
    r = random.randint(1, 9)
    answer = getAnswer(r)
    print('\n' + answer + '\n')
else:
    input('Goodbye!\nEnter any key to quit.')
    exit()
