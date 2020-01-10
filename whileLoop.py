# while loops
# loop through a block of code multiple times

i = 1
while i <= 10: # loop conidition/loop guard
    print(i)
    i += 1
print('done with loop')


# building a guessing game-------------------------------------------
secretWord = 'giraffe'
#variable that will store all the guesses.
guess = ""
guessCount = 0
guessLimit = 3
outOfGuesses = False 

# prompt user to enter the secret word and if incorrect, prompt to enter it again
# can be done with a while loop

while guess != secretWord and not(outOfGuesses):
    if guessCount < guessLimit:
        guess = input('enter guess: ') # user input stored inside the guess var
        guessCount += 1
    else:
        outOfGuesses = True
if outOfGuesses:
    print("out of guesses")
else:
    print('you win')  
