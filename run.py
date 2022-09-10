from random import randint


def menu_logo():
    """
    Main menu logo and game initialisation
    """
    print("""
 _     _                                   _  _____     __
| |   | |                                 ( )/ ___ \   / /
| |__ | | ____ ____   ____ ____   ____ ___|/( (   ) ) / /_
|  __)| |/ _  |  _ \ / _  |    \ / _  |  _ \ > > < < / __ \\
| |   | ( ( | | | | ( ( | | | | ( ( | | | | ( (___) | (__) )
|_|   |_|\_||_|_| |_|\_|| |_|_|_|\_||_|_| |_|\_____/ \____/
                    (_____|
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """)
    print('Would you like to play hangman? (y)es or (n)o')
    while True:
        answer = input()
        if answer.lower() == 'y':
            rules()
            break
        elif answer.lower() == 'n':
            print("""
 ..|'''.|                       '||  '||
.|'     '    ...     ...      .. ||   || ...  .... ...   ....
||    .... .|  '|. .|  '|.  .'  '||   ||'  ||  '|.  |  .|...||
'|.    ||  ||   || ||   ||  |.   ||   ||    |   '|.|   ||
 ''|...'|   '|..|'  '|..|'  '|..'||.  '|...'     '|     '|...'
                                              .. |
                                               ''
            """)
            exit()
        else:
            print("Please enter a valid option")


def rules():
    """
    Displays the rules of the game before the game starts
    """
    print("""
  ____        _
 |  _ \ _   _| | ___  ___
 | |_) | | | | |/ _ \/ __|
 |  _ <| |_| | |  __/\__ \\
 |_| \_\\__,_|_|\___||___/
    Choose a letter and press enter to play your guess.
    If your guess is correct, the letter will be displayed in its
    relevant position in the word.
    If your guess is incorrect, the hangman gallows will build up.
    You have 8 guesses.
    """)
    print('Do you want to continue?  (y)es or (n)o:')
    while True:
        answer = input()
        if answer.lower() == 'y':
            set_difficulty()
            break
        elif answer.lower() == 'n':
            print("""
 ..|'''.|                       '||  '||
.|'     '    ...     ...      .. ||   || ...  .... ...   ....
||    .... .|  '|. .|  '|.  .'  '||   ||'  ||  '|.  |  .|...||
'|.    ||  ||   || ||   ||  |.   ||   ||    |   '|.|   ||
 ''|...'|   '|..|'  '|..|'  '|..'||.  '|...'     '|     '|...'
                                              .. |
                                               ''
        """)
            exit()
            break
        else:
            print("Please enter a valid option")


def set_difficulty():
    """
    Asks player to set difficulty
    """
    print("\n")
    print(" Select your difficulty level\n")
    print(
        " Press 1 for Level 1, 4 letter word"
        )
    print(
        " Press 2 for Level 2, 6 letter word"
        )
    print(
        " Press 3 for Level 3, 8 letter word"
        )
    difficulty = False
    while not difficulty:
        options = input("\n ").upper()
        if options == "1":
            difficulty = True
            letter_count = 4
            return letter_count
            play()
            break
        elif options == "2":
            difficulty = True
            letter_count = 6
            return letter_count
            play()
            break
        elif options == "3":
            difficulty = True
            letter_count = 8
            return letter_count
            play()
            break
        else:
            print("\n Please select 1, 2 or 3 to make your choice")


def getRandomWord():
    """
    Picks a random word to be used for the players guess from the
    answers.txt file
    """
    wordFile = open('answers.txt', 'r')
    words = wordFile.readlines()
    wordFile.close()
    return words[randint(0, len(words)-1)][0:-1]


