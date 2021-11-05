import random
print(" ------------------------------------------------")
print("|                                                |")
print("|    Hangman                                     |")
print("|    Name : Leo                                  |")
print("|    Version : 01                                |")
print("|                                                |")
print(" ------------------------------------------------")
words = ['tree', 'mango', 'coding', 'human', 'python', 'java',
         'hangman', 'amazon', 'help', 'football', 'cricket', 'direction', 'dress', 'apology', 'driver', 'ship', 'pilot', 'paper', 'laptop'
         'chair', 'maths', 'snake', 'paint']
guess = words[random.randint(0, len(words)-1)].upper()
display = []
for x in guess:
    display.append("_")
print("-----Game of hangman has started-----")
print("")
print("Guess a letter! ", end=" ")
indexes = []
limbs = 8
userWon = False
userLost = False
guessedLetters = []

def start(word, indexes, display, limbs, userWon, userLost, guessedLetters):
    chance = False 
    wrong_guess = False
    word_found = "" 
    if userLost == False:
        if len(indexes) > 0:  
            for val in indexes:
                display[val] = word[val]
        if limbs == 1:
            print("Careful, you can only mess up once more.")
        if limbs == 2:
            print("You have", limbs, "chances to mess up left")
            print("")
            print("Wrong Guesses", guessedLetters)
            print("")
        if limbs == 3:
            print("You have", limbs, "chances to mess up left")
            print("")
            print("Wrong Guesses", guessedLetters)
            print("")
        if limbs == 4:
            print("You have", limbs, "chances to mess up left")
            print("")
            print("Wrong Guesses", guessedLetters)
            print("")
        if limbs == 5:
            print("You have", limbs, "chances to mess up left")
            print("")
            print("Wrong Guesses", guessedLetters)
            print("")
        if limbs == 6:
            print("You have", limbs, "chances to mess up left")
            print("")
            print("Wrong Guesses", guessedLetters)
            print("")
        if limbs == 7:
            print("You have", limbs, "chances to mess up left")
            print("")
            print("Wrong Guesses", guessedLetters)
            print("")
        if limbs == 8:
            print("You have", limbs, "chances to mess up left")
            print("")
            print("Wrong Guesses", guessedLetters)
            print("")
        if limbs == 0:
            userLost = True
        for dash in display:
            print(dash, end=" ")
        print("")
        print("")
        user_guessed = input(
            "Guess by entering a letter or the complete word to win: ").upper()
        if len(user_guessed) == 1: 
            word_found = False
            for i in range(len(word)): 
                if(word[i] == user_guessed): 
                    if i in indexes: 
                        print("You already guessed the letter ", word[i])
                        chance = True
                        word_found = True
                        break
                    else:
                        indexes.append(i)
                        print("Nice guess it was ", word[i])
                        word_found = True
        elif len(user_guessed) > 1: 
            if(word == user_guessed):
                print("Nice, you won! There is no prize.")
                print("The correct word was ", word)
                userWon = True
            else:
                wrong_guess = True
        if user_guessed in guessedLetters: 
            print("You already tried ", user_guessed)
            chance = True
        elif wrong_guess == True or word_found == False: 
            guessedLetters.append(user_guessed)
            print("Sorry, nope")
            limbs -= 1
            if limbs == 0:
                userLost = True
            else: 
                chance = True
        if chance == True:
            start(word, indexes, display, limbs,
                  userWon, userLost, guessedLetters)
            chance = False 
        elif len(indexes) > 0 and userWon == False and userLost == False and chance == False:
            if len(indexes) == len(word): 
                print("Good job, you good guesser")
                print(word, " was indeed the word")
            else:
                start(word, indexes, display, limbs,
                      userWon, userLost, guessedLetters)
        elif userLost == True: 
            print("You lost.")
            print("The correct word was ", word)
start(guess, indexes, display, limbs, userWon, userLost, guessedLetters)