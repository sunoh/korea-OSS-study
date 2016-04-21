from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def isValidWordinList(word, hand):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    tempHand = hand.copy()
    for letter in word:
        tempHand[letter] = tempHand.get(letter,0) - 1
    for letter in tempHand:
        if tempHand[letter] <0:
            return False
    return True

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    maxScore = 0  
    bestWord = ''
    
    for word in wordList:
        if isValidWordinList(word, hand):
            if getWordScore(word, n) > maxScore:
                maxScore = getWordScore(word, n)
                bestWord = word
            else:
                pass
        else:
            continue
    if bestWord == '':
        return None
    else:
        return bestWord


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0
    
    while calculateHandlen(hand) > 0:
        print 'Current Hand: %s' % displayHand(hand)
        
        word = compChooseWord(hand, wordList, n)
        if word == None:
            print 'Goodbye! Total score: %d points.' % score
            return None
        else:
            hand = updateHand(hand, word)
            score += getWordScore(word, n)
            print '"%s" earned %d points. Total: %d points' % \
            (word, getWordScore(word, n), score)
            print
            continue

    print
    print 'Run out of letters. Total score: %d points.' % score
    return None
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    counter = 0
    while True:
        counter += 1
        print('Enter n to deal a new hand, r to replay' \
        ' the last hand, or e to end game: ')
        choice = raw_input()
        if choice == 'n':
            hand = dealHand(HAND_SIZE)
            print('Enter u to have yourself play,' \
            ' c to have the computer play: ')
            uc = raw_input()
            if uc == 'u':
                playHand(hand, wordList, HAND_SIZE)
                continue
            elif uc == 'c':
                compPlayHand(hand, wordList, HAND_SIZE)
                continue
            else:
                print 'Invalid command.'
                continue
        elif choice =='r':
            if counter == 1:
                print 'You have not played a hand yet.',
                print ' Please play a new hand first!'
                continue
            else:
                print('Enter u to have yourself play,' \
            ' c to have the computer play: ')
                uc = raw_input()
                if uc == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    continue
                elif uc == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    continue
                else:
                    print 'Invalid command.'
                    continue
        elif choice =='e':
            break
        else:
            print 'Invalid command.'
            continue
    return None    

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


