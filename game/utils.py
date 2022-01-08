


def calculator(comp,user):
    if user=='scissor':
        if comp == 'scissor':
            output = 'neutral'
        elif comp == 'paper':
            output = 'user'
        else:
            output ='comp'
    elif user == 'rock':
        if comp == 'rock':
            output = 'neutral'
        elif comp == 'paper':
            output = 'comp'
        else:
            output ='user'
    else:
        if comp == 'scissor':
            output = 'comp'
        elif comp == 'paper':
            output = 'neutral'
        else:
            output ='user'
    return output