def play():
    """
    Play the game. Incorrect letters draw out the hangman
    until the image is complete and it is game over.
    """
    word = getRandomWord()
    progress = ''
    for i in range(len(word)):
        progress += '_'
    incorrect = 0
    letters = []
    while True:
        letterString = ''
        for i in range(len(letters)):
            if i != len(letters) and i != 0:
                letterString += ', '
            letterString += letters[i]
        print(drawMan(incorrect))
        print(f'Letters used: {letterString}')
        if progress == word:
            print(progress)
            print(user_wins())
            restart_game()
            break
        if incorrect >= 8:
            print(user_loses())
            print(f'The word was {word}.')
            restart_game()
            break
        print(progress)
        print(f'Number of incorrect guesses {incorrect}')
        print('Guess a letter!')
        userInput = input()
        if userInput not in letters:
            letters.append(userInput)
        if userInput in word:
            print(f'The letter {userInput} is in the word.')
            for i in range(len(word)):
                if userInput == word[i]:
                    progressStart = progress[0:i]
                    progressEnd = progress[i+1:]
                    progress = progressStart + userInput + progressEnd
        elif len(userInput) > 1:
            print('You can only guess 1 letter at a time')
        elif not userInput.isalpha():
            print(f"You can only guess letters, you guessed {(userInput)}")
        else:
            print(f'The letter {userInput} is not in the word. Try Again.')
            incorrect += 1


def restart_game():
    """
    When game ends user to choose to restart the game or exit
    """
    while True:
        choice = input("Would you like to play again?  (y)es or (n)o:\n")
        if choice == "y":
            set_difficulty()
            main(False)
        elif choice == "n":
            print("""
 ..|'''.|                       '||  '||
.|'     '    ...     ...      .. ||   || ...  .... ...   ....
||    .... .|  '|. .|  '|.  .'  '||   ||'  ||  '|.  |  .|...||
'|.    ||  ||   || ||   ||  |.   ||   ||    |   '|.|   ||
 ''|...'|   '|..|'  '|..|'  '|..'||.  '|...'     '|     '|...'
                                              .. |
                                               ''
        """)
            exit()
        else:
            print("Please enter a valid option")
        


def drawMan(incorrect):
    """
    Draws hangman gallow and stick figure in increments
    up to 8 until a complete hangman is drawn
    """
    if incorrect == 0:
        return """






        """
    if incorrect == 1:
        return """
        |
        |
        |
        |
        |
        ========
        """
    if incorrect == 2:
        return """
        |/
        |
        |
        |
        |
        |\\
        ========
        """
    if incorrect == 3:
        return """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """
    if incorrect == 4:
        return """
        __________
        |/        |
        |
        |
        |
        |
        |\\
        ========
        """
    if incorrect == 5:
        return """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """
    if incorrect == 6:
        return """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """
    if incorrect == 7:
        return """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """
    if incorrect == 8:
        return """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """


def user_wins():
    """
    You Won logo displayed when player wins game
    """
    print("""
 _     _  _____  _   _     _       _  _____  _   _
( )   ( )(  _  )( ) ( )   ( )  _  ( )(  _  )( ) ( )
`\`\_/'/'| ( ) || | | |   | | ( ) | || ( ) || `\| |
  `\ /'  | | | || | | |   | | | | | || | | || , ` |
   | |   | (_) || (_) |   | (_/ \_) || (_) || |`\ |
   (_)   (_____)(_____)   `\___x___/'(_____)(_) (_)
""")


def user_loses():
    """
    You Lost logo displayed when player loses game
    """
    print("""

 _     _  _____  _   _     _      _____  ___   _____
( )   ( )(  _  )( ) ( )   ( )    (  _  )(  _`\(_   _)
`\`\_/'/'| ( ) || | | |   | |    | ( ) || (_(_) | |
  `\ /'  | | | || | | |   | |  _ | | | |`\__ \  | |
   | |   | (_) || (_) |   | |_( )| (_) |( )_) | | |
   (_)   (_____)(_____)   (____/'(_____)`\____) (_)
    """)


def main(first_run):
    """
    Runs the game
    """
    if first_run:
        print(drawMan(0))
        menu_logo()
    
    getRandomWord()
    play()


main(True)