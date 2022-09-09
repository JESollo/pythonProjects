import random

#getAnswer() a the function 
#(answerNumber) is assigned as a parameter
#return value is stored in the answerNumber parameter. Depending on the parameters value passed by the 'r' argument, it will return 1 of 9 possible string values
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
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

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

#r is passed to the function getAnswer() as an argument
#r is assigned the random.randit() function 
#fortune is assigned the value of getAnswer(r)