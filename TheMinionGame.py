def minion_game(string):
    # your code goes here
    Kevin = 0
    Stuart = 0
    word = list(string)
    x = len(word)
    vowels = ['A','E','I','O','U']
    for inx, w in enumerate(word):
        if w in vowels:
            Kevin = Kevin + x
        else:
            Stuart = Stuart + x
        x = x - 1
    if Stuart > Kevin:
        print ('Stuart', Stuart)
    elif Kevin > Stuart:
        print ('Kevin', Kevin)
    else:
        print ('Draw')