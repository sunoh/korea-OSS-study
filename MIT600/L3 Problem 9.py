maxNum = 100

guess = maxNum/2
bot = 0
top = maxNum

print "Please think of a number between 0 and 100"
while True:
    print "Is your secret number " + str(guess) + "?"
    ans = raw_input("Enter 'h' to indicate the guess is too high.\
    Enter 'l' to indicate the guess is too low. \
    Enter 'c' to indicate I guessed correctly.")
    if ans == 'h':
        top = guess
        guess = (guess + bot) / 2
        continue
    elif ans == 'l':
        bot = guess
        guess = (guess + top) / 2
        continue
    elif ans == 'c':
        print "Game over. Your secret number was: " + str(guess)
        break
    else:
        print "Sorry, I did not understand your input."
        continue

        
        
