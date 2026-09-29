while true:
    try:
        number = int (input('enter a number: '))
        print ('you entered:',number)
    except ValueError:
        print ('invalid input. please enter a valid number')