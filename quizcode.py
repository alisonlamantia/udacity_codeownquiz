print "Welcome to the python knowledge quiz. What is your name?"
#asks player's name so we can address them directly
name = raw_input("")
print "Great " + name + " time to test your python knowledge."
#these are the strings and lists used in the functions
easystring='''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''
mediumstring ='''Python code is read using an ___1___. Another word for function is ___2___. Python includes pre-defined ___2___s, but we can also create new ___2___s using def. There are two types of loops in python code: ___3___ and ___4___ loops.'''
hardstring = '''When using the or statement, if the value of the first expression is ___1___, then the second expression isn't evaluated. Python is often used for data analysis. We can generate random numbers using the ___2___ function. This function is built in. Using a ___3___ helps you to structure data so you can do different things to it. For example, we can add an new element to a ___3___ using the ___4___ method. This acts like a procedure, but is a built in method, like find.'''
easyanswer = ["function", "inputs", "boolean values", "lists"]
mediumanswer = ["interpreter", "procedure", "for", "while"]
hardanswer = ["true", "randint", "list", "append"]
blanks = ['___1___','___2___','___3___','___4___']

#triggers which test text the game will use based on user input. It returns corresponding question and answers. If user doesn't select a level, they will be looped back to user input again.
def levelchoice():
    while True:
        level= raw_input("First, pick the level of difficulty. You can choose easy, medium or hard. ")
        if level == 'easy':
            return easystring, easyanswer
        if level == 'medium':
            return mediumstring, mediumanswer
        if level == 'hard':
            return hardstring, hardanswer
            break
        else:
            print "please start over and pick level easy, medium or hard"


#runs the quiz by first calling levelchoice to determine the level the user will play. It assigns the variables test and answer to the outputs of levelchoice.
#users are asked to indicate the max number of times they want to play, which is converted to an integer assigned to the variable maxplay.
#if the user answers the wrong answer, 1 is subtracted from the integer maxplay until it reaches 0. When it reaches 0 the game exits.
#the function asks the user to fill in the blank from the blanks list and compares the user's inputted answer against the correct answer in the answer list. It moves through the list using the variable i. 1 is added to i each time a correct answer is inputted.

def quiz():
    test,answer=levelchoice()
    maxplay= int(raw_input('how many times would you like to try to answer? '))
    i=0
    while i<len(answer):
        print test
        response = raw_input('What should we replace' + blanks[i] + 'with? ''')
        if response == answer[i]:
            print 'correct, good work!'
            test=test.replace(blanks[i], response)
            i+=1
            if i==len(answer):
                print 'Thanks for playing ' + name +'!'
        else:
            maxplay-=1
            if maxplay==0:
                print 'Your turns have run out. Thanks for trying'
                return
            print 'Sorry, try again'

quiz()